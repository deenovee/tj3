import boto3
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from .config import Config
from .register.register import register_bp
from .login.login import login_blueprint
from .logout.logout import logout_blueprint 
from .home.home import home_blueprint
from .csv_input.csv_input import csv_input_blueprint
from .new_entry.new_entry import new_entry_blueprint
from .new_trade.new_trade import new_trade_blueprint
from .new_entry_option.new_entry_option import new_entry_option_blueprint
from .add_images.add_images import add_images_blueprint
from .trade_images.trade_images import trade_images_blueprint
from .delete_images.delete_images import delete_images_blueprint
from .journal.journal import journal_blueprint
from .edit.edit import edit_blueprint
from .edited.edited import edited_blueprint
from .tables.tables import tables_blueprint
from .date_picker.date_picker import date_picker_blueprint
from .calendar.calendar import calendar_blueprint

# Configure application
app = Flask(__name__)
Config.init_app(app)
app.config.from_object(Config)
Session(app)

app.register_blueprint(register_bp)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(csv_input_blueprint)
app.register_blueprint(new_entry_blueprint)
app.register_blueprint(new_trade_blueprint)
app.register_blueprint(new_entry_option_blueprint)
app.register_blueprint(add_images_blueprint)
app.register_blueprint(trade_images_blueprint)
app.register_blueprint(delete_images_blueprint)
app.register_blueprint(journal_blueprint)
app.register_blueprint(edit_blueprint)
app.register_blueprint(edited_blueprint)
app.register_blueprint(tables_blueprint)
app.register_blueprint(date_picker_blueprint)
app.register_blueprint(calendar_blueprint)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return e

    # Listen for errors
    for code in default_exceptions:
        application.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run()  