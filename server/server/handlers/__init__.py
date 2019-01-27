#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of server.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Jacek Burys <jacekburys@gmail.com>


from server.handlers import (
    healthcheck,
    index,
    process_image
    # add your own handlers here
)


def init_app(app):
    app.register_blueprint(healthcheck.mod)
    app.register_blueprint(index.mod)
    app.register_blueprint(process_image.mod)
