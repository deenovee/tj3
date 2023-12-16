from flask import Blueprint, render_template, session
from ..query_helpers import get_username
from ..helpers import login_required

home_blueprint = Blueprint('home_blueprint', __name__, template_folder='templates', static_folder='static')

@home_blueprint.route("/")
@login_required
def home():
    user_id=session.get("user_id")
    username=get_username(user_id)
    return render_template("index.html", user_id=user_id, username=username)