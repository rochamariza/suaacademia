from flask import Blueprint, render_template

profile_route = Blueprint('profile', __name__)

@sobre_route.route('/profile')
def profile():
    return render_template('profile.html')