from flask import Blueprint, render_template, session, request, redirect, url_for
from ..query_helpers import get_journal_entries, get_username, get_user_balance, add_change, update_user, insert_journal
from ..helpers import percent_change, risk_reward
from ..csv_helpers import find_session
from ..config import Config
import csv
import tempfile
import os
import random
import string


csv_input_blueprint = Blueprint('csv_input_blueprint', __name__, template_folder='templates', static_folder='static')

@csv_input_blueprint.route("/csv_input", methods=["GET", "POST"])
def csv_input():
    if request.method == "POST":
        user_id=session.get("user_id")
        journal_entries_list = get_journal_entries(user_id)
        username=get_username(user_id)
        file = request.files['csv-file']
        if file:
            _, temp_path = tempfile.mkstemp()
            file.save(temp_path)
            with open(temp_path, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["Order Type"] == "BALANCE":
                        date_open = row['Opened At'][0:10].strip()
                        amount = 1
                        if row["Profit/Balance"][0] != "-":
                            amount = row["Profit/Balance"][1:]
                        
                        else:
                            amount = "-" + row["Profit/Balance"][2:] 
                          
                        while True:
                            letters = string.ascii_uppercase
                            random_string = ''.join(random.choice(letters) for i in range(6))
                            if not exists(random_string, journal_entries_list):
                                break
                        trade_id = random_string
                        old_balance = get_user_balance(user_id)
                        new_balance = round(float(old_balance) + float(amount), 2)
                        percent_value = percent_change(new_balance, old_balance)
                        change_data = {"trade_id": trade_id, "dollar_amount_before_trade": old_balance, "dollar_amount_after_trade": new_balance, "user_id": user_id, "date": date_open, "percent_change": percent_value}
                        add_change(change_data)
                        user_data = {"dollar_amount": new_balance}
                        update_user(user_id, user_data)
                        data = {
                            "user_id": user_id,
                            "trade_id": trade_id, 
                            "date_open": date_open,
                            "date_close": date_open,
                            "dollar_amount": amount,
                            "rrr":1
                        }
                        insert_journal(data)
                        continue
                    elif row["Order Type"] == "BUY" or row["Order Type"] == "SELL":
                        pair = row["Symbol"].replace("/", "_")
                        if row['Comment'] == "cancelled" or row['Profit/Balance'] == "No Profit" or row['Comment'][0:5] == "rebate":
                            continue
                        trade_id = ""
                        while True:
                            trade_id = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
                            if not exists(trade_id, journal_entries_list):
                                break

                        
                        date_open = row['Opened At'][0:10].strip()
                        date_close = row['Closed At'][0:10].strip()
                        time_open = row['Opened At'][10:18]
                        time_close = row['Closed At'][10:18]
                        session_entry = find_session(time_open)
                        session_exit = find_session(time_close)

                        direction = ""
                        if row['Order Type'] == "BUY":
                            direction = "Long"
                        else: direction = "Short"

                        dollar_amount=1

                        if row["Profit/Balance"][0] != "-":
                            dollar_amount = row["Profit/Balance"][1:]
                            if float(row["Profit/Balance"][1:]) > 0:
                                w_l = "Win"
                            
                        else:
                            dollar_amount = "-" + row["Profit/Balance"][2:]
                            if float(row["Profit/Balance"][2:]) > 0:
                                w_l = "Loss"

                        rrr=1
                        if float(row['S/L']) != 0:
                            if float(row['T/P']) != 0:
                                rrr = risk_reward(round(float(row['Open Price']), 2), round(float(row['S/L']),2), round(float(row['T/P']),2))
                        else: rrr = 1


                        old_balance = get_user_balance(user_id)
                        new_balance = round(float(old_balance) + float(dollar_amount), 2)
                        percent_value = percent_change(new_balance, old_balance)
                        change_data = {"trade_id": trade_id, "dollar_amount_before_trade": old_balance, "dollar_amount_after_trade": new_balance, "user_id": user_id, "date": date_open, "percent_change": percent_value}
                        add_change(change_data)
                        
                        user_data = {"dollar_amount": new_balance}
                        update_user(user_id, user_data)

                        data = {
                            "trade_id": trade_id, 
                            "date_open": date_open, 
                            "date_close": date_close, 
                            "time_open": time_open, 
                            "pair": pair, 
                            "pos_size": row["Volume"], 
                            "direction": direction, 
                            "enter_price": row["Open Price"], 
                            "stop_loss": row["S/L"], 
                            "take_profit": row["T/P"], 
                            "exit_price": row["Close Price"], 
                            "win_loss": w_l, 
                            "dollar_amount": dollar_amount,
                            "strategy": "",
                            "entry_type": "",
                            "session_entry": session_entry,
                            "session_exit": session_exit,
                            "trend": "",
                            "day": "", 
                            "user_id": user_id, 
                            "rrr": int(rrr)
                        }
                        insert_journal(data)
                        continue
                os.remove(temp_path)
            return redirect(url_for("journal"))
        else:
            
            return render_template("new-entry-option.html", username=username, user_id=user_id)
