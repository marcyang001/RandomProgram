import sys, json
import pprint, argparse
import convertToJSON

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


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--attendance", help="file that keeps track of attendance",
                    action="store")
parser.add_argument("-v", "--voteresult", help="file that keeps track of the vote result",
                    action="store")
parser.add_argument("-g", "--generate", help="generate a new attendance sheet",
                    action="store_true")
parser.add_argument("-of", "--outputfraction", help="generate a new attendance sheet",
                    action="store_true")

args = parser.parse_args()


def updateFraction(inputFile):
    print()
    with open (inputFile) as file:
        try:
            attendanceSheet = json.load(file)
        except json.decoder.JSONDecodeError:
            print("ERROR: invalid json attendance result file")
            sys.exit()

        for ownerUnit, representative in attendanceSheet.items():
            if int(representative) != 0:
                if str(ownerUnit) in fraction and str(representative) in fraction:
                    if str(ownerUnit) != str(representative):
                        # check if the representative itself is present
                        if attendanceSheet[str(representative)] != 0:
                            # update the fraction of the represetative 
                            fraction[str(representative)] += fraction[str(ownerUnit)]
                            # set the fraction of the absent owner to zero
                            fraction[str(ownerUnit)] = 0
                        else:
                            print("ERROR: the representative # ", representative, " is absent. Check the attendance again")
                            sys.exit()
                else:
                    print("ERROR: either # ", ownerUnit, " or # ", representative, " is invalid")
                    sys.exit()
            else:
                # forfeit owner
                fraction[ownerUnit] = 0

def totalAttendanceRate(fractionChart):
    print()
    totalFraction = 0
    for ownerUnit, unitFraction in fractionChart.items():
        totalFraction += unitFraction

    if totalFraction < 50:
        print ("CAUTON: total fraction less than 50%, not enough to vote!")
    print("Info: total fraction vote: ", totalFraction)
    return totalFraction

def outputFractionOFEachVoter(fractionChart):

    totalFraction = 0
    print("\nVoting Right for each voter ")
    print("=============================")
    for ownerUnit, unitFraction in fractionChart.items():
        if unitFraction != 0:
            print(ownerUnit, " : ", unitFraction)


def calculateFraction(inputFile):
    print()
    with open (inputFile) as file:
        try:
            json_data = json.load(file)
        except json.decoder.JSONDecodeError:
            print("ERROR: invalid json vote result file")
            return
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
                        print("ERROR: the candidate unit # ", candidateUnit, " is not valid, voted by # ", voterUnit)
                        return
            else:
                print("ERROR: the voter unit # ", voterUnit, " is not valid")
                return

    file.close()
    print ("\n\nElected | Total Votes")
    print("===============================")

    for candidate, totalFraction in sorted(electedCandiates.items(), reverse=True, key=lambda k: (k[1],k[0])):
        if candidate < 1000:
            print (candidate, "    |    ", totalFraction)
        else:
            print (candidate, "   |    ", totalFraction)

    print()

if args.generate:
    convertToJSON.generateAttendance()
    sys.exit()

elif args.attendance == None and args.voteresult == None:
    print("\nERROR: missing required file input: attend.json or voteresult.json")
    sys.exit()


attendanceFile = args.attendance

votingResultFile = args.voteresult

if attendanceFile != None:
    updateFraction(attendanceFile)

if args.outputfraction:
    outputFractionOFEachVoter(fraction)

if votingResultFile != None:
    calculateFraction(votingResultFile)








