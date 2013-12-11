#!/var/www/ctcblog/web/mio/bin/python

from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
	WSGIServer(app).run()
