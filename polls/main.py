import logging

import aiohttp_jinja2
import jinja2
from aiohttp import web

from config.settings import config
from polls.middlewares import setup_middlewares
from polls.models import init_pg, close_pg
from polls.routes import setup_routes

logging.basicConfig(level=logging.DEBUG)
app = web.Application()
setup_routes(app)
setup_middlewares(app)
app['config'] = config

# setup Jinja2 template renderer
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('polls', 'templates'))

# signals for db connection on start and close on shutdown
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)


web.run_app(app)
