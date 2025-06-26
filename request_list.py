import requests

#Roblox game universe ID
universeID = '24833080'

#Gets the player id and aliases when given username
def userInfo(username: str):
    # API endpoints
    username_url = "https://users.roblox.com/v1/usernames/users"

    #Username payload
    payload = {
        "usernames": [username],
        "excludeBannedUsers": True
    }

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    return requests.post(username_url, json=payload, headers=headers)

#Gets the badges a user has collected when given a userID
def getCollectedBadges(userId, gameData):
    #
    #
    # We are getting all game badges on inserted username. Maybe we could do this a different way?
    #
    #
    badges_url = "https://badges.roblox.com/v1/users/" + str(userId) + "/badges/awarded-dates?badgeIds="

    nonCanon = []
    breakpoint = 4406520174507095
    isNonCanon = False

    first = True
    for badge in gameData:
        if first:
           badges_url += str(badge.id)
           first = False
        else:
            badges_url +=("," + str(badge.id) )

        if badge.id == breakpoint:
            isNonCanon = True
        
        if isNonCanon:
            nonCanon.append(badge.to_dict())

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(badges_url, headers=headers)
    if response.status_code == 200:
        return (response, nonCanon)
    else:
        #TODO: Brush this up, very messy
        return False

# { BADGE RESPONSE BODY
#       "id": 19361395,
#       "name": "\"Hidden\" badge",
#       "description": "The first badge I ever drew. Your hint is: Red.",
#       "displayName": "\"Hidden\" badge",
#       "displayDescription": "The first badge I ever drew. Your hint is: Red.",
#       "enabled": true,
#       "iconImageId": 19361211,
#       "displayIconImageId": 19361211,
#       "created": "2009-12-18T00:22:38.237+00:00",
#       "updated": "2021-01-28T01:11:24.483+00:00",
#       "statistics": {
#         "pastDayAwardedCount": 3,
#         "awardedCount": 1115,
#         "winRatePercentage": 0.522
#       },
#       "awardingUniverse": {
#         "id": 24833080,
#         "name": "Happy Home Badge Hunt (61)",
#         "rootPlaceId": 19336334
#       }

#Gets all of the badges belonging to a specific Roblox game
def getGameBadges():
    # API endpoints
    badges_url = "https://badges.roblox.com/v1/universes/" + universeID +"/badges?sortBy=Rank&limit=100&sortOrder=Asc"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    return requests.get(badges_url, headers=headers)
    



