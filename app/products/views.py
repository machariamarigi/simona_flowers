# 3rd party imports
from flask import render_template

# Local imports
from . import products
from ..models import Products, Category


@products.route('/products/all')
def all_products():
    """List all products"""

    products = Products.query.all()

    return render_template(
        'products/products.html',
        products=products,
        title='all products'
    )


@products.route('/products/<category>')
def products_by_category(category):
    """List products by categories they fall under"""

    product_category = Category.query.filter_by(name=category).first()
    products = Products.query.filter_by(category_id=product_category.id)
    title = '{} products'.format(category)

    return render_template(
        'products/products.html',
        products=products,
        title=title
    )

