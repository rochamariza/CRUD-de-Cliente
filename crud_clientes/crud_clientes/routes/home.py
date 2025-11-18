from flask import Blueprint,render_template
from database import Clientes

home = Blueprint('home', __name__)

@home.route('/')
def show_home():
    return render_template("home.html", clientes=Clientes)
