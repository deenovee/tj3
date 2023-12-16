from flask import Blueprint, render_template, request, redirect, url_for, session
from ..query_helpers import get_journal_entries, get_account_changes, get_username
from ..config import Config
from ..helpers import login_required
from ..functions.days import day
from ..functions.entry_types import entry_type
from ..functions.sessions import session_entry, session_exit
from ..functions.reasons import reason_for_loss
from ..functions.pairs import pairs
from ..functions.directions import direction
from ..functions.trends import trend
from ..functions.strategies import strategy

tables_blueprint = Blueprint("tables_blueprint", __name__, static_folder="static", template_folder="templates")

pairs_list = Config.PAIRS_LIST
directions = Config.DIRECTIONS
outcomes = Config.OUTCOMES
strategies = Config.STRATEGIES
entry_types = Config.ENTRY_TYPES
sessions = Config.SESSIONS
trends = Config.TRENDS
days = Config.DAYS
reasons = Config.REASONS


@tables_blueprint.route("/tables", methods=["GET", "POST"])
@login_required
def tables():
    user_id=session.get("user_id")
    username=get_username(user_id)

    if request.method == "GET":
        return render_template("tables.html", user_id=user_id, table="")
    
    else:

        table = request.form.get("table_choice")
        journal_entries_list = get_journal_entries(user_id)
        account_change_list = get_account_changes(user_id)
        #SESSION ENTRY TABLE
        if table == "Session Entry":
            session_data, graphJSON, header = session_entry(journal_entries_list, account_change_list)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=session_data, graphJSON=graphJSON, header=header)

        #SESSION EXIT TABLE
        elif table == "Session Exit":
            session_data, graphJSON, header = session_exit(journal_entries_list, account_change_list)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=session_data, graphJSON=graphJSON, header=header)

        #REASON FOR LOSS TABLE
        elif table == "Reason For Loss":
            reason_data, graphJSON, header = reason_for_loss(journal_entries_list, account_change_list, reasons)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=reason_data, graphJSON=graphJSON, header=header)

        elif table == "Pairs":
            pair_data, graphJSON, header = pairs(journal_entries_list, account_change_list, pairs_list)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=pair_data, graphJSON=graphJSON, header=header)

        elif table == "Direction":
            direction_data, graphJSON, header = direction(journal_entries_list, account_change_list, directions)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=direction_data, graphJSON=graphJSON, header=header)

        elif table == "Trend":
            trend_data, graphJSON, header = trend(journal_entries_list, account_change_list)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=trend_data, graphJSON=graphJSON, header=header)

        elif table == "Strategy":
            strategy_data, graphJSON, header = strategy(journal_entries_list, account_change_list, strategies)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=strategy_data, graphJSON=graphJSON, header=header)

        elif table == "Day":
            day_data, graphJSON, header = day(journal_entries_list, account_change_list, days)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=day_data, graphJSON=graphJSON, header=header)

        elif table == "Entry Type":
            entry_type_data, graphJSON, header = entry_type(journal_entries_list, account_change_list)
            return render_template("tables.html", user_id=user_id, table=table, username=username, data=entry_type_data, graphJSON=graphJSON, header=header)

        return redirect(url_for("journal_blueprint.journal"))
