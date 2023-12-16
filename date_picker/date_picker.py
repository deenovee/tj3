from flask import Blueprint, render_template, session
from ..helpers import login_required
from ..query_helpers import get_username

date_picker_blueprint = Blueprint("date_picker_blueprint", __name__, static_folder="static", template_folder="templates")

@date_picker_blueprint.route("/date-picker")
@login_required
def date_picker():
    user_id=session.get("user_id")
    username=get_username(user_id)
    return render_template("date-picker.html", user_id=user_id, username=username)