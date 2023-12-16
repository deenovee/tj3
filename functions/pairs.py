import json
import pandas as pd
import plotly
import plotly.express as px


def pairs(journal_entries_list, account_change_list, pairs_list):
    trade_data = []
    for journal_entry in journal_entries_list:
        for account_change in account_change_list:
            if journal_entry['trade_id'] == account_change['trade_id']:
                if "pair" in journal_entry and journal_entry["pair"]:
                    trade_data.append({"trade_id": journal_entry["trade_id"], "pair": journal_entry["pair"], "percent_change": account_change["percent_change"]})
                else: continue


    acad_pos = 0
    acad_neg = 0
    achf_pos = 0
    achf_neg = 0
    aj_pos = 0
    aj_neg = 0
    an_pos = 0
    an_neg = 0
    au_pos = 0
    au_neg = 0
    cadchf_pos = 0
    cadchf_neg = 0
    cadjpy_pos = 0
    cadjpy_neg = 0
    ea_pos = 0
    ea_neg = 0
    ecad_pos = 0
    ecad_neg = 0
    echf_pos = 0
    echf_neg = 0
    eg_pos = 0
    eg_neg = 0
    ej_pos = 0
    ej_neg = 0
    en_pos = 0
    en_neg = 0
    eu_pos = 0
    eu_neg = 0
    ga_pos = 0
    ga_neg = 0
    gcad_pos = 0
    gcad_neg = 0
    gchf_pos = 0
    gchf_neg = 0
    gj_pos = 0
    gj_neg = 0
    gn_pos = 0
    gn_neg = 0
    gu_pos = 0
    gu_neg = 0
    ncad_pos = 0
    ncad_neg = 0
    nchf_pos = 0
    nchf_neg = 0
    nj_pos = 0
    nj_neg = 0
    nu_pos = 0
    nu_neg = 0
    ucad_pos = 0
    ucad_neg = 0
    uchf_pos = 0
    uchf_neg = 0
    uj_pos = 0
    uj_neg = 0
    cj_pos = 0
    cj_neg = 0
    gold_pos = 0
    gold_neg = 0
    silver_pos = 0
    silver_neg = 0
    u30_pos = 0
    u30_neg = 0
    spx_pos = 0
    spx_neg = 0
    u100_pos = 0
    u100_neg = 0
    wti_pos = 0
    wti_neg = 0
    xbt_pos = 0
    xbt_neg = 0
    xrp_pos = 0
    xrp_neg = 0

    for trade in trade_data:
        if trade["pair"] == "AUDCAD":
            if trade["percent_change"] > 0:
                acad_pos = acad_pos + trade["percent_change"]
            else:
                acad_neg = acad_neg + trade["percent_change"]

        if trade["pair"] == "AUDCHF":
            if trade["percent_change"] > 0:
                achf_pos = achf_pos + trade["percent_change"]
            else:
                achf_neg = achf_neg + trade["percent_change"]

        if trade["pair"] == "AUDJPY":
            if trade["percent_change"] > 0:
                aj_pos = aj_pos + trade["percent_change"]
            else:
                aj_neg = aj_neg + trade["percent_change"]

        if trade["pair"] == "AUDNZD":
            if trade["percent_change"] > 0:
                an_pos = an_pos + trade["percent_change"]
            else:
                an_neg = an_neg + trade["percent_change"]

        if trade["pair"] == "AUDUSD":
            if trade["percent_change"] > 0:
                au_pos = au_pos + trade["percent_change"]
            else:
                au_neg = au_neg + trade["percent_change"]

        if trade["pair"] == "CADCHF":
            if trade["percent_change"] > 0:
                cadchf_pos = cadchf_pos + trade["percent_change"]
            else:
                cadchf_neg = cadchf_neg + trade["percent_change"]

        if trade["pair"] == "CADJPY":
            if trade["percent_change"] > 0:
                cadjpy_pos = cadjpy_pos + trade["percent_change"]
            else:
                cadjpy_neg = cadjpy_neg + trade["percent_change"]

        if trade["pair"] == "EURAUD":
            if trade["percent_change"] > 0:
                ea_pos = ea_pos + trade["percent_change"]
            else:
                ea_neg = ea_neg + trade["percent_change"]

        if trade["pair"] == "EURCAD":
            if trade["percent_change"] > 0:
                ecad_pos = ecad_pos + trade["percent_change"]
            else:
                ecad_neg = ecad_neg + trade["percent_change"]

        if trade["pair"] == "EURCHF":
            if trade["percent_change"] > 0:
                echf_pos = echf_pos + trade["percent_change"]
            else:
                echf_neg = echf_neg + trade["percent_change"]

        if trade["pair"] == "EURGBP":
            if trade["percent_change"] > 0:
                eg_pos = eg_pos + trade["percent_change"]
            else:
                eg_neg = eg_neg + trade["percent_change"]

        if trade["pair"] == "EURJPY":
            if trade["percent_change"] > 0:
                ej_pos = ej_pos + trade["percent_change"]
            else:
                ej_neg = ej_neg + trade["percent_change"]

        if trade["pair"] == "EURNZD":
            if trade["percent_change"] > 0:
                en_pos = en_pos + trade["percent_change"]
            else:
                en_neg = en_neg + trade["percent_change"]

        if trade["pair"] == "EURUSD":
            if trade["percent_change"] > 0:
                eu_pos = eu_pos + trade["percent_change"]
            else:
                eu_neg = eu_neg + trade["percent_change"]

        if trade["pair"] == "GBPAUD":
            if trade["percent_change"] > 0:
                ga_pos = ga_pos + trade["percent_change"]
            else:
                ga_neg = ga_neg + trade["percent_change"]

        if trade["pair"] == "GBPCAD":
            if trade["percent_change"] > 0:
                gcad_pos = gcad_pos + trade["percent_change"]
            else:
                gcad_neg = gcad_neg + trade["percent_change"]

        if trade["pair"] == "GBPCHF":
            if trade["percent_change"] > 0:
                gchf_pos = gchf_pos + trade["percent_change"]
            else:
                gchf_neg = gchf_neg + trade["percent_change"]

        if trade["pair"] == "GBPJPY":
            if trade["percent_change"] > 0:
                gj_pos = gj_pos + trade["percent_change"]
            else:
                gj_neg = gj_neg + trade["percent_change"]

        if trade["pair"] == "GBPUSD":
            if trade["percent_change"] > 0:
                gu_pos = gu_pos + trade["percent_change"]
            else:
                gu_neg = gu_neg + trade["percent_change"]

        if trade["pair"] == "NZDCAD":
            if trade["percent_change"] > 0:
                ncad_pos = ncad_pos + trade["percent_change"]
            else:
                ncad_neg = ncad_neg + trade["percent_change"]

        if trade["pair"] == "NZDCHF":
            if trade["percent_change"] > 0:
                nchf_pos = nchf_pos + trade["percent_change"]
            else:
                nchf_neg = nchf_neg + trade["percent_change"]

        if trade["pair"] == "NZDJPY":
            if trade["percent_change"] > 0:
                nj_pos = nj_pos + trade["percent_change"]
            else:
                nj_neg = nj_neg + trade["percent_change"]

        if trade["pair"] == "NZDUSD":
            if trade["percent_change"] > 0:
                nu_pos = nu_pos + trade["percent_change"]
            else:
                nu_neg = nu_neg + trade["percent_change"]

        if trade["pair"] == "USDCAD":
            if trade["percent_change"] > 0:
                ucad_pos = ucad_pos + trade["percent_change"]
            else:
                ucad_neg = ucad_neg + trade["percent_change"]

        if trade["pair"] == "USDCHF":
            if trade["percent_change"] > 0:
                uchf_pos = uchf_pos + trade["percent_change"]
            else:
                uchf_neg = uchf_neg + trade["percent_change"]

        if trade["pair"] == "CHFJPY":
            if trade["percent_change"] > 0:
                cj_pos = cj_pos + trade["percent_change"]
            else:
                cj_neg = cj_neg + trade["percent_change"]

        if trade["pair"] == "XAUUSD":
            if trade["percent_change"] > 0:
                gold_pos = gold_pos + trade["percent_change"]
            else:
                gold_neg = gold_neg + trade["percent_change"]

        if trade["pair"] == "XAGUSD":
            if trade["percent_change"] > 0:
                silver_pos = silver_pos + trade["percent_change"]
            else:
                silver_neg = silver_neg + trade["percent_change"]

        if trade["pair"] == "US30":
            if trade["percent_change"] > 0:
                u30_pos = u30_pos + trade["percent_change"]
            else:
                u30_neg = u30_neg + trade["percent_change"]

        if trade["pair"] == "SPX":
            if trade["percent_change"] > 0:
                spx_pos = spx_pos + trade["percent_change"]
            else:
                spx_neg = spx_neg + trade["percent_change"]

        if trade["pair"] == "US100":
            if trade["percent_change"] > 0:
                u100_pos = u100_pos + trade["percent_change"]
            else:
                u100_neg = u100_neg + trade["percent_change"]

        if trade["pair"] == "WTI":
            if trade["percent_change"] > 0:
                wti_pos = wti_pos + trade["percent_change"]
            else:
                wti_neg = wti_neg + trade["percent_change"]

        if trade["pair"] == "XBT":
            if trade["percent_change"] > 0:
                xbt_pos = xbt_pos + trade["percent_change"]
            else:
                xbt_neg = xbt_neg + trade["percent_change"]

        if trade["pair"] == "XRP":
            if trade["percent_change"] > 0:
                xrp_pos = xrp_pos + trade["percent_change"]
            else:
                xrp_neg = xrp_neg + trade["percent_change"]

    pair_data = {
        "AUD_CAD_Pos":round(acad_pos,2),
        "AUD_CAD_Neg":round(acad_neg,2),
        "AUD_CHF_Pos":round(achf_pos,2),
        "AUD_CHF_Neg":round(achf_neg,2),
        "AUD_JPY_Pos":round(aj_pos,2),
        "AUD_JPY_Neg":round(aj_neg,2),
        "AUD_NZD_Pos":round(an_pos,2),
        "AUD_NZD_Neg":round(an_neg,2),
        "AUD_USD_Pos":round(au_pos,2),
        "AUD_USD_Neg":round(au_neg,2),
        "CAD_CHF_Pos":round(cadchf_pos,2),
        "CAD_CHF_Neg":round(cadchf_neg,2),
        "CAD_JPY_Pos":round(cadjpy_pos,2),
        "CAD_JPY_Neg":round(cadjpy_neg,2),
        "EUR_AUD_Pos":round(ea_pos,2),
        "EUR_AUD_Neg":round(ea_neg,2),
        "EUR_CAD_Pos":round(ecad_pos,2),
        "EUR_CAD_Neg":round(ecad_neg,2),
        "EUR_CHF_Pos":round(echf_pos,2),
        "EUR_CHF_Neg":round(echf_neg,2),
        "EUR_GBP_Pos":round(eg_pos,2),
        "EUR_GBP_Neg":round(eg_neg,2),
        "EUR_JPY_Pos":round(ej_pos,2),
        "EUR_JPY_Neg":round(ej_neg,2),
        "EUR_NZD_Pos":round(en_pos,2),
        "EUR_NZD_Neg":round(en_neg,2),
        "EUR_USD_Pos":round(eu_pos,2),
        "EUR_USD_Neg":round(eu_neg,2),
        "GBP_AUD_Pos":round(ga_pos,2),
        "GBP_AUD_Neg":round(ga_neg,2),
        "GBP_CAD_Pos":round(gcad_pos,2),
        "GBP_CAD_Neg":round(gcad_neg,2),
        "GBP_CHF_Pos":round(gchf_pos,2),
        "GBP_CHF_Neg":round(gchf_neg,2),
        "GBP_JPY_Pos":round(gj_pos,2),
        "GBP_JPY_Neg":round(gj_neg,2),
        "GBP_NZD_Pos":round(gn_pos,2),
        "GBP_NZD_Neg":round(gn_neg,2),
        "GBP_USD_Pos":round(gu_pos,2),
        "GBP_USD_Neg":round(gu_neg,2),
        "NZD_CAD_Pos":round(ncad_pos,2),
        "NZD_CAD_Neg":round(ncad_neg,2),
        "NZD_CHF_Pos":round(nchf_pos,2),
        "NZD_CHF_Neg":round(nchf_neg,2),
        "NZD_JPY_Pos":round(nj_pos,2),
        "NZD_JPY_Neg":round(nj_neg,2),
        "NZD_USD_Pos":round(nu_pos,2),
        "NZD_USD_Neg":round(nu_neg,2),
        "USD_CAD_Pos":round(ucad_pos,2),
        "USD_CAD_Neg":round(ucad_neg,2),
        "USD_CHF_Pos":round(uchf_pos,2),
        "USD_CHF_Neg":round(uchf_neg,2),
        "USD_JPY_Pos":round(uj_pos,2),
        "USD_JPY_Neg":round(uj_neg,2),
        "CHF_JPY_Pos":round(cj_pos,2),
        "CHF_JPY_Neg":round(cj_neg,2),
        "XAU_USD_Pos":round(gold_pos,2),
        "XAU_USD_Neg":round(gold_neg,2),
        "XAG_USD_Pos":round(silver_pos,2),
        "XAG_USD_Neg":round(silver_neg,2),
        "US30_Pos":round(u30_pos,2),
        "US30_Neg":round(u30_neg,2),
        "SPX_Pos":round(spx_pos,2),
        "SPX_Neg":round(spx_neg,2),
        "US100_Pos":round(u100_pos,2),
        "US100_Neg":round(u100_neg,2),
        "WTI_Pos":round(wti_pos,2),
        "WTI_Neg":round(wti_neg,2),
        "XBT_Pos":round(xbt_pos,2),
        "XBT_Neg":round(xbt_neg,2),
        "XRP_Pos":round(xrp_pos,2),
        "XRP_Neg":round(xrp_neg,2)
    }
    data_list = []
    for data in pair_data:
        data_list.append(pair_data[data])

    pair_graph_data = []
    for pair in pairs_list:
        fixed = []
        fixed.append(pair_data[pair + "_Pos"])
        fixed.append(pair_data[pair + "_Neg"])

        df = pd.DataFrame({
            "Pair": [pair, pair],
            "Percentage": fixed,
            "Pos/Neg": ["+", "-"]
            })

        fig = px.bar(df, x="Pair", y="Percentage", color="Pos/Neg", barmode="group")

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        pair_graph_data.append(graphJSON)
    header="Pair"

    return pair_data, pair_graph_data, header
