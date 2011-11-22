import datetime
from dictshield.document import Document
from dictshield.fields import StringField
from dictshield.fields import ObjectIdField
from dictshield.fields import IntField
from dictshield.fields import DateTimeField
import simplejson as json

import redis

class Client(object):
    def __init__(self, **kwargs):
        self.connection_settings = kwargs or {'host': 'localhost',
                'port': 6379, 'db': 0}

    def redis(self):
        return redis.Redis(**self.connection_settings)

    def update(self, d):
        self.connection_settings.update(d)

def connection_setup(**kwargs):
    global connection, client
    if client:
        client.update(kwargs)
    else:
        client = Client(**kwargs)
    connection = client.redis()

def get_client():
    global connection
    return connection

client = Client()
connection = client.redis()

class BaseDocument(Document):

    def save(self, redis_client = None):
	redis_client = redis_client or connection
	if self.key is None:
	    #generate the key as well
	    id = redis_client.incr('global_unique_counter')
	    self.id = id
	    self.key = '%s%s' % (self.key_prefix, id)

	redis_client.set(self.key, self.to_json())
	return self

    @classmethod
    def get(cls, id, redis_client = None):
	"""Quick helper function to retrieve an object"""
	redis_client = redis_client or connection
	key = '%s%s' % (cls.key_prefix, id)
	json_str = redis_client.get(key)
	if json_str:
	    return cls(**json.loads(json_str)) 
	else:
	    return None

    @classmethod
    def multi_get(cls, redis_client, *keys):
	"""Quick helper function to retrieve an object"""
	redis_client = redis_client or connection
	if not keys:
	    return []
	redis_strings = redis_client.mget(*keys)
	objects = []
	for json_str in redis_strings:
	    if json_str:
		objects.append(cls(**json.loads(json_str)))
	return objects
    
    @classmethod
    def get_all(cls, redis_client = None):
	"""Quick helper function to retrieve an object"""
	redis_client = redis_client or connection
	keys = redis_client.keys('%s*' % (cls.key_prefix))
	if keys:
	    return cls.multi_get(redis_client, *keys)
	else:
	    return []

    def reload(self, redis_client = None):
	"""Quick function to reload current object from datastore"""
	redis_client = redis_client or connection
	self = self.__class__.get(self.key, redis_client) 
	return self

    def delete(self, redis_client = None):
	"""Quick function to delete a redis client"""
	redis_client = redis_client or connection
	redis_client.delete(self.key)

class Conference(BaseDocument):
    id = StringField(default = None)
    key = StringField(default = None)
    url_title = StringField()
    title = StringField(required = True)
    desc = StringField()
    venue = StringField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    twitter_handle = StringField()
    twitter_hashcode = StringField()

    url_key_prefix = 'conference:url:'
    key_prefix = 'conference:id:'
    session_set_prefix = 'conference:sessions:'

    def update_url_key(self, redis_client = None):
	redis_client = redis_client or connection
	url_key = '%s%s' % (Conference.url_key_prefix, self.url_title)
	redis_client.set(url_key, self.id)
    
    @staticmethod
    def get_id_from_url_title(url_title, redis_client = None):
	redis_client = redis_client or connection
	url_key = '%s%s' % (Conference.url_key_prefix, url_title)
	return redis_client.get(url_key)

    def add_session(self, session, redis_client = None):
	set_key = '%s%s' % (Conference.session_set_prefix, self.id)
	import time
	redis_client = redis_client or connection
	redis_client.zadd(set_key, **{'%s' % (session.id): time.mktime(session.start_date.timetuple())})

    def get_sessions_keys(self, redis_client = None):
	redis_client = redis_client or connection
	set_key = '%s%s' % (Conference.session_set_prefix, self.id)
	session_keys = ['%s%s' % (Session.key_prefix, x) for x in redis_client.zrange(set_key, 0, 100)]
	return session_keys


class Session(BaseDocument):
    id = StringField(default = None)
    key = StringField(default = None)
    conf_id = StringField(required = True)
    talk_type = StringField(default = 'Talk')
    title = StringField(required = True)
    desc = StringField()
    venue = StringField()
    duration = IntField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    speaker_title = StringField()

    key_prefix = 'session:id:'

    def json_friendly(self):
	day = self.start_date.strftime('%A') 
	time_label = '%s' % (self.start_date.strftime('%I:%M%p'))
	d = self.to_json(encode = False)
	d['day'] = day
	d['time_label'] = time_label
	return d

class Speaker(BaseDocument):
    id = StringField(default = None)
    key = StringField(default = None)
    first_name = StringField()
    last_name = StringField()
    desc = StringField()
    twitter_handle = StringField()

    key_prefix = 'speaker:id:'
