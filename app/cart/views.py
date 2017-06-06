from flask import session, render_template, redirect, flash

from . import cart
from ..models import Products


@cart.route('/cart')
def shopping_cart():
    """Display contents in a shopping cart"""

    if "cart" not in session:
        flash("Nothing in the cart")
        return render_template('cart.html', display_cart={}, total=0)
    else:
        items = session["cart"]
        dict_of_products = {}
        total_price = 0

        for item in items:
            product = Products.query.get_or_404(item)
            total_price += product.price
            if product.id in dict_of_products:
                dict_of_products[product.id]["qty"] += 1
            else:
                dict_of_products[product.id] = {
                    "qty": 1,
                    "name": product.name,
                    "price": product.price}

        return render_template(
            "cart.html",
            display_cart=dict_of_products,
            title="cart",
            total=total_price)


@cart.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(id)

    flash("Succesfully added to cart")
    return redirect("/cart")
