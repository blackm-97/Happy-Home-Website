#Adds more info into the game data for the frontend to use
def createBadgeList(gameData, userBadges, databaseBadges):

    #Create dictionary of badge Id -> award date

    badgeDictionary = {}
    for data in userBadges:
        badgeDictionary[data['badgeId']] = data['awardedDate']

    sections = ["Main Hub", "Dream Island", "Depths of Void", "Arena", "Milestones", "Special", "Tom Cinematic Universe", "Kool Game Corner", "Collab", "Extra"]
    breakpoints = [19361395, 2124783685, 36731175871168, 2124980594, 2124943412, 2124827611, 2145442036, 2124801414, 3765062370657717, 2124493093]
    res = []

    index = 0
  
    currDict = {} #{name->sectionName, bagdes->[list of badges]}
    #For each badge, we add it to once of the sections above. We figure out which section based on the badge breakpoint
    for badge in databaseBadges:
        if index < len(breakpoints) and badge.id == breakpoints[index]:
            if currDict:
                res.append(currDict)
                currDict = {}

            currDict['sectionName'] = sections[index]
            currDict['badges'] = []
            index += 1

        badge.difficultyVal = getDifficultyFromNum(badge.difficultyVal)

        value = badgeDictionary.get(badge.id, None)

        if value:
            badge.collected = True
            badge.awardedDate = value[0:10]

        currDict['badges'].append(badge)

    if currDict:
        res.append(currDict)

    return res

def getDifficultyFromNum(num) -> str:
    match num:
        case 1:
            return "Freebee"
        case 2:
            return "Easy"
        case 3:
            return "Intermediate"
        case 4:
            return "Difficult"
        case 5:
            return "Intense"
        case 6:
            return "Soul-Melter"
        case 7:
            return "Nonsensical"
        case 10:
            return "Special"
        case _:
            return "Undefined"
