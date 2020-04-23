import os
from flask import Flask, render_template, request, jsonify
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight_orig.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """ Book a flight. """

    # Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")
    
    # Make sure the flight exists.
    flight = Flight_orig.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger.
    flight.add_passenger(name)
    return render_template("success.html")

@app.route("/flights")
def flights():
    """ Lists all flights. """
    flights = Flight_orig.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """ List a single flight """

    # Make sure the flight exists.
    flight = Flight_orig.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Get all passengers
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """ Return details about a single flight. """

    # Make sure the flight exists.
    flight = Flight_orig.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "Invalid flight_id"}), 422

    # Get all passengers
    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })

if __name__ == "__main__":
    with app.app_context(): # One of the nuances of Flask, allows us to interact with the flask app without a webpage
        app.run()