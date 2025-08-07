from flask import Blueprint, render_template

profile_route = Blueprint('profile', __name__)

@profile_route.route('/profile')
def profile():
    return render_template('profile.html')

@profile_route.route('/profile', methods=['POST'])
def editar_profile():
    pass
