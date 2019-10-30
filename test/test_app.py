# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'src'))
import app


def test_app_add():
    assert app.add(0, 1) == 1
