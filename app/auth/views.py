# 3rd party imports
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

# Local imports
from . import auth
from .forms import LoginForm
from .. import db
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Handle requests to the /login route
    Log an admin through the login form"""

    form = LoginForm()
    if form.validate_on_submit():
        # Check if an admin exists in the database
        # The password entered matches the password in the db
        admin = User.query.filter_by(email=form.email.data).first()
        if admin is not None and admin.verify_password(
                form.password.data):
            login_user(admin)

            # redirect to the proper dashboard
            return redirect(url_for('home.admin_home'))

        else:
            flash('Invalid email and password')

    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
def logout():
    """Handle requests for the /logout route
    Log an employee out through the logout link"""

    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))
