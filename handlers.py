import sys
from brubeck.request_handling import Brubeck, WebMessageHandler
from brubeck.templating import MakoRendering, load_mako_env
from wsgi_bridge import Request, Context, Response
from mako.template import Template
from mako.lookup import TemplateLookup
from app_config import get_config
import simplejson as json

from models import Conference, Session, Speaker
from dateutil.parser import parse

import logging
import shopify

log = logging.getLogger(__name__)

class BaseHandler(WebMessageHandler, MakoRendering):
    """Base handler class which every other handler will be inheriting
    """

    def prepare(self):
	self.config = get_config()
	shopify.Session.setup(api_key = self.config.get('shopify_apikey'),
			    secret = self.config.get('shopify_secret'))
	self.wsgi_request = Request(self)
	self.wsgi_response = Response(self)
	self.context = Context()

    def render_stuff(self, template_name):

	context = {
		    'config': get_config(),
		    'request': self.wsgi_request,
		    'c': self.context,
		    }
	return self.render_template(template_name, **context)

class ShopifyHandler(BaseHandler):
    def get(self):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	#response.headers['content-type'] = 'application/json'

	shop_url = request.params.get('shop')
	shopify_params = {'shop': shop_url,
			't': request.params.get('t'),
			'timestamp': request.params.get('timestamp'),
			'signature': request.params.get('signature')}

	log.info('Login post handler... params: %s' % (shopify_params))
	shopify_session = shopify.Session(shop_url, params = shopify_params)

	#self.set_body('Login post handler... %s' % (shopify_session))
	self.set_body('Login post handler... params: %s' % (shopify_params))
	return self.render()
	#return self.render_stuff('/')

    def post(self):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	shop_url = request.params.get('shop')
	shopify_session = shopify.Session(shop_url, request.params)

	self.set_body('Login post handler... %s' % (shopify_session))
	#response.headers['content-type'] = 'application/json'
	return self.render()

class LoginHandler(BaseHandler):
    def get(self):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	#response.headers['content-type'] = 'application/json'

	shop = request.params.get('shop')
	if shop:
	    permission_url = shopify.Session.create_permission_url(shop.strip())
	    #return redirect(permission_url)
	    self.set_body('Lets login.... perm url %s' % (permission_url))
	    self.redirect(permission_url)
	else:
	    self.set_body('Lets login....')
	return self.render()
	#return self.render_stuff('/')

    def post(self):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	self.set_body('Login post handler...')
	#response.headers['content-type'] = 'application/json'
	return self.render()


class SessionManagementHandler(BaseHandler):
    def get(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	response.headers['content-type'] = 'application/json'

	if id is None:
	    #get all the sessions
	    conf_id = request.params.conf_id
	    if conf_id:
		conf = Conference.get(conf_id)
		session_keys = conf.get_sessions_keys()
		log.info('request for sessions for conf_id %s with sessions: %s' % (conf.id, session_keys))
		sessions = [x.json_friendly() for x in Session.multi_get(None, *session_keys)]
	    else:
		sessions = [x.json_friendly() for x in Session.get_all()]
	    #for s in sessions:
		#s['day'] = s.get('start_date').strftime('%A') 
		#s['time_label'] = s.get('start_date').strftime('%I:%M %p')
	    self.set_body(json.dumps(sessions))
	else:
	    session = Session.get(id)
	    self.set_body(session.to_json())
	return self.render()
	#return self.render_stuff('/')

    def post(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	param_dict = dict(
		title = request.params.title,
		conf_id = request.params.conf_id,
		desc = request.params.desc,
		venue = request.params.venue,
		talk_type = request.params.talk_type,
		start_date = parse(request.params.start_date),
		end_date = parse(request.params.end_date),
		duration = request.params.duration,
		speaker_title = request.params.speaker_title)
	content = param_dict
	session = Session(**param_dict)
	session = session.save()

	conf = Conference.get(session.conf_id)
	if conf:
	    conf.add_session(session)

	self.set_body(session.to_json())
	response.headers['content-type'] = 'application/json'
	return self.render()

    def put(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	if id is None:
	    self.set_body('Conf id is a Must')
	else:
	    session = Session.get(id)
	    if request.params.title: session.title = request.params.title
	    if request.params.desc: session.desc = request.params.desc
	    if request.params.conf_id: session.conf_id = request.params.conf_id
	    if request.params.venue: session.venue = request.params.venue
	    if request.params.talk_type: session.type = request.params.talk_type
	    if request.params.start_date: session.start_date = parse(request.params.start_date)
	    if request.params.end_date: session.end_date = parse(request.params.end_date)
	    if request.params.duration: session.duration = request.params.duration
	    if request.params.speaker_title: session.speaker_title = request.params.speaker_title
	    session = session.save()
	    self.set_body(session.to_json())
	return self.render()
    
    def delete(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	if id is None:
	    self.set_body('session id is a Must')
	else:
	    session = Session.get(id)
	    if session is None:
		self.set_body('No conference with %d exist' % (id))
	    else:
		session.delete()
		self.set_body("Deleted Successfully...")
	return self.render()

class ConferenceManagementHandler(BaseHandler):
    def get(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	response.headers['content-type'] = 'application/json'

	if id is None:
	    #get all the confs
	    confs = [x.to_json(encode = False) for x in Conference.get_all()]
	    self.set_body(json.dumps(confs))
	else:
	    conf = Conference.get(id)
	    self.set_body(conf.to_json())
	return self.render()
	#return self.render_stuff('/')

    def post(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	param_dict = dict(
		url_title = request.params.url_title,
		title = request.params.title,
		desc = request.params.desc,
		venue = request.params.venue,
		start_date = parse(request.params.start_date),
		end_date = parse(request.params.end_date),
		twitter_handle = request.params.twitter_handle,
		twitter_hashcode = request.params.twitter_hashcode)
	content = param_dict
	conf = Conference(**param_dict)
	conf = conf.save()
	conf.update_url_key()
	self.set_body(conf.to_json())
	response.headers['content-type'] = 'application/json'
	return self.render()

    def put(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	if id is None:
	    self.set_body('Conf id is a Must')
	else:
	    conf = Conference.get(id)
	    if request.params.title: conf.title = request.params.title
	    if request.params.url_title: conf.url_title = request.params.url_title
	    if request.params.desc: conf.desc = request.params.desc
	    if request.params.venue: conf.venue = request.params.venue
	    if request.params.start_date: conf.start_date = parse(request.params.start_date)
	    if request.params.end_date: conf.end_date = parse(request.params.end_date)
	    if request.params.twitter_handle: conf.twitter_handle = request.params.twitter_handle
	    if request.params.twitter_hashcode: conf.twitter_hashcode = request.params.twitter_hashcode
	    conf = conf.save()
	    conf.update_url_key()
	    self.set_body(conf.to_json())
	return self.render()
    
    def delete(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	if id is None:
	    self.set_body('Conf id is a Must')
	else:
	    conf = Conference.get(id)
	    if conf is None:
		self.set_body('No conference with %d exist' % (id))
	    else:
		conf.delete()
		self.set_body("Deleted Successfully...")
	return self.render()


class SpeakerManagementHandler(BaseHandler):
    def get(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	response.headers['content-type'] = 'application/json'

	if id is None:
	    #get all the speakers
	    speakers = [x.to_json(encode = False) for x in Speaker.get_all()]
	    self.set_body(json.dumps(speakers))
	else:
	    speaker = Speaker.get(id)
	    self.set_body(speaker.to_json())
	return self.render()
	#return self.render_stuff('/')

    def post(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	param_dict = dict(
		first_name = request.params.first_name,
		last_name = request.params.last_name,
		desc = request.params.desc,
		twitter_handle = request.params.twitter_handle)
	content = param_dict
	speaker = Speaker(**param_dict)
	speaker = speaker.save()
	self.set_body(speaker.to_json())
	response.headers['content-type'] = 'application/json'
	return self.render()

    def put(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	if id is None:
	    self.set_body('speaker id is a Must')
	else:
	    speaker = Speaker.get(id)
	    if request.params.first_name: speaker.first_name = request.params.first_name
	    if request.params.last_name: speaker.last_name = request.params.last_name
	    if request.params.desc: speaker.desc = request.params.desc
	    if request.params.twitter_handle: speaker.twitter_handle = request.params.twitter_handle
	    speaker = speaker.save()
	    self.set_body(speaker.to_json())
	return self.render()
    
    def delete(self, id = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context
	if id is None:
	    self.set_body('speaker id is a Must')
	else:
	    speaker = Speaker.get(id)
	    if speaker is None:
		self.set_body('No speakererence with %d exist' % (id))
	    else:
		speaker.delete()
		self.set_body("Deleted Successfully...")
	return self.render()


class IndexPageHandler(BaseHandler):
    def get(self, conf_handle = None):
	request = self.wsgi_request
	response = self.wsgi_response
	c = self.context

	if conf_handle:
	    conf_id = Conference.get_id_from_url_title(conf_handle)
	    c.conf = Conference.get(conf_id)
	    if c.conf:
		return self.render_stuff('/index.html')	
	
	self.set_body("Please enter a valid conference handle..")
	return self.render()
