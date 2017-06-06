# 3rd party imports
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

# Local imports
from . import admin
from .forms import ProductForm, CategoryForm, EventServiceForm
from .. import db
from ..models import User, Products, Category, EventService
from ..tools import s3_upload, s3_delete


def check_admin():
    """Prevent non admins from accesing the page"""
    if not current_user.is_admin:
        abort(403)


@admin.route('/admin-products', methods=['GET', 'POST'])
@login_required
def list_products():
    """List all products"""

    check_admin()
    products = Products.query.all()

    return render_template(
        'admin/products/products.html', products=products, title='Products')


@admin.route('/admin-products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    """Add a product to the database"""

    check_admin()
    add_product = True

    form = ProductForm()
    if form.validate_on_submit():
        product = Products(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            stock=form.stock.data,
            category=form.category.data,
            image=s3_upload(form.image)
        )

        try:
            # add product to database
            db.session.add(product)
            db.session.commit()
            flash('You have succesfully added a Product')
        except:
            flash('Error: Product already exists')

        return redirect(url_for('admin.list_products'))

    return render_template('admin/products/product.html', action="Add",
                           add_product=add_product, form=form,
                           title="Add Product")


@admin.route('/admin-products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    """Edit a product"""

    check_admin()
    add_product = False

    product = Products.query.get_or_404(id)
    product_image = product.image
    form = ProductForm(obj=Products)
    if form.validate_on_submit():
        s3_delete(product_image)
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.category = form.category.data
        product.image = s3_upload(form.image)
        db.session.commit()
        flash('You have succesfully edited the product')

        return redirect(url_for('admin.list_products'))

    form.category.data = product.category
    form.stock.data = product.stock
    form.price.data = product.price
    form.description.data = product.description
    form.name.data = product.name
    return render_template('admin/products/product.html', action="Edit",
                           add_product=add_product, form=form,
                           product=product, title="Edit Product")


@admin.route('/admin-products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    """Delete a products from the database"""

    check_admin()

    product = Products.query.get_or_404(id)
    product_image = product.image
    s3_delete(product_image)
    db.session.delete(product)
    db.session.commit()
    flash('You have successfully deleted the product')

    return redirect(url_for('admin.list_products'))

    return render_template(title="Delete Product")


@admin.route('/admin-categories', methods=['GET', 'POST'])
@login_required
def list_categories():
    """List all categories"""

    check_admin()
    categories = Category.query.all()

    return render_template(
        'admin/categories/categories.html',
        categories=categories,
        title='Categories'
        )


@admin.route('/admin-categories/add', methods=['GET', 'POST'])
@login_required
def add_category():
    """Add a Category to the database"""

    check_admin()
    add_category = True

    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data,
                            description=form.description.data,
                            image=s3_upload(form.image,
                                            upload_dir='categories/'))

        try:
            # add category to database
            db.session.add(category)
            db.session.commit()
            flash('You have succesfully added a category')
        except:
            flash('Error: category already exists')

        return redirect(url_for('admin.list_categories'))

    return render_template('admin/categories/category.html', action="Add",
                           add_category=add_category, form=form,
                           title="Add Category")


@admin.route('/admin-categories/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    """Edit a category"""

    check_admin()
    add_category = False

    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=Category)
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        category.image = s3_upload(form.image, upload_dir='categories/')
        db.session.commit()
        flash('You have succesfully edited the category')

        return redirect(url_for('admin.list_categories'))

    form.description.data = category.description
    form.name.data = category.name
    return render_template('admin/categories/category.html', action="Edit",
                           add_category=add_category, form=form,
                           category=category, title="Edit Category")


@admin.route('/admin-categories/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    """Delete a category from the database"""

    check_admin()

    category = Category.query.get_or_404(id)
    category_image = category.image
    s3_delete(product_image, upload_dir='categories/')
    db.session.delete(category)
    db.session.commit()
    flash('You have successfully deleted the category')

    return redirect(url_for('admin.list_categories'))

    return render_template(title="Delete Category")


@admin.route('/admin_events_services', methods=['GET', 'POST'])
@login_required
def list_events_services():
    """List all events and services"""

    check_admin()
    events_services = EventService.query.all()

    return render_template(
        'admin/events_services/events_services.html',
        events_services=events_services,
        title='Events And Services'
        )


@admin.route('/admin_events_services/add', methods=['GET', 'POST'])
@login_required
def add_event_service():
    """Add an event or service to the database"""

    check_admin()
    add_event_service = True

    form = EventServiceForm()
    if form.validate_on_submit():
        event_service = EventService(
            name=form.name.data,
            description=form.description.data,
            image=s3_upload(form.image, upload_dir='events_services/'))

        try:
            # add category to database
            db.session.add(event_service)
            db.session.commit()
            flash('You have succesfully added an event on service')
        except:
            flash('Error: event or service already exists')

        return redirect(url_for('admin.list_events_services'))

    return render_template(
        'admin/events_services/event_service.html',
        action="Add",
        add_event_service=add_event_service, form=form,
        title="Add Event or Services")


@admin.route('/admin_events_services/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_event_service(id):
    """Edit an event or service"""

    check_admin()
    add_event_service = False

    event_service = EventService.query.get_or_404(id)
    event_service_image = event_service.image
    s3_delete(event_service_image, upload_dir='events_services/')
    form = EventServiceForm(obj=EventService)
    if form.validate_on_submit():
        event_service.name = form.name.data
        event_service.description = form.description.data
        event_service.image = s3_upload(
            form.image, upload_dir='events_services/')
        db.session.commit()
        flash('You have succesfully edited the event or sevice')

        return redirect(url_for('admin.list_events_services'))

    form.description.data = event_service.description
    form.name.data = event_service.name
    return render_template(
        'admin/events_services/event_service.html',
        action="Edit",
        add_event_service=add_event_service, form=form,
        event_service=event_service, title="Edit Event or Service")


@admin.route('/admin_events_services/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_event_service(id):
    """Delete an event or service from the database"""

    check_admin()

    event_service = EventService.query.get_or_404(id)
    event_service_image = event_service.image
    s3_delete(event_service_image, upload_dir='events_services/')
    db.session.delete(event_service)
    db.session.commit()
    flash('You have successfully deleted the event or service')

    return redirect(url_for('admin.list_events_services'))

    return render_template(title="Delete Events or Service")
