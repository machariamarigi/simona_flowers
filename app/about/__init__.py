from flask import Blueprint

about_us = Blueprint('about_us', __name__)

from . import views
