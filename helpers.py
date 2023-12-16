import math
from flask import session, redirect, render_template
from functools import wraps


def allowed_file(filename, ALLOWED_EXTENSIONS):     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def exists(trade_id, journal_entries):
    trade_list = []
    for entry in journal_entries:
        trade_list.append(entry['trade_id'])
    if trade_id in trade_list:
            return True
    else: return False

def percent_change(new, old):
    if float(old) == 0:
        old = 0.01
    percent_change = ((float(old) - new) / float(old)) * 100
    if percent_change > 0:
        percent_change = -percent_change
    elif percent_change < 0:
        percent_change = abs(percent_change)
    return percent_change

def risk_reward(enter, sl, tp):
    if float(sl) == 0 or float(tp) == 0:
        rrr = 1
    else:
        loss_difference = abs(float(sl) - float(enter))
        gain_difference = abs(float(tp) - float(enter))
        rrr = math.floor(gain_difference / loss_difference)
    return rrr

def check_ratios(ratios_list):
    total=0
    avg=0
    if len(ratios_list) >= 1:
        for ratio in ratios_list:
            total = total + int(ratio['rrr'])
        avg = total/len(ratios_list)
    else: avg = 1
    return avg


