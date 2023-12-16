import json
import pandas as pd
import plotly
import plotly.express as px

def day(journal_entries_list, account_change_list, days):
    # Combine the results of the two queries to get the equivalent of an inner join
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "day" in journal_entry and journal_entry["day"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "day": journal_entry["day"], "percent_change": account_change["percent_change"]})
                else: continue

    
    #CALCULATE % CHANGE BY DAY
    m_pos = 0
    m_neg = 0
    t_pos = 0
    t_neg = 0
    w_pos = 0
    w_neg = 0
    th_pos = 0
    th_neg = 0
    f_pos = 0
    f_neg = 0
    sat_pos = 0
    sat_neg = 0
    sun_pos = 0
    sun_neg = 0

    for trade in trade_data:
        if trade["day"] == "Monday":
            if trade["percent_change"] > 0:
                m_pos = m_pos + trade["percent_change"]
            else:
                m_neg = m_neg + trade["percent_change"]
        if trade["day"] == "Tuesday":
            if trade["percent_change"] > 0:
                t_pos = t_pos + trade["percent_change"]
            else:
                t_neg = t_neg + trade["percent_change"]
        if trade["day"] == "Wednesday":
            if trade["percent_change"] > 0:
                w_pos = w_pos + trade["percent_change"]
            else:
                w_neg = w_neg + trade["percent_change"]
        if trade["day"] == "Thursday":
            if trade["percent_change"] > 0:
                th_pos = th_pos + trade["percent_change"]
            else:
                th_neg = th_neg + trade["percent_change"]
        if trade["day"] == "Friday":
            if trade["percent_change"] > 0:
                f_pos = f_pos + trade["percent_change"]
            else:
                f_neg = f_neg + trade["percent_change"]
        if trade["day"] == "Saturday":
            if trade["percent_change"] > 0:
                sat_pos = sat_pos + trade["percent_change"]
            else:
                sat_neg = sat_neg + trade["percent_change"]
        if trade["day"] == "Sunday":
            if trade["percent_change"] > 0:
                sun_pos = sun_pos + trade["percent_change"]
            else:
                sun_neg = sun_neg + trade["percent_change"]

    day_data = {
        "Sun_Pos": round(sun_pos,2),
        "Sun_Neg": round(sun_neg,2),
        "M_Pos": round(m_pos,2),
        "M_Neg": round(m_neg,2),
        "T_Pos": round(t_pos,2),
        "T_Neg": round(t_neg,2),
        "W_Pos": round(w_pos,2),
        "W_Neg": round(w_neg,2),
        "Th_Pos": round(th_pos,2),
        "Th_Neg": round(th_neg,2),
        "F_Pos": round(f_pos,2),
        "F_Neg": round(f_neg,2),
        "Sat_Pos": round(sat_pos,2),
        "Sat_Neg": round(sat_neg,2)
    }

    positives =[]
    negatives = []
    for data in day_data:
        if data[-3:] == "Pos":
            positives.append(day_data[data])
        else:
            negatives.append(day_data[data])
    fixed = positives + negatives
    df = pd.DataFrame({
        "Days": days + days,
        "Percentage": fixed,
        "Pos/Neg": ["+", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-", "-", "-", "-"]
        })

    fig = px.bar(df, x="Days", y="Percentage", color="Pos/Neg", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Days"
    return day_data, graphJSON, header