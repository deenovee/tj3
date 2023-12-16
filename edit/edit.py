from flask import Blueprint, render_template, request, session
from ..query_helpers import get_trade, get_username
from ..helpers import login_required
from ..config import Config

edit_blueprint = Blueprint("edit_blueprint", __name__, static_folder="static", template_folder="templates")

pairs_list = Config.PAIRS_LIST
directions = Config.DIRECTIONS
outcomes = Config.OUTCOMES
strategies = Config.STRATEGIES
entry_types = Config.ENTRY_TYPES
sessions = Config.SESSIONS
trends = Config.TRENDS
days = Config.DAYS
reasons = Config.REASONS

@edit_blueprint.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    user_id=session.get("user_id")
    username=get_username(user_id)
    select_values = {
        "pairs": pairs_list,
        "directions": directions,
        "outcomes": outcomes,
        "strategies": strategies,
        "entry_types": entry_types,
        "sessions": sessions,
        "trends": trends,
        "days": days,
        "reasons": reasons
    }

    if request.method == "POST":
        data=request.form.get("edit")
        entry_data = get_trade(data)
        return render_template("edit.html", data=entry_data, user_id=user_id, select_values=select_values, username=username)