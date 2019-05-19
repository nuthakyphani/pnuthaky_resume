"""
    Assets context processors
    =========================

    This module defines context processors related to the assets extension.

"""

import json
import os

from flask import current_app, url_for


def webpack_assets():
    """ Inserts a function allowing to retrieve asset URLs into the context. """
    asset_str = _get_asset
    print('Assest %s',asset_str)
    return {
        'asset_url': asset_str,
    }


def _get_asset(path):
    """ Returns the URL for a given asset by looking at the webpack manifest first. """
    assets = current_app.extensions['webpack']['assets']
    print assets
    webpack_manifest_path = os.path.join(
        os.path.dirname(__file__),
        '../../static/build/' if not current_app.debug else '../../static/build_dev/',
        'manifest.json',
    )
    print ('Manifest path %s', webpack_manifest_path)
    # In debug mode, files are read each request.
    if assets is None or current_app.debug:
        try:
            with open(webpack_manifest_path) as fp:
                assets = json.load(fp)
        except IOError:
            current_app.logger.exception('Unable to load webpack manifest')
            assets = {}
            print("Unable to load assets manifest")
        current_app.extensions['webpack']['assets'] = assets
    filename = assets.get(path, path)
    print ("Context filename: %s", filename)
    return url_for('static', filename=assets.get(path, path))
