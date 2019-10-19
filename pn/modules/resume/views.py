"""
    Resume views
    ============

    This module defines the views responsible for exposing information for the resume website.

"""

import datetime as dt

from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template


resume_blueprint = Blueprint('resume', __name__)


@resume_blueprint.route('/', methods=['GET', ])
def home():
    """ The main entrypoint of the resume web application. """
    now_dt = dt.datetime.now()
    return render_template(
        'resume/home.html',
        age=relativedelta(now_dt, dt.datetime(day=19, month=3, year=1983)).years,
        current_year=now_dt.year,
    )


@resume_blueprint.route('/details', methods=['GET', ])
def details():
    """ The main entrypoint of the resume web application. """
    now_dt = dt.datetime.now()
    return render_template(
                           'resume/home.html',
                           age=relativedelta(now_dt, dt.datetime(day=19, month=3, year=1983)).years,
                           current_year=now_dt.year,
                           )


@resume_blueprint.route('/download', methods=['GET', ])
def download():
    """ The main entrypoint of the resume web application. """
    now_dt = dt.datetime.now()
    return render_template(
                           'resume/home.html',
                           age=relativedelta(now_dt, dt.datetime(day=19, month=3, year=1983)).years,
                           current_year=now_dt.year,
                           )
