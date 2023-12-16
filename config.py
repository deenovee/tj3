# config.py
import boto3
from tempfile import mkdtemp


class Config:
    # Ensure templates are auto-reloaded
    TEMPLATES_AUTO_RELOAD = True
    S3_BUCKET_NAME = "tj-screenshots"
    # Flask session configuration
    SESSION_FILE_DIR = mkdtemp()
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    # Custom constants
    PAIRS_LIST = ["AUD_CAD", "AUD_CHF", "AUD_JPY", "AUD_NZD", "AUD_USD", "CAD_CHF", "CAD_JPY", "EUR_AUD", "EUR_CAD", "EUR_CHF", "EUR_GBP", "EUR_JPY", "EUR_NZD", "EUR_USD", "GBP_AUD", "GBP_CAD", "GBP_CHF", "GBP_JPY", "GBP_NZD", "GBP_USD", "NZD_CAD", "NZD_CHF", "NZD_JPY", "NZD_USD", "USD_CAD", "USD_CHF", "USD_JPY", "CHF_JPY", "XAU_USD", "XAG_USD", "US30", "SPX", "US100", "WTI", "XBT", "XRP"]
    DIRECTIONS = ["Long", "Short"]
    OUTCOMES = ["Win", "Loss"]
    STRATEGIES = ["Accu Type 1", "Accu Type 2", "Accu Type 4", "Distro Type 1", "Distro Type 2", "Distro Type 4", "Re Accu", "Re Distro", "Extreme", "BOS", "Orderflow", "Scalp"]
    ENTRY_TYPES = [0, 50, 80]
    SESSIONS = ["Sydney", "Asia", "London", "Crossover", "New York"]
    TRENDS = ["Up", "Down"]
    DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    REASONS = ["Orderflow", "Entered Too Early", "Outside Trading Window", "Low Probability", "Bad/No Trade Mgmt", "FOMO", "Counter-Trend", "Misread Structure", "Spread", "Not In Prem/Disc", "Mindset", "New Strategy", "Overleverage", "N/A"]
    
    def init_app(app):
        ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])
        client = boto3.client('s3')

        @app.after_request
        def after_request(response):
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Expires"] = 0
            response.headers["Pragma"] = "no-cache"
            return response

