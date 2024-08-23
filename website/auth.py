from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', method=['GET', 'POST'])
def login():
    return render_template("login.html")



@auth.route('/logout')
def logout():
    return "<p>Logout</p>"



@auth.route('/sign-up', method=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    return render_template("sign_up.html")