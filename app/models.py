# 3rd Party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """Create users db table"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    phone_number = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('You cannot access password')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User({})'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Products(db.Model):
    """Create a products db table"""

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.Integer, index=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200), index=True)
    stock = db.Column(db.Integer, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return 'Product({})'.format(self.name)


class Category(db.Model):
    """Create a categories db table"""

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200), index=True)
    products = db.relationship('Products', backref='category',
                               lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.name)


class EventService(db.Model):
    """Create a events_services db table"""

    __tablename__ = 'events_services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200), index=True)

    def __repr__(self):
        return '{}'.format(self.name)

