from flask import Blueprint,render_template
from database import Clientes

users = Blueprint('users', __name__)

@users.route('/users')
def list_users():
    return render_template("users.html")
@users.route('/users/<id>')
def show_user():
    pass
@users.route('/users/edit/<id>')
def edit_user():
    pass
@users.route('/users/delete/<id>')
def delete_user():
    pass