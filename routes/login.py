from flask import Blueprint, render_template

login_route = Blueprint('login', __name__)

@login_route.route('/login', methods=['GET', 'POST'])
def login(username, password):
    return render_template('login.html')

@login_route.route('/signin', methods=['POST'])
def signin():
    return render_template('signin.html')
