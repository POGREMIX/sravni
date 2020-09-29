from flask import Blueprint, redirect, url_for, flash
from flask import render_template


from forms import ContactForm
from werkzeug.datastructures import MultiDict

user_route = Blueprint('user_route', __name__)


@user_route.route('/user/<int:user_id>/')
def user(user_id):
    return render_template('user.html', user_id=user_id)


@user_route.route('/user/auth/', methods=['get', 'post'])
def auth():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        # здесь логика базы данных
        print("\nData received. Now redirecting ...")
        flash("Message Received", "success")
        return redirect(url_for('index_route.index'))
    return render_template('login.html', form=form)
