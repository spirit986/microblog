from flask import render_template, flash, redirect, url_for
from app import app_microblog
from app.forms import LoginForm

@app_microblog.route('/')
@app_microblog.route('/index')
def index():
    user_details = {
        'fname': 'Tom',
        'lname': 'Spirit',
        'username': 'spirit.986'
    }

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

    return render_template('index.html', title='Tom Spirit\'s', user=user_details, posts=user_posts)


@app_microblog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)


