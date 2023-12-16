from flask import Blueprint, render_template, request, redirect, url_for, session
from ..query_helpers import get_trade, get_username, get_dollar_amount, get_user_balance
from ..helpers import login_required, percent_change, risk_reward
from ..query_helpers import update_trade, update_change, update_user

edited_blueprint = Blueprint("edited_blueprint", __name__, static_folder="static", template_folder="templates")

@edited_blueprint.route("/edited", methods=["GET", "POST"])
@login_required
def edited():
    user_id=session.get("user_id")

    if request.method == "POST":
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
            "trade_id": request.form.get("trade_id")
        }

        #CHANGE BALANCE
        old_trade_amount = get_dollar_amount(form_data["trade_id"])
        current_balance = get_user_balance(user_id)
        reset_balance = float(current_balance) - float(old_trade_amount)
        new_balance = round(reset_balance,2) + float(form_data["dollar_amount"])
        user_data = {"dollar_amount": round(new_balance,2)}
        update_user(user_id, user_data)

        #CHANGE ACCOUNT CHANGE DB
        percent_value = percent_change(new_balance, reset_balance)

        change_data = {"dollar_amount_before_trade": reset_balance, "dollar_amount_after_trade": new_balance, "percent_change": round(percent_value, 2), "date": form_data["date_close"]}
        update_change(form_data["trade_id"], change_data)
        rrr = risk_reward(form_data['enter_price'], form_data['stop_loss'], form_data['take_profit'])

        #UPDATE JOURNAL ENTRY DB
        data = {"date_open": form_data["date_open"], "date_close": form_data["date_close"], "time_open": form_data["time_open"], "pair": form_data["pair"], "pos_size": form_data["pos_size"], "direction": form_data["direction"], "enter_price": form_data["enter_price"], "stop_loss": form_data["stop_loss"], "take_profit": form_data["take_profit"], "exit_price": form_data["exit_price"], "win_loss": form_data["win_loss"], "dollar_amount": form_data["dollar_amount"], "strategy": form_data["strategy"], "entry_type": form_data["entry_type"], "session_entry": form_data["session_entry"], "session_exit": form_data["session_exit"], "trend": form_data["trend"], "day": form_data["day"], "reason": form_data["reason"], "rrr": rrr, "trade_id": form_data["trade_id"]}

        update_trade(form_data["trade_id"], data)
        return redirect(url_for("journal_blueprint.journal"))