from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
# get the database
db = client.get_database("journal")
journal_entries = db["journal_entry"]
users = db["users"]
account_change = db["account_change"]


#
#
#JOURNAL_ENTRY TABLE QUERIES
#
#


#Get Docs
def get_username(user_id):
    username=users.find_one({"user_id": user_id}, {"username": 1})["username"]
    return username

def get_journal_entries(user_id):
    journal_entries_list = list(journal_entries.find({'user_id': user_id}))
    return journal_entries_list

def get_trade(trade_id):
    entry_data = journal_entries.find_one({"trade_id": trade_id})
    return entry_data

def get_ratios(user_id):
    ratios_list = list(journal_entries.find({"user_id": user_id}, {"rrr": 1}))
    return ratios_list

def get_dollar_amount(trade_id):
    dollar_amount = journal_entries.find_one({"trade_id": trade_id}, {"dollar_amount": 1})['dollar_amount']
    return dollar_amount

def get_dates(user_id):
    trade_dates = journal_entries.find({"user_id": user_id}, {"date_close": 1, "trade_id": 1, "dollar_amount": 1})
    return trade_dates



#Insert Docs
def insert_journal(data):
    journal_entries.insert_one(data)


#Delete Docs
def delete_trade(trade_id):
    journal_entries.delete_one({"trade_id": trade_id})

#Update Docs
def update_trade(trade_id, data):
    journal_entries.update_one({"trade_id": trade_id}, {"$set": data})



#
#
#USER TABLE QUERIES
#
#

#Get Docs
def check_user(username):
    if users.find_one({"username": username}):
        return True
    else: return False

def create_user(username, hash, dollar_amount):
    users.insert_one({"username": username, "hash": hash, "dollar_amount": dollar_amount})

def find_user(username):
    user = users.find_one({"username": username})
    return user

def get_user_balance(user_id):
    balance = users.find_one({"user_id": user_id}, {"dollar_amount": 1})['dollar_amount']
    return balance

#Insert Docs

#Delete Docs

#Update Docs
def update_user(user_id, data):
    users.update_one({"user_id": user_id}, {"$set": data})


#
#
#ACCOUNT_CHANGE TABLE QUERIES
#
#

#Get Docs

def get_account_changes(user_id):
    account_change_list = list(account_change.find({"user_id": user_id}))
    return account_change_list

def get_trade_percs(user_id, filters):
    trade_percentages = account_change.find({"user_id": user_id}, filters)
    return trade_percentages

#Insert Docs
def add_change(change_data):
    account_change.insert_one(change_data)


#Delete Docs
def delete_change(trade_id):
    account_change.delete_one({"trade_id": trade_id})


#Update Docs
def update_change(trade_id, change_data):
    account_change.update_one({"trade_id": trade_id}, {"$set": change_data})
