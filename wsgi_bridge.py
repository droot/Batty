class Cookies(object):
    def __init__(self, handler):
	self.handler = handler

    def _get(self, attrib, default = None):
	"""internal get method"""
	return self.handler.get_cookie(attrib, default)

    def __getitem__(self, index):
	return self._get(index)

    def __getattr__(self, name):
	return self._get(name)

    def get(self, name, default = None):
	return self._get(name, default)

    def __repr__(self):
	return '%s' % self.handler.cookies


class Params(object):
    def __init__(self, handler):
	self.handler = handler

    def _get(self, attrib, default = None):
	"""internal get method"""
	return self.handler.get_argument(attrib, default)

    def __getitem__(self, index):
	return self._get(index)

    def __getattr__(self, name):
	return self._get(name)

    def get(self, name, default = None):
	return self._get(name, default)

class Context(object):
    def __getattr__(self, name, default = None):
	return self.__dict__.get(name, default)

    def __setattr__(self, name, value):
	self.__dict__[name] = value

class Request(object):
    """Request class which emulates behavior
    of webob.request class
    """
    def __init__(self, handler):
	self.params = Params(handler)
	self.environ = {}
	self.cookies = Cookies(handler)

class Response(object):
    """Response class which emulates behavior
    of webob.response class
    """
    def __init__(self, handler):
	self.handler = handler
	self.cookies = Cookies(handler)

    @property
    def headers(self):
	return self.handler.headers

    def set_cookie(self, name, value, expires = None, **kwargs):
	self.handler.set_cookie(name, value, expires = expires, **kwargs)
