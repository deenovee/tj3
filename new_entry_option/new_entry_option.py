from flask import Blueprint, render_template, request, session
from ..query_helpers import get_username
from ..helpers import login_required

new_entry_option_blueprint = Blueprint("new_entry_option_blueprint", __name__, static_folder="static", template_folder="templates")

@new_entry_option_blueprint.route("/new-entry-option", methods=["GET", "POST"])
@login_required
def new_entry_option():
    user_id=session.get("user_id")
    username=get_username(user_id)

    if request.method == "GET":
        return render_template("new-entry-option.html", username=username, user_id=user_id)

    else:
        if request.form.get("csv"):
            return render_template("new-entry-csv.html")