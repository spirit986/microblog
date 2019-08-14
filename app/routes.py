from flask import render_template, flash, redirect, url_for, request
from app import app_microblog, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app_microblog.route('/')
@app_microblog.route('/index')
@login_required
def index():

    user_posts = [
        {
            'author': {'username': 'spirit.986'},
            'title': 'Lorem Ipsum',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        },
        {
            'author': {'username': 'the_renegade'},
            'title': 'Bacon Ipsum',
            'body': 'Bacon ipsum dolor amet short ribs beef ribs boudin bacon, biltong short loin pig spare ribs drumstick meatball hamburger frankfurter jerky buffalo. Flank short ribs leberkas cow doner shoulder, tail boudin ham salami andouille. Shank pork chop biltong brisket, cow bresaola turkey alcatra tongue venison buffalo chuck. Alcatra ball tip ground round cow picanha, burgdoggen pork loin jowl strip steak.'
        },
        {
            'author': {'username': 'Lorem_master'},
            'title': 'Bacon Ipsum with meat',
            'body': 'T-bone picanha shank tri-tip ball tip landjaeger jowl rump leberkas ground round ribeye pig shankle pastrami pork loin. Tenderloin pork meatloaf bacon, frankfurter flank boudin ball tip salami shankle capicola pastrami pancetta. Alcatra pancetta jowl hamburger, chicken meatloaf andouille tail pork bresaola. Venison fatback ribeye ham hock flank.'
        },
        {
            'author': {'username': 'void'},
            'title': 'Spicy Bacon Ipsum with meat and filler',
            'body': 'Spicy jalapeno bacon ipsum dolor amet eu irure pork loin esse nostrud pork biltong sed lorem culpa aliquip corned beef. Beef ribs swine meatball turkey shankle pastrami proident. Esse jerky do occaecat consectetur. Prosciutto capicola lorem, esse pig buffalo short ribs jowl. Commodo in landjaeger, kielbasa dolor prosciutto alcatra bresaola ad ham pork loin strip steak short ribs swine. Bacon ut drumstick esse jerky qui sed anim do prosciutto t-bone strip steak meatloaf.'
        }
    ]

    return render_template('index.html', title='Tom Spirit\'s', posts=user_posts)


@app_microblog.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app_microblog.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app_microblog.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

