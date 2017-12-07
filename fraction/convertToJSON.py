import json


def generateAttendance():
	print("\nInfo: generating original fraction file and attendance file")
	originalFraction = {}
	attendanceAuthorization = {}
	with open('fraction.csv') as inputFile:
		for line in inputFile:
			unit, fraction = line.split(',')
			unit = unit.replace("\"","").replace(" ","")
			fraction = fraction.replace("\"","").replace("\n","")

			originalFraction[int(unit)] = float(fraction)
			attendanceAuthorization[int(unit)] = 0

	#output the original fraction to a file
	with open('originalFraction.json', 'w') as outfile:
		json.dump(originalFraction, outfile, sort_keys=True, indent=4)

	# output a new attendance sheet
	with open('attend.json', 'w') as outfile:
		json.dump(attendanceAuthorization, outfile, sort_keys=True, indent=4)

	# output a new attendance sheet
	with open('voteresult.json', 'w') as outfile:
		json.dump({}, outfile, sort_keys=True, indent=4)

	print("Info: generated originalFraction.json, attend.json and voteresult.json\n")
