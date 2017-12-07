import json


originalFraction = {}
attendanceAuthorization = {}
with open('fraction.csv') as inputFile:
	for line in inputFile:
		unit, fraction = line.split(',')
		unit = unit.replace("\"","").replace(" ","")
		fraction = fraction.replace("\"","").replace("\n","")

		originalFraction[int(unit)] = float(fraction)
		attendanceAuthorization[int(unit)] = 0


with open('originalFraction.json', 'w') as outfile:
	json.dump(originalFraction, outfile, sort_keys=True, indent=4)


with open('attend.json', 'w') as outfile:
	json.dump(attendanceAuthorization, outfile, sort_keys=True, indent=4)

