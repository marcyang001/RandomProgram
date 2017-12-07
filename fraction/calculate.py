import sys, json
import pprint

fraction = {
    "101": 0.55, 
    "102": 0.55, 
    "103": 0.66, 
    "105": 0.53, 
    "106": 0.67, 
    "107": 0.64, 
    "109": 0.73, 
    "110": 0.65, 
    "111": 1.1, 
    "112": 0.55, 
    "114": 0.5, 
    "115": 0.48, 
    "201": 0.6, 
    "202": 0.48, 
    "203": 0.49, 
    "204": 0.53, 
    "205": 0.53, 
    "206": 0.68, 
    "207": 0.51, 
    "208": 0.6, 
    "209": 0.72, 
    "210": 0.73, 
    "212": 0.55, 
    "214": 0.5, 
    "215": 0.48, 
    "216": 0.6, 
    "301": 0.61, 
    "302": 0.48, 
    "303": 0.5, 
    "304": 0.53, 
    "305": 0.53, 
    "306": 0.68, 
    "307": 0.51, 
    "308": 0.61, 
    "309": 0.73, 
    "310": 0.66, 
    "311": 0.93, 
    "312": 0.56, 
    "314": 0.5, 
    "315": 0.48, 
    "316": 0.61, 
    "401": 0.62, 
    "402": 0.48, 
    "403": 0.5, 
    "404": 0.54, 
    "405": 0.54, 
    "406": 0.7, 
    "407": 0.52, 
    "408": 0.61, 
    "409": 0.74, 
    "410": 0.67, 
    "411": 0.76, 
    "412": 0.56, 
    "414": 0.51, 
    "415": 0.49, 
    "416": 0.62, 
    "501": 0.73, 
    "502": 0.69, 
    "503": 0.78, 
    "504": 0.84, 
    "505": 1.08, 
    "506": 0.84, 
    "507": 1.11, 
    "508": 0.82, 
    "509": 0.8, 
    "510": 0.74, 
    "511": 0.72, 
    "601": 0.74, 
    "602": 0.7, 
    "603": 0.79, 
    "604": 0.84, 
    "605": 1.09, 
    "606": 0.83, 
    "607": 1.11, 
    "608": 0.82, 
    "609": 0.81, 
    "610": 0.75, 
    "611": 0.73, 
    "701": 0.75, 
    "702": 0.71, 
    "703": 0.8, 
    "704": 0.84, 
    "705": 1.09, 
    "706": 0.84, 
    "707": 1.12, 
    "708": 0.83, 
    "709": 0.81, 
    "710": 0.76, 
    "711": 0.74, 
    "801": 0.76, 
    "802": 0.72, 
    "803": 0.81, 
    "804": 0.86, 
    "805": 1.11, 
    "806": 0.86, 
    "807": 1.13, 
    "808": 0.84, 
    "809": 0.83, 
    "810": 0.77, 
    "811": 0.75, 
    "901": 0.77, 
    "902": 0.73, 
    "903": 0.82, 
    "904": 0.87, 
    "905": 1.12, 
    "906": 0.86, 
    "907": 1.15, 
    "908": 0.85, 
    "909": 0.84, 
    "910": 0.78, 
    "911": 0.76, 
    "1001": 0.79, 
    "1002": 0.97, 
    "1003": 0.75, 
    "1004": 1.28, 
    "1005": 0.88, 
    "1006": 1.31, 
    "1007": 0.82, 
    "1008": 1.02, 
    "1009": 0.76, 
    "1101": 0.83, 
    "1102": 1.01, 
    "1103": 0.78, 
    "1104": 1.16, 
    "1105": 0.78, 
    "1106": 1.64, 
    "1107": 0.86, 
    "1108": 1.06, 
    "1109": 0.8
}



if len(sys.argv) < 3:
	
	print("ERROR: no input file")
	sys.exit()


attendanceFile = sys.argv[1]

votingResultFile = sys.argv[2]


def updateFraction(inputFile):
    with open (inputFile) as file:
        json_data = json.load(file)
        for ownerUnit, representative in json_data.items():
            if int(representative) != 0:
                if str(ownerUnit) in fraction and str(representative) in fraction:
                    if str(ownerUnit) != str(representative):
                        # update the fraction of the represetative 
                        fraction[str(representative)] += fraction[str(ownerUnit)]
                        # set the fraction of the absent owner to zero
                        fraction[str(ownerUnit)] = 0
                else:
                    print("either # ", ownerUnit, " or # ", representative, " is invalid")
                    return
            else:
                # forfeit owner
                fraction[ownerUnit] = 0


def calculateFraction(inputFile):

    with open (inputFile) as file:
        json_data = json.load(file)
        electedCandiates = {}
        for voterUnit, candidates in json_data.items():
            #voter unit is valid
            if voterUnit in fraction:
                for candidateUnit in set(candidates):
                    #candidate is a valid number
                    if str(candidateUnit) in fraction:
                        if candidateUnit in electedCandiates:
                            electedCandiates[candidateUnit] += fraction[voterUnit]
                        else:
                            electedCandiates[candidateUnit] = fraction[voterUnit]
                    else:
                        print("the candidate unit # ", candidateUnit, " is not valid, voted by # ", voterUnit)
                        return
            else:
                print("the voter unit # ", voterUnit, " is not valid")
                return

    file.close()
    print ("\n\n Elected | Total Votes")
    print("=======================================\n")

    for candidate, totalFraction in sorted(electedCandiates.items(), reverse=True, key=lambda k: (k[1],k[0])):
        print (candidate, "    |    ", totalFraction)



updateFraction(attendanceFile)
calculateFraction(votingResultFile)








