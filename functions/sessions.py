import json
import pandas as pd
import plotly
import plotly.express as px


#SESSION ENTRY

def session_entry(journal_entries_list, account_change_list):

    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "session_entry" in journal_entry and journal_entry["session_entry"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "session_entry": journal_entry["session_entry"], "percent_change": account_change["percent_change"]})
                else: continue


    #CALCULATE % CHANGE BY SESSION ENTRY

    sydney_neg = 0
    sydney_pos = 0
    asia_neg = 0
    asia_pos = 0
    london_neg = 0
    london_pos = 0
    crossover_neg = 0
    crossover_pos = 0
    ny_neg = 0
    ny_pos = 0


    for trade in trade_data:
        if trade["session_entry"] == "Sydney":
            if trade["percent_change"] > 0:
                sydney_pos = sydney_pos + trade["percent_change"]
            else:
                sydney_neg = sydney_neg + trade["percent_change"]
        if trade["session_entry"] == "Asia":
            if trade["percent_change"] > 0:
                asia_pos = asia_pos + trade["percent_change"]
            else:
                asia_neg = asia_neg + trade["percent_change"]
        if trade["session_entry"] == "London":
            if trade["percent_change"] > 0:
                london_pos = london_pos + trade["percent_change"]
            else:
                london_neg = london_neg + trade["percent_change"]
        if trade["session_entry"] == "Crossover":
            if trade["percent_change"] > 0:
                crossover_pos = crossover_pos + trade["percent_change"]
            else:
                crossover_neg = crossover_neg + trade["percent_change"]
        if trade["session_entry"] == "New York":
            if trade["percent_change"] > 0:
                ny_pos = ny_pos + trade["percent_change"]
            else:
                ny_neg = ny_neg + trade["percent_change"]

    session_data = {
        "Sydney_Pos": round(sydney_pos,2),
        "Sydney_Neg": round(sydney_neg,2),
        "Asia_Pos": round(asia_pos,2),
        "Asia_Neg": round(asia_neg,2),
        "London_Pos": round(london_pos,2),
        "London_Neg": round(london_neg,2),
        "Crossover_Pos": round(crossover_pos,2),
        "Crossover_Neg": round(crossover_neg,2),
        "NY_Pos": round(ny_pos,2),
        "NY_Neg": round(ny_neg,2)
    }
    positives =[]
    negatives = []
    labels=["Sydney", "Asia", "London", "Crossovwer", "New York"]
    for data in session_data:
        if data[-3:] == "Pos":
            positives.append(session_data[data])
        else:
            negatives.append(session_data[data])
    fixed = positives + negatives
    df = pd.DataFrame({
        "Sessions": labels + labels,
        "Percentage": fixed,
        "Pos/Neg": ["+", "+", "+", "+", "+", "-", "-", "-", "-", "-"]
        })
    fig = px.bar(df, x="Sessions", y="Percentage", color="Pos/Neg", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Sessions"
    return session_data, graphJSON, header 


#SESSION EXIT


def session_exit(journal_entries_list, account_change_list):       
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "session_exit" in journal_entry and journal_entry["session_exit"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "session_exit": journal_entry["session_exit"], "percent_change": account_change["percent_change"]})
                else: continue


    sydney_neg = 0
    sydney_pos = 0
    asia_neg = 0
    asia_pos = 0
    london_neg = 0
    london_pos = 0
    crossover_neg = 0
    crossover_pos = 0
    ny_neg = 0
    ny_pos = 0


    for trade in trade_data:
        if trade["session_exit"] == "Sydney":
            if trade["percent_change"] > 0:
                sydney_pos = sydney_pos + trade["percent_change"]
            else:
                sydney_neg = sydney_neg + trade["percent_change"]
        if trade["session_exit"] == "Asia":
            if trade["percent_change"] > 0:
                asia_pos = asia_pos + trade["percent_change"]
            else:
                asia_neg = asia_neg + trade["percent_change"]
        if trade["session_exit"] == "London":
            if trade["percent_change"] > 0:
                london_pos = london_pos + trade["percent_change"]
            else:
                london_neg = london_neg + trade["percent_change"]
        if trade["session_exit"] == "Crossover":
            if trade["percent_change"] > 0:
                crossover_pos = crossover_pos + trade["percent_change"]
            else:
                crossover_neg = crossover_neg + trade["percent_change"]
        if trade["session_exit"] == "New York":
            if trade["percent_change"] > 0:
                ny_pos = ny_pos + trade["percent_change"]
            else:
                ny_neg = ny_neg + trade["percent_change"]

    session_data = {
        "Sydney_Pos": round(sydney_pos,2),
        "Sydney_Neg": round(sydney_neg,2),
        "Asia_Pos": round(asia_pos,2),
        "Asia_Neg": round(asia_neg,2),
        "London_Pos": round(london_pos,2),
        "London_Neg": round(london_neg,2),
        "Crossover_Pos": round(crossover_pos,2),
        "Crossover_Neg": round(crossover_neg,2),
        "NY_Pos": round(ny_pos,2),
        "NY_Neg": round(ny_neg,2)
    }

    positives =[]
    negatives = []
    labels=["Sydney", "Asia", "London", "Crossovwer", "New York"]
    for data in session_data:
        if data[-3:] == "Pos":
            positives.append(session_data[data])
        else:
            negatives.append(session_data[data])
    fixed = positives + negatives
    df = pd.DataFrame({
        "Sessions": labels + labels,
        "Percentage": fixed,
        "Pos/Neg": ["+", "+", "+", "+", "+", "-", "-", "-", "-", "-"]
        })
    fig = px.bar(df, x="Sessions", y="Percentage", color="Pos/Neg", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Sessions"

    return session_data, graphJSON, header
