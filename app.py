# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template, jsonify
import requests
from request_list import *
from flask_bootstrap import Bootstrap

#request is used to parse request data and figure out what to return

#API info at https://users.roblox.com//docs/index.html, and https://badges.roblox.com//docs/index.html?urls.primaryName=Badges%20Api%20v1


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
Bootstrap(app)
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
port_number = 5000

#Universe ID:
universe_id = 24833080

@app.route('/')
def home():
    return redirect(url_for('cube'))


@app.route('/cube', methods=['GET', 'POST'])
def cube():
    if request.method == 'POST':
        num = request.form.get('num')

        if num.strip() == '':
            return render_template("stringinput.html", message='No number entered. Please enter an integer')

        try:
            cubed = int(num)** 3
            return render_template("answer.html", initialNum=num, cubedNum=cubed)
        except:
            return render_template("stringinput.html", message='Invalid input. Please enter a valid number.')
    else:
        return render_template("stringinput.html")
    

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
        if userResponse.status_code == 200:
            data = userResponse.json()['data']
            if len(data) != 0:
                data = data[0]
                #We will have to do much more for comparing badges to users current badges
                gameData = getGameBadges()

                gameData = gameData.json()['data']

                retrievedBadges = getCollectedBadges(data['id'] ,gameData)

                #Dictionary of Parameters
                context = {
                    'gameData': gameData,
                    'userName' : data['name'],
                    'userId' : data['id'],
                    'earnedDict' : retrievedBadges.json()['data']
                }

                return render_template('badgesresponse.html', **context)
            else:
                errorMessage = "User Not Found"
        
        return render_template('badges.html', error=errorMessage)
    else:
        return render_template('badges.html')

    
if __name__ == '__main__':
    app.run(debug=True, port=port_number)