#Add a flask instance (instance is a general term to refer to a singular version of something)
#app = Flask(__name__)
#variables with underscores before and after them are called magic methods in Python

#To create first route, we need to define the starting point (aka Root)
# @app.route('/') #Putting the forward slash means we want to put data at the root of our route
# def hello_world():
#     return "Hello world"
#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Set up the database, create_engine() allows us to access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

#Reflect SQL tables
Base.prepare(engine, reflect= True)
#Create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link from Python to our database
session = Session(engine)

#Set up flask
app = Flask(__name__)

#Set up welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipiation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Creating the precipiation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Jsonify the data to create a dictionary

#Create the Stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

    #Create monthly temperature route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.datetime(2017,8,23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Create the statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start = None, end = None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end: 
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
        