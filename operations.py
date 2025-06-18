#Adds more info into the game data for the frontend to use
def createBadgeList(gameData, userBadges):
    collectedBadgeLength = len(userBadges)
    i = 0

    for badge in gameData:
        badge['collected'] = False
        badge['awardedDate'] = "N/A"
        if i < collectedBadgeLength and (userBadges[i].get('badgeId', None) == badge['id']):
            badge['collected'] = True
            badge['awardedDate'] = userBadges[i].get('awardedDate',"Error")
            i += 1

    return gameData