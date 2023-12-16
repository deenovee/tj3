from flask import Blueprint, render_template, request, redirect, url_for, session
from ..query_helpers import get_journal_entries, get_username, get_user_balance, get_ratios, get_dollar_amount, update_user, delete_trade, delete_change
from ..helpers import login_required, check_ratios
import math
import boto3
from ..config import Config

journal_blueprint = Blueprint("journal_blueprint", __name__, static_folder="static", template_folder="templates")

# client = boto3.client('s3', aws_access_key_id=Config.AWS_ACCESS_KEY_ID, aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY)

@journal_blueprint.route("/journal", methods=["GET", "POST"])
@login_required
def journal():
    user_id=session.get("user_id")
    balance = get_user_balance(user_id)
    username=get_username(user_id)
    ratios_list = get_ratios(user_id)
    avg = check_ratios(ratios_list)

    if request.method == "GET":
        journal_entries_list = get_journal_entries(user_id)
        journal_pages = len(journal_entries_list) / 8
        return render_template("journal.html", user_id=user_id, journal_data=journal_entries_list[0:8], balance = round(float(balance),2), username=username,journal_pages = math.floor(journal_pages),avg=math.floor(avg))

    else:
        #adding page count
        if "page_number" in request.form:
            journal_entries_list = get_journal_entries(user_id)            
            journal_pages = len(journal_entries_list) / 8
            journal_page = 1
            if ( request.form.get("page_number")):
                journal_page = request.form.get("page_number")
            else:
                journal_page = 1
            journal_page = int(journal_page)
            if (journal_page == 1):
                journal_index_high = journal_page + 7
                journal_index_low = 0
            else:
                journal_index_high = (journal_page * 8) 
                journal_index_low = (journal_page * 8)  - 8
            return render_template("journal.html", user_id=user_id, journal_data=journal_entries_list[journal_index_low:journal_index_high], balance=round(float(balance),2), username=username, journal_pages=math.floor(journal_pages), avg=math.floor(avg))

        else:
            trade_id = request.form.get("delete")
            # formatted_tid = trade_id[0:3] + trade_id[4:7]
            # prefix=str(user_id) + "/" + formatted_tid + "/"
            # response = client.list_objects_v2(Bucket=application.config["S3_BUCKET"], Prefix = prefix, Delimiter = "/")
            # if "Contents" in response:
            #     for object in response['Contents']:
            #         client.delete_object(Bucket=application.config["S3_BUCKET"], Key=object['Key'])

            #CHANGE USER BALANCE
            dollar_amount = get_dollar_amount(trade_id)
            new_balance = float(balance) - float(dollar_amount)
            user_data = {"dollar_amount": round(new_balance, 2)}
            update_user(user_id, user_data)
            delete_trade(trade_id)
            #CHANGE ACCOUNT CHANGE
            delete_change(trade_id)
        
        return redirect(url_for("journal_blueprint.journal"))

