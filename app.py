# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor
from request_list import *
from operations import *
from flask_bootstrap import Bootstrap

from models.badgeModel import badgeInfoMaker

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
#import email_validator

import os


#request is used to parse request data and figure out what to return

#API info at https://users.roblox.com//docs/index.html, and https://badges.roblox.com//docs/index.html?urls.primaryName=Badges%20Api%20v1


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
Bootstrap(app)

#If I ever need to run multiple threads at a time :)
executor = ThreadPoolExecutor(max_workers=5)


# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

# Create SQLAlchemy instance
db = SQLAlchemy(app)


port_number = 5000

#Universe ID:
universe_id = 24833080

#Gets badges from the database on spinup since they are not changing
badgeConstructor = None
with app.app_context():
    badgeConstructor = badgeInfoMaker(db)

@app.route('/')
def opener():
    return render_template('opener.html')


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', error="User Not Found")
    

#Handle if the user makes a badge request
@app.route('/badges', methods=['GET', 'POST'])
def badges():
    if request.method == 'POST':
        #TODO: Handle requests in a different class?
        #Sending a request. See if user is valid
        nameRequest = request.form.get('R_Name')

        if nameRequest.strip() == '':
            #TODO: Message flash here
            return render_template('badges.html', error='Username cannot be empty')

        userResponse = userInfo(nameRequest)

        errorMessage = "Unknown Error Occurred"

        #We can make this better with showing a error response message
        if userResponse.status_code != 200:
            return render_template('badges.html', error="Roblox Server Error")

        data = userResponse.json()['data']
        if len(data) == 0:
            return render_template('badges.html', error="User Not Found")
        
        data = data[0]
        #We will have to do much more for comparing badges to users current badges

        gameData = getGameBadges()
        gameData = gameData.json()['data']

        db_badges = badgeConstructor.query.order_by(badgeConstructor.order.asc()).all()

        retrievedBadges = getCollectedBadges(data['id'], db_badges)

        #Dictionary of Parameters
        context = {
            'gameData': createBadgeList(retrievedBadges['data'], db_badges),
            'userName' : data['name'],
            'userId' : data['id'],
            'earnedDict' : retrievedBadges
        }

        return render_template('badgesresponse.html', **context)

        #TODO: Turn back into try-catch block

        # try:
        #     data = data[0]
        #     #We will have to do much more for comparing badges to users current badges

        #     gameData = getGameBadges()
        #     gameData = gameData.json()['data']

        #     db_badges = badgeConstructor.query.order_by(badgeConstructor.order.asc()).all()

        #     retrievedBadges = getCollectedBadges(data['id'], db_badges)

        #     #Dictionary of Parameters
        #     context = {
        #         'gameData': createBadgeList(gameData, retrievedBadges, db_badges),
        #         'userName' : data['name'],
        #         'userId' : data['id'],
        #         'earnedDict' : retrievedBadges
        #     }

        #     return render_template('badgesresponse.html', **context)
        # except Exception as e:
        #     return render_template('badges.html', error=f"Internal Server Error: {e}")
    else:
        return render_template('badges.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/fanart')
def fanart():
    return render_template('fanart.html')
    
    
if __name__ == '__main__':
    with app.app_context():  # Needed for DB operations
        db.create_all()      # Creates the database and tables
    app.run(debug=True, port=port_number)