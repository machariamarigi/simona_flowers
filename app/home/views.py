from flask import render_template, abort
from flask_login import login_required, current_user

from . import home
from ..models import Category, EventService


@home.route('/')
def homepage():
    """Render the homepage template on the / route"""
    categories = Category.query.all()
    events_services = EventService.query.all()
    return render_template(
        'home/index.html',
        title="Welcome",
        categories=categories,
        events_services=events_services)


@home.route('/admin/home')
@login_required
def admin_home():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_home.html', title="Admin Landing")

