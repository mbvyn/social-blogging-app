from flask import render_template, session, redirect, url_for, current_app
from flask_login import login_required
from . import main
from .forms import NameForm
from .. import db
from ..email import send_email
from ..models import User


@main.route('/')
def index():
    return render_template('index.html')
