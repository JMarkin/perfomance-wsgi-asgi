import uvloop

uvloop.install()

from .fastapi_app import app as fastapi_app
from .falcon_wsgi_app import app as falcon_wsgi_app
from .falcon_asgi_app import app as falcon_asgi_app
