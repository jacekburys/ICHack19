#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of server.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Jacek Burys <jacekburys@gmail.com>

from datetime import datetime

from flask import Blueprint, render_template, current_app




mod = Blueprint('index', __name__)


@mod.route("/")
def index():
    
    users = []
    
    return render_template('index.html', dt=datetime.now().strftime("%d %M %Y - %H %m %s"), users=users)
