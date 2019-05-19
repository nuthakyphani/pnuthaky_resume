#!/usr/bin/env python

"""
    The autoapp module
    ==================

    This module creates an instance of the Flask application.

"""

import os
import sys
import logging
from pn import create_app

##Replace the standard out
sys.stdout = sys.stderr

##Add this file path to sys.path in order to import settings
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
if __name__ == "__main__":
    app.run(ssl_context=('fullchain.pem', 'privkey.pem'))
