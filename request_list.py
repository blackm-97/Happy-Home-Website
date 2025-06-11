import requests

#Roblox game universe ID
universeID = 24833080

#Gets the player id and aliases when given username
def userInfo(username: str) -> requests.Response:
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
def getCollectedBadges(userId):
    return 0

def getGameBadges():
    return 0



