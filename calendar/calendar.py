from flask import Blueprint, render_template, request, session
from ..helpers import login_required
from ..query_helpers import get_username, get_dates, get_trade_percs
from ..config import Config

calendar_blueprint = Blueprint("calendar_blueprint", __name__, static_folder="static", template_folder="templates")

pairs_list = Config.PAIRS_LIST
directions = Config.DIRECTIONS
outcomes = Config.OUTCOMES
strategies = Config.STRATEGIES
entry_types = Config.ENTRY_TYPES
sessions = Config.SESSIONS
trends = Config.TRENDS
days = Config.DAYS
reasons = Config.REASONS

@calendar_blueprint.route("/calendar", methods=["GET", "POST"])
@login_required
def calendar():
    user_id=session.get("user_id")
    username=get_username(user_id)

    days_count = 0
    if request.method == "POST":
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        date = {
            "year": int(request.form.get("year")),
            "month": months[int(request.form.get("month")) - 1]
        }
        trades=[]
        #dAILY DATA ARRAY
        daily_data = []

        #FIND AMOUNT OF DAYS BASED ON MONTH CHOSEN
        if int(request.form.get("month")) == 1 or int(request.form.get("month")) == 3 or int(request.form.get("month")) == int(5 or request.form.get("month")) == 7 or int(request.form.get("month")) == 8 or int(request.form.get("month")) == 10 or int(request.form.get("month")) == 12:
            days_count = 31
        elif int(request.form.get("month")) == 4 or int(request.form.get("month")) == 6 or int(request.form.get("month")) == 9 or int(request.form.get("month")) == 11:
            days_count = 30
        else:
            days_count = 28

        #PULL TRADE DATE FROM DB
        trade_dates = get_dates(user_id)
        
        #FIND ALL TRADES IN SELECTED MONTH AND YEAR
        for trade in trade_dates:
            if int(trade["date_close"].split("-")[0]) == date["year"] and int(trade["date_close"].split("-")[1]) == int(request.form.get("month")):
                trades.append(trade)

        #FIND $ CHANGE BY DAY
        for day in range(days_count):
            dollars = 0
            trade_count = 0
            for trade in trades:
                if (int(trade["date_close"].split("-")[2]) == day + 1):
                    dollars = dollars + float(trade["dollar_amount"])
                    trade_count = trade_count + 1
            daily_data.append({
                "day": day + 1,
                "dollar_change": round(dollars, 2),
                "trade_count": trade_count
            })

        #PULL TRADE % CHANGE FROM DB
        filters = { "date": 1, "trade_id": 1, "percent_change": 1, "dollar_amount_before_trade": 1, "dollar_amount_after_trade": 1}

        trade_percentages = get_trade_percs(user_id, filters)

        #FIND ALL TRADES IN SELECTED MONTH AND YEAR
        percentages=[]
        for trade in trade_percentages:
            if int(trade["date"].split("-")[0]) == date["year"] and int(trade["date"].split("-")[1]) == int(request.form.get("month")):
                percentages.append(trade)

        #SEPARATE $ CHANGE BY DAY
        for day in range(days_count):
            total_percentage=0
            for trade in percentages:
                if (int(trade["date"].split("-")[2]) == day + 1):
                    total_percentage = total_percentage + float(trade["percent_change"])
            daily_data[day]["total_percentage"] = round(total_percentage,2)

        return render_template("calendar.html", user_id=user_id, date=date, days=days_count, daily_data=daily_data, username=username)
