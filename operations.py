#Adds more info into the game data for the frontend to use
def createBadgeList(gameData, userBadges):
    collectedBadgeLength = len(userBadges)
    i = 0

    #Create dictionary of badge Id -> award date
    badgeDictionary = {}
    for data in userBadges:
        badgeDictionary[data['badgeId']] = data['awardedDate']

    for badge in gameData:
        badge['collected'] = False
        badge['awardedDate'] = "N/A"

        value = badgeDictionary.get(badge['id'], None)

        if value:
            badge['collected'] = True
            badge['awardedDate'] = value[0:9]
            i += 1

    return gameData