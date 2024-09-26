'''
running web app:

set FLASK_APP=hello.py
flask --app hello.py run
'''

from datetime import datetime, timezone
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class IndexForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/',methods=['GET','POST'])
def index():
    form = IndexForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!', 'warning')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!', 'info')
        
        session.permanent = False
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    
    return render_template('index.html', current_time=datetime.now(timezone.utc), form=form, name=session.get('name'), email=session.get('email'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.now(timezone.utc))


@app.route('/clear')
def clear():
    session.pop('name', None)
    session.pop('email', None)
    flash('Session cleared. Name and email reset to Stranger.', 'info')
    return redirect(url_for('index'))


# error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
