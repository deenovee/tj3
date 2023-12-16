import json
import pandas as pd
import plotly
import plotly.express as px


def strategy(journal_entries_list, account_change_list, strategies):
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "strategy" in journal_entry and journal_entry["strategy"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "strategy": journal_entry["strategy"], "percent_change": account_change["percent_change"]})
                else: continue

    #CALCULATE % CHANGE BY STRATEGY
    a1_pos = 0
    a1_neg = 0
    a2_pos = 0
    a2_neg = 0
    a4_pos = 0
    a4_neg = 0
    d1_pos = 0
    d1_neg = 0
    d2_pos = 0
    d2_neg = 0
    d4_pos = 0
    d4_neg = 0
    ra_pos = 0
    ra_neg = 0
    rd_pos = 0
    rd_neg = 0
    x_pos = 0
    x_neg = 0
    bos_pos = 0
    bos_neg = 0
    order_pos = 0
    order_neg = 0
    scalp_pos = 0
    scalp_neg = 0

    for trade in trade_data:
        if trade["strategy"] == "Accu Type 1":
            if trade["percent_change"] > 0:
                a1_pos = a1_pos + trade["percent_change"]
            else:
                a1_neg = a1_neg + trade["percent_change"]
        if trade["strategy"] == "Accu Type 2":
            if trade["percent_change"] > 0:
                a2_pos = a2_pos + trade["percent_change"]
            else:
                a2_neg = a2_neg + trade["percent_change"]
        if trade["strategy"] == "Accu Type 4":
            if trade["percent_change"] > 0:
                a4_pos = a4_pos + trade["percent_change"]
            else:
                a4_neg = a4_neg + trade["percent_change"]
        if trade["strategy"] == "Distro Type 1":
            if trade["percent_change"] > 0:
                d1_pos = d1_pos + trade["percent_change"]
            else:
                d1_neg = d1_neg + trade["percent_change"]
        if trade["strategy"] == "Distro Type 2":
            if trade["percent_change"] > 0:
                d2_pos = d2_pos + trade["percent_change"]
            else:
                d2_neg = d2_neg + trade["percent_change"]
        if trade["strategy"] == "Distro Type 4":
            if trade["percent_change"] > 0:
                d4_pos = d4_pos + trade["percent_change"]
            else:
                d4_neg = d4_neg + trade["percent_change"]
        if trade["strategy"] == "Re Accu":
            if trade["percent_change"] > 0:
                ra_pos = ra_pos + trade["percent_change"]
            else:
                ra_neg = ra_neg + trade["percent_change"]
        if trade["strategy"] == "Re Distro":
            if trade["percent_change"] > 0:
                rd_pos = rd_pos + trade["percent_change"]
            else:
                rd_neg = rd_neg + trade["percent_change"]
        if trade["strategy"] == "Extreme":
            if trade["percent_change"] > 0:
                x_pos = x_pos + trade["percent_change"]
            else:
                x_neg = x_neg + trade["percent_change"]
        if trade["strategy"] == "BOS":
            if trade["percent_change"] > 0:
                bos_pos = bos_pos + trade["percent_change"]
            else:
                bos_neg = bos_neg + trade["percent_change"]
        if trade["strategy"] == "Orderflow":
            if trade["percent_change"] > 0:
                order_pos = order_pos + trade["percent_change"]
            else:
                order_neg = order_neg + trade["percent_change"]
        if trade["strategy"] == "Scalp":
            if trade["percent_change"] > 0:
                scalp_pos = scalp_pos + trade["percent_change"]
            else:
                scalp_neg = scalp_neg + trade["percent_change"]

    strategy_data = {
        "A1_Pos": round(a1_pos,2),
        "A1_Neg": round(a1_neg,2),
        "A2_Pos": round(a2_pos,2),
        "A2_Neg": round(a2_neg,2),
        "A4_Pos": round(a4_pos,2),
        "A4_Neg": round(a4_neg,2),
        "D1_Pos": round(d1_pos,2),
        "D1_Neg": round(d1_neg,2),
        "D2_Pos": round(d2_pos,2),
        "D2_Neg": round(d2_neg,2),
        "D4_Pos": round(d4_pos,2),
        "D4_Neg": round(d4_neg,2),
        "RA_Pos": round(ra_pos,2),
        "RA_Neg": round(ra_neg,2),
        "RD_Pos": round(rd_pos,2),
        "RD_Neg": round(rd_neg,2),
        "X_Pos": round(x_pos,2),
        "X_Neg": round(x_neg,2),
        "BOS_Pos": round(bos_pos,2),
        "BOS_Neg": round(bos_neg,2),
        "Order_Pos": round(order_pos,2),
        "Order_Neg": round(order_neg,2),
        "Scalp_Pos": round(scalp_pos,2),
        "Scalp_Neg": round(scalp_neg,2)
    }

    positives =[]
    negatives = []
    for data in strategy_data:
        if data[-3:] == "Pos":
            positives.append(strategy_data[data])
        else:
            negatives.append(strategy_data[data])
    fixed = positives + negatives
    df = pd.DataFrame({
        "Strategies": strategies + strategies,
        "Percentage": fixed,
        "Pos/Neg": ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        })

    fig = px.bar(df, x="Strategies", y="Percentage", color="Pos/Neg", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Strategies"

    return strategy_data, graphJSON, header
