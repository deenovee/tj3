Forex Trading Journal Web App

Overview

This Python Flask server project is designed to serve a web-based Forex trading journal. The project utilizes Flask Blueprints to organize routes into modular components, making the codebase more maintainable and scalable. The web application allows users to sign in or register, view their trading account balance, and monitor their trading success based on various parameters such as day, time, and asset. Users can keep track of their daily earnings and conveniently insert their trades using a CSV file downloaded from MetaTrader.

Features

User authentication (Sign Up, Sign In, Logout)
View trading account balance
Monitor trading success based on day, time, asset, etc.
Keep track of daily earnings
Insert trades using a CSV file downloaded from MetaTrader

Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/dylanpvillan/forex-trading-journal.git
    cd forex-trading-journal

Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:

    ```bash
    pip install -r requirements.txt

Run the Flask application:

    ```bash 
    flask run

Open a web browser and navigate to http://localhost:5000 to access the Forex Trading Journal web app.