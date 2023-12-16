import json
import pandas as pd
import plotly
import plotly.express as px


def direction(journal_entries_list, account_change_list, directions_list):
    
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry["trade_id"] == account_change["trade_id"]:
                if "direction" in journal_entry and journal_entry["direction"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "direction": journal_entry["direction"], "percent_change": account_change["percent_change"]})
                else: continue


    
    #CALCULATE % CHANGE DIRECTION
    long_pos = 0
    long_neg = 0
    short_pos = 0
    short_neg = 0
    for trade in trade_data:
        if trade["direction"] == "Long":
            if trade["percent_change"] > 0:
                long_pos = long_pos + trade["percent_change"]
            else:
                long_neg = long_neg + trade["percent_change"]
        if trade["direction"] == "Short":
            if trade["percent_change"] > 0:
                short_pos = short_pos + trade["percent_change"]
            else:
                short_neg = short_neg + trade["percent_change"]

    direction_data = {
        "Long_Pos": round(long_pos,2),
        "Long_Neg": round(long_neg,2),
        "Short_Pos": round(short_pos,2),
        "Short_Neg": round(short_neg,2)
    }

    positives =[]
    negatives = []
    for data in direction_data:
        if data[-3:] == "Pos":
            positives.append(direction_data[data])
        else:
            negatives.append(direction_data[data])
    fixed = positives + negatives
    df = pd.DataFrame({
        "Directions": directions_list + directions_list,
        "Percentage": fixed,
        "Pos/Neg": ["+", "+", "-", "-"]
        })
    fig = px.bar(df, x="Directions", y="Percentage", color="Pos/Neg", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Directions"

    return direction_data, graphJSON, header