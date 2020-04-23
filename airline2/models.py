from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Flight_orig(db.Model):
    __tablename__ = "flights_orig"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights_orig.id"), nullable=False)