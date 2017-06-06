from flask import render_template

from . import about_us


@home.route('/about_us')
def about_us():
    """Render the about us template on the /about_us route"""
    categories = Category.query.all()
    events_services = EventService.query.all()
    return render_template(
        'about_us.html',
        title="About Us",
        categories=categories,
        events_services=events_services)

