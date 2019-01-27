#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of server.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Jacek Burys <jacekburys@gmail.com>

import os.path
import logging
from os import walk
import mimetypes
from cStringIO import StringIO
import gzip as gzip_module

from flask import current_app
from flask.ext.script import Manager, Shell
from flask.ext.assets import ManageAssets

from server.app import create_app
from server.static.assets import assets_env


def main():
    manager = Manager(create_app)
    conf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config', 'local.conf'))
    manager.add_option('-c', '--config', dest='config', default=conf_path, required=False)
    manager.add_option('-d', '--debug', dest='debug', default=False, required=False, action='store_true')
    asset_manager = ManageAssets(assets_env)
    manager.add_command("assets", asset_manager)

    def _make_context():
        return dict(app=current_app, db=models.db, models=models)
    manager.add_command("shell", Shell(make_context=_make_context))

    manager.run()


if __name__ == "__main__":
    main()
