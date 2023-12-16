from flask import Blueprint, render_template, request, session, redirect, url_for
from ..query_helpers import get_journal_entries, get_username, get_user_balance, update_user, insert_journal, add_change
from ..helpers import login_required, percent_change, risk_reward, exists
from ..config import Config
import random

pairs_list = Config.PAIRS_LIST

new_entry_blueprint = Blueprint("new_entry_blueprint", __name__, static_folder="static", template_folder="templates")

@new_entry_blueprint.route("/new-entry", methods=["GET", "POST"])
@login_required
def new_entry():
    user_id=session.get("user_id")
    journal_entries_list = get_journal_entries(user_id)
    username=get_username(user_id)
    
    if request.method == "GET":
        return render_template("new-entry-2.html", user_id=user_id, pairs=pairs_list, username=username, journal_data=journal_entries_list)
    else:
        #COLLECT JOURNAL ENTRY DATAn
        form_data = {
            "date_open": request.form.get("date_open"),
            "date_close": request.form.get("date_close"),
            "time_open": request.form.get("time_open"),
            "pair": request.form.get("pair_selection"),
            "pos_size": request.form.get("pos_size"),
            "direction": request.form.get("direction"),
            "enter_price": request.form.get("enter_price"),
            "stop_loss": request.form.get("stop_loss"),
            "take_profit": request.form.get("take_profit"),
            "exit_price": request.form.get("exit_price"),
            "win_loss": request.form.get("win_loss"),
            "dollar_amount": request.form.get("dollar_amount"),
            "strategy": request.form.get("strategy"),
            "entry_type": request.form.get("entry_type"),
            "session_entry": request.form.get("session_entry"),
            "session_exit": request.form.get("session_exit"),
            "trend": request.form.get("trend"),
            "day": request.form.get("day"),
            "reason": request.form.get("reason_for_loss"),
            "user_id":user_id
        }

        #FUNCTION TO CREATE TRADE ID
        while True:
            trade_id = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            if not exists(trade_id, journal_entries_list):
                break

        #PULL OLD AND NEW BALANCE
        old_balance = get_user_balance(user_id)
        new_balance = round(float(old_balance) + float(form_data["dollar_amount"]),2)

        #FIND PERCENT CHANGE
        percent_value = percent_change(new_balance, old_balance)
        change_data = {"trade_id": trade_id, "dollar_amount_before_trade": old_balance, "dollar_amount_after_trade": new_balance, "user_id": user_id, "date": form_data["date_close"], "percent_change": percent_value}
        add_change(change_data)
        
        #CHANGE ACCOUNT BALANCE
        user_data = {"dollar_amount": new_balance}
        update_user(user_id, user_data)
        rrr = risk_reward(form_data['enter_price'], form_data['stop_loss'], form_data['take_profit'])

        #INSERT JOURNAL ENTRY INTO DB
        data = {
            "trade_id": trade_id, 
            "date_open": form_data["date_open"], 
            "date_close": form_data["date_close"], 
            "time_open": form_data["time_open"], 
            "pair": form_data["pair"], 
            "pos_size": form_data["pos_size"], 
            "direction": form_data["direction"], 
            "enter_price": form_data["enter_price"], 
            "stop_loss": form_data["stop_loss"], 
            "take_profit": form_data["take_profit"], 
            "exit_price": form_data["exit_price"], 
            "win_loss": form_data["win_loss"], 
            "dollar_amount": form_data["dollar_amount"], 
            "strategy": form_data["strategy"], 
            "entry_type": form_data["entry_type"], 
            "session_entry": form_data["session_entry"], 
            "session_exit": form_data["session_exit"], 
            "trend": form_data["trend"], 
            "day": form_data["day"], 
            "reason_for_loss": form_data["reason"], 
            "user_id": user_id, 
            "rrr": rrr
        }
        insert_journal(data)

        return redirect(url_for("journal_blueprint.journal"))