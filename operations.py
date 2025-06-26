#Adds more info into the game data for the frontend to use
def createBadgeList(gameData, userBadges, databaseBadges, nonCanonBadges):
    collectedBadgeLength = len(userBadges)

    #Total badges collected
    numCollected = 0

    #Create dictionary of badge Id -> award date
    badgeDictionary = {}
    for data in userBadges:
        badgeDictionary[data['badgeId']] = data['awardedDate']

    sections = ["Main Hub", "Dream Island", "Depths of Void", "Arena", "Milestones", "Tom Cinematic Universe", "Kool Game Corner", "Extra"]
    breakpoints = [19361395, 2124783685, 36731175871168, 2124980594, 2124943412, 2145442036, 2124801414, 2124493093]
    res = []

    index = 0
    for badges in nonCanonBadges:
        gameData.append(badges)
  
    currDict = {} #{name->sectionName, bagdes->[list of badges]}
    #For each badge, we add it to once of the sections above. We figure out which section based on the badge breakpoint
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