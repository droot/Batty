#!/usr/bin/env python

from brubeck.request_handling import Brubeck
from brubeck.templating import load_mako_env

from handlers import (ConferenceManagementHandler,
		    SessionManagementHandler,
		    SpeakerManagementHandler,
		    IndexPageHandler,
		    ShopifyHandler,
		    LoginHandler)
import app_config

# Routing config
handler_tuples = [
    (r'^/shopify_callback', ShopifyHandler),
    (r'^/login', LoginHandler),
    #(r'^/confs/(?P<id>\w+)', ConferenceManagementHandler),
    #(r'^/confs', ConferenceManagementHandler),
    #(r'^/sessions/(?P<id>\w+)', SessionManagementHandler),
    #(r'^/sessions', SessionManagementHandler),
    #(r'^/speakers/(?P<id>\w+)', SpeakerManagementHandler),
    #(r'^/speakers', SpeakerManagementHandler),
    #(r'^/(?P<conf_handle>\w+)', IndexPageHandler),
    #(r'^/$', IndexPageHandler),
]

_batty_config = app_config.get_config()
# Application config
config = {
    'mongrel2_pair': ('tcp://127.0.0.1:9999', 'tcp://127.0.0.1:9998'),
    'handler_tuples': handler_tuples,
    'template_loader': load_mako_env(_batty_config.get('template_path'),
			input_encoding='utf-8',
			output_encoding='utf-8',
			encoding_errors='replace',
			default_filters=['escape'],
			imports=['from webhelpers.html import escape'])
    #'db_conn': db_conn,
    #'login_url': '/login',
    #'cookie_secret': 'OMGSOOOOOSECRET',
}
config.update(_batty_config)

# Instantiate app instance
app = Brubeck(**config)
app.run()
