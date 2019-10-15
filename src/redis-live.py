import os

import tornado.ioloop
import tornado.options
from tornado.options import define, options
import tornado.web

from src.api.controller.BaseStaticFileHandler import BaseStaticFileHandler

from src.api.controller.ServerListController import ServerListController
from src.api.controller.InfoController import InfoController
from src.api.controller.MemoryController import MemoryController
from src.api.controller.CommandsController import CommandsController
from src.api.controller.TopCommandsController import TopCommandsController
from src.api.controller.TopKeysController import TopKeysController

if __name__ == "__main__":
    define("port", default=8888, help="run on the given port", type=int)
    define("debug", default=0, help="debug mode", type=int)
    tornado.options.parse_command_line()
    current_dir = os.getcwd()
    static_folder = os.path.join(current_dir, 'www')

    # Bootup
    handlers = [
        (r"/api/servers", ServerListController),
        (r"/api/info", InfoController),
        (r"/api/memory", MemoryController),
        (r"/api/commands", CommandsController),
        (r"/api/topcommands", TopCommandsController),
        (r"/api/topkeys", TopKeysController),
        (r"/(.*)", BaseStaticFileHandler, {"path": static_folder})
    ]

    server_settings = {'debug': options.debug, 'autoreload': True, 'static_hash_cache': False}
    application = tornado.web.Application(handlers, **server_settings)
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
