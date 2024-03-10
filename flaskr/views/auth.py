import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from models import storage
from flaskr.views import app_views
from models.user import User
from hashlib import md5


bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        first_name = request.form['name']
        email = request.form['email']
        password= request.form['password']
        # password = generate_password_hash(passw)
        # db = get_db()
        error = None

        if not first_name:
            error = 'name is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                data = {"first_name": first_name, "email": email, "password": password}
                instance = User(**data)
                instance.save()
            except:
                error = f"Email {email} is already registered."
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        error = None
        user = storage.get_email(email)
        user_passw = user.password
        passw = md5(password.encode()).hexdigest()
        if user is  None:
            error = 'Incorrect email.'
        # elif not check_password_hash(user.password, password):
        elif user_passw != passw:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect('/')

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = storage.get(User, user_id)



@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('app_views.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view