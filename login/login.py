from flask import Blueprint, request, session, redirect, render_template
from werkzeug.security import check_password_hash
from ..helpers import apology
from ..query_helpers import find_user

login_blueprint = Blueprint('login_blueprint', __name__, template_folder='templates', static_folder='static')

@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    #Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Please enter a valid username", 404)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please enter a valid password", 404)
        # Query database for username
        user = find_user(request.form.get("username"))
        # Ensure username exists and password is correct
        if not user or not check_password_hash(user["hash"], request.form.get("password")):
            return apology("Account not found", 404)
        # Remember which user has logged in
        session["user_id"] = user["user_id"]
        # Redirect user to home page
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")