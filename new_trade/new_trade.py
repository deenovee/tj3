from flask import Blueprint, render_template, request, session
from ..query_helpers import get_journal_entries, get_username
from ..helpers import login_required
from ..config import Config

new_trade_blueprint = Blueprint("new_trade_blueprint", __name__, static_folder="static", template_folder="templates")

pairs_list = Config.PAIRS_LIST

@new_trade_blueprint.route("/new-trade", methods=["GET", "POST"])
@login_required
def new_trade():
    user_id=session.get("user_id")
    journal_entries_list = get_journal_entries(user_id)
    username=get_username(user_id)

    if request.method == "GET":
        return render_template("new-entry.html", user_id=user_id, pairs=pairs_list, username=username, journal_data=journal_entries_list)