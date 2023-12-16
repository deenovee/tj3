import json
import pandas as pd
import plotly
import plotly.express as px


def reason_for_loss(journal_entry_list, account_change_list, reasons):

    trade_data = []
    for journal_entry in journal_entry_list:
        for account_change in account_change_list:
            if journal_entry["trade_id"] == account_change["trade_id"]:
                if "reason_for_loss" in journal_entry and journal_entry["reason_for_loss"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "reason_for_loss": journal_entry["reason_for_loss"], "percent_change": account_change["percent_change"]})
                else: continue


    orderflow = 0
    entered_early = 0
    outside_window = 0
    low_prob = 0
    mgmt = 0
    fomo = 0
    counter = 0
    misread = 0
    spread = 0
    prem_disc = 0
    mindset = 0
    new_strat = 0
    overleverage = 0
    n_a = 0

    for trade in trade_data:
        if trade["reason_for_loss"] == "Orderflow":
            if trade["percent_change"] < 0:
                orderflow = orderflow + trade["percent_change"]
        if trade["reason_for_loss"] == "Entered Too Early":
            if trade["percent_change"] < 0:
                entered_early = entered_early + trade["percent_change"]
        if trade["reason_for_loss"] == "Outside Trading Window":
            if trade["percent_change"] < 0:
                outside_window = outside_window + trade["percent_change"]
        if trade["reason_for_loss"] == "Low Probability":
            if trade["percent_change"] < 0:
                low_prob = low_prob + trade["percent_change"]
        if trade["reason_for_loss"] == "Bad/No Trade Mgmt":
            if trade["percent_change"] < 0:
                mgmt = mgmt + trade["percent_change"]
        if trade["reason_for_loss"] == "FOMO":
            if trade["percent_change"] < 0:
                fomo = fomo + trade["percent_change"]
        if trade["reason_for_loss"] == "Counter-Trend":
            if trade["percent_change"] < 0:
                counter = counter + trade["percent_change"]
        if trade["reason_for_loss"] == "Misread Structure":
            if trade["percent_change"] < 0:
                misread = misread + trade["percent_change"]
        if trade["reason_for_loss"] == "Spread":
            if trade["percent_change"] < 0:
                spread = spread + trade["percent_change"]
        if trade["reason_for_loss"] == "Not In Prem/Disc":
            if trade["percent_change"] < 0:
                prem_disc = prem_disc + trade["percent_change"]
        if trade["reason_for_loss"] == "Mindset":
            if trade["percent_change"] < 0:
                mindset = mindset + trade["percent_change"]
        if trade["reason_for_loss"] == "New Strategy":
            if trade["percent_change"] < 0:
                new_strat = new_strat + trade["percent_change"]
        if trade["reason_for_loss"] == "Overleverage":
            if trade["percent_change"] < 0:
                overleverage = overleverage + trade["percent_change"]
        if trade["reason_for_loss"] == "N/A":
            if trade["percent_change"] > 0:
                n_a = n_a + trade["percent_change"]

    reason_data = {
        "Orderflow": round(orderflow,2),
        "Entered_Early": round(entered_early,2),
        "Outside_Window": round(outside_window,2),
        "Low_Prob": round(low_prob,2),
        "Mgmt": round(mgmt,2),
        "FOMO": round(fomo,2),
        "Counter": round(counter,2),
        "Misread": round(misread,2),
        "Spread": round(spread,2),
        "Prem_Disc": round(prem_disc,2),
        "Mindset": round(mindset,2),
        "New_Strat": round(new_strat,2),
        "Overleverage": round(overleverage,2),
        "N_A": round(n_a,2)
    }

    values=[]
    for data in reason_data:
        values.append(reason_data[data])
    fixed = values + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    df = pd.DataFrame({
        "Reasons": reasons + reasons,
        "Percentage": fixed,
        "Neg/Pos": ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "-"]
        })
    fig = px.bar(df, x="Reasons", y="Percentage", color="Neg/Pos", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Reasons"

    return reason_data, graphJSON, header
