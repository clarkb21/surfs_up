from re import X
from flask import Flask

#Add a flask instance (instance is a general term to refer to a singular version of something)
app = Flask(__name__)
#variables with underscores before and after them are called magic methods in Python

#To create first route, we need to define the starting point (aka Root)
@app.route('/') #Putting the forward slash means we want to put data at the root of our route
def hello_world():
    return "Hello world"

def square(x):
    squared= x*X
    return (f"The number squared is equal to {squared}")
