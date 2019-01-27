#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of server.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Jacek Burys <jacekburys@gmail.com>


from flask import Blueprint



mod = Blueprint('healthcheck', __name__)


@mod.route("/healthcheck/")
def healthcheck():
    

    return 'WORKING'
