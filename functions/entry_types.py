import json
import pandas as pd
import plotly
import plotly.express as px

def entry_type(journal_entries_list, account_change_list):
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "entry_type" in journal_entry and journal_entry["entry_type"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "entry_type": journal_entry["entry_type"], "percent_change": account_change["percent_change"]})
                else: continue

            
            #CALCULATE % CHANGE BY ENTRY TYPE
            zero_pos = 0
            zero_neg = 0
            fifty_pos = 0
            fifty_neg = 0
            eighty_pos = 0
            eighty_neg = 0

            for trade in trade_data:
                if trade["entry_type"] == 0:
                    if trade["percent_change"] > 0:
                        zero_pos = zero_pos + trade["percent_change"]
                    else:
                        zero_neg = zero_neg + trade["percent_change"]
                if trade["entry_type"] == 50:
                    if trade["percent_change"] > 0:
                        fifty_pos = fifty_pos + trade["percent_change"]
                    else:
                        fifty_neg = fifty_neg + trade["percent_change"]
                if trade["entry_type"] == 80:
                    if trade["percent_change"] > 0:
                        eighty_pos = eighty_pos + trade["percent_change"]
                    else:
                        eighty_neg = eighty_neg + trade["percent_change"]

            entry_type_data = {
                "Zero_Pos": round(zero_pos,2),
                "Zero_Neg": round(zero_neg,2),
                "Fifty_Pos": round(fifty_pos,2),
                "Fifty_Neg": round(fifty_neg,2),
                "Eighty_Pos": round(eighty_pos,2),
                "Eighty_Neg": round(eighty_neg,2)
            }

            positives =[]
            negatives = []
            for data in entry_type_data:
                if data[-3:] == "Pos":
                    positives.append(entry_type_data[data])
                else:
                    negatives.append(entry_type_data[data])
            fixed = positives + negatives
            df = pd.DataFrame({
                "Entry Type": ["Zero", "Fifty", "Eighty", "Zero", "Fifty", "Eighty",],
                "Percentage": fixed,
                "Pos/Neg": ["+", "+", "+", "-", "-", "-"]
                })

            fig = px.bar(df, x="Entry Type", y="Percentage", color="Pos/Neg", barmode="group")

            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            header="Entry Type"
            return entry_type_data, graphJSON, header
