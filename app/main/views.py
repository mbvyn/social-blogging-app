from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import NameForm
from .. import db
from ..email import send_email
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['SB_ADMIN']:
                send_email(current_app.config['SB_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@main.route('/user/<int:id>')
def user_id(id):
    return '<h1>Hello, user your id is %s!</h1>' % id
