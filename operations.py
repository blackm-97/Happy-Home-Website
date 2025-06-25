#Adds more info into the game data for the frontend to use
def createBadgeList(gameData, userBadges):
    collectedBadgeLength = len(userBadges)

    #Total badges collected
    numCollected = 0

    #Create dictionary of badge Id -> award date
    badgeDictionary = {}
    for data in userBadges:
        badgeDictionary[data['badgeId']] = data['awardedDate']

    sections = ["Main Hub", "Dream Island", "Depths of Void", "Arena", "Bonus Badges"]
    breakpoints = [19361395, 2124783685, 36731175871168, 2124980594, 2124943412]
    res = []

    index = 0
  
    currDict = {}
    for badge in gameData:
        if index < len(breakpoints) and badge['id'] == breakpoints[index]:
            if currDict:
                res.append(currDict)
                currDict = {}

            currDict['sectionName'] = sections[index]
            currDict['badges'] = []
            index += 1

        badge['collected'] = False
        badge['awardedDate'] = "N/A"

        value = badgeDictionary.get(badge['id'], None)

        if value:
            badge['collected'] = True
            badge['awardedDate'] = value[0:10]
            numCollected += 1

        currDict['badges'].append(badge)


    if currDict:
        res.append(currDict)

    return res