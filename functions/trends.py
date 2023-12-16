import json
import pandas as pd
import plotly
import plotly.express as px


def trend(journal_entries_list, account_change_list):

    # Prepare a list to store the data for each trade
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "trend" in journal_entry and journal_entry["trend"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "trend": journal_entry["trend"], "percent_change": account_change["percent_change"]})
                else: continue

    
    #CALCULATE % CHANGE BY PRO/COUNTER TREND
    pro_pos = 0
    pro_neg = 0
    counter_pos = 0
    counter_neg = 0
    for trade in trade_data:
        if trade["direction"] == "Long" and trade["trend"] == "Up":

            if trade["percent_change"] > 0:
                pro_pos = pro_pos + trade["percent_change"]
            else:
                pro_neg = pro_neg + trade["percent_change"]

        if trade["direction"] == "Short" and trade["trend"] == "Down":

            if trade["percent_change"] > 0:
                pro_pos = pro_pos + trade["percent_change"]
            else:
                pro_neg = pro_neg + trade["percent_change"]

        if trade["direction"] == "Short" and trade["trend"] == "Up":

            if trade["percent_change"] > 0:
                counter_pos = counter_pos + trade["percent_change"]
            else:
                counter_neg = counter_neg + trade["percent_change"]

        if trade["direction"] == "Long" and trade["trend"] == "Down":

            if trade["percent_change"] > 0:
                counter_pos = counter_pos + trade["percent_change"]
            else:
                counter_neg = counter_neg + trade["percent_change"]

    trend_data = {
        "Pro_Pos": round(pro_pos,2),
        "Pro_Neg": round(pro_neg,2),
        "Counter_Pos": round(counter_pos,2),
        "Counter_Neg": round(counter_neg,2)
    }

    positives =[]
    negatives = []
    for data in trend_data:
        if data[-3:] == "Pos":
            positives.append(trend_data[data])
        else:
            negatives.append(trend_data[data])
    fixed = positives + negatives
    df = pd.DataFrame({
        "Trend": ["Pro", "Counter", "Pro", "Counter"],
        "Percentage": fixed,
        "Pos/Neg": ["+", "+", "-", "-"]
        })

    fig = px.bar(df, x="Trend", y="Percentage", color="Pos/Neg", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Directions"
    return trend_data, graphJSON, header
