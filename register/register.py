from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import generate_password_hash
from ..helpers import apology
from ..query_helpers import check_user, create_user

register_bp = Blueprint('register_bp', __name__, template_folder='templates', static_folder='static')

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        p1 = request.form.get("p1")
        p2 = request.form.get("p2")
        hashed_password = generate_password_hash(p1)
        dollar_amount = request.form.get("dollar_amount")
        if not username:
            return apology("Please enter a valid username", 404)
        elif p1 != p2 or not p1 or not p2:
            return apology("Please enter a valid password", 404)
        elif not dollar_amount:
            return apology("Please enter a valid account balance", 404)
        elif check_user(username):
            return redirect("/login")
        else:
            create_user(username, hashed_password, int(dollar_amount))
            return redirect("/login")

    if request.method == "GET":
            return render_template("register.html", user_id=0)
    return apology("Something went wrong", 600)