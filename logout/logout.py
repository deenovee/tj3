from flask import Blueprint, session, redirect

logout_blueprint = Blueprint('logout_blueprint', __name__, template_folder='templates', static_folder='static')

@logout_blueprint.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")