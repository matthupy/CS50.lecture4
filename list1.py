import os, csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight_orig.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration}")

if __name__ == "__main__":
    with app.app_context(): # One of the nuances of Flask, allows us to interact with the flask app without a webpage
        main()