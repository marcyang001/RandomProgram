import subprocess, time

##########################################
"""
Script to automatically shutdown an application after a certain time

Two important variables:
	1. processName: the name of the application which the user wants to turn off
	2. totalSecond: the time after which the application will shutdown

"""



processName = "Chrome"
totalSecond = 60


##########################################


def get_pid(name):
	ps = subprocess.Popen(('ps', '-ax'), stdout=subprocess.PIPE)
	output = subprocess.check_output(('grep', name), stdin=ps.stdout)
	ps.wait()

	pid = -1
	try:
		pid = int(output.split("\n")[0].split()[0])
	except ValueError:
		print "Oops!  That was no valid number.  Try again..."

	return pid

#processName by Default is FaceTime
def killFaceTime(processName):

	pid = str(get_pid(processName))
	output = subprocess.check_output(('kill', '-9', pid))
	return output



# Loop until totalSecond is 0
while totalSecond != 0:
	print ">>>>>>>>>>>>>>>>>>>>>", totalSecond, " second(s)"
	# Sleep for a second
	time.sleep(1)
	# Increment the minute total
	totalSecond -= 1

killFaceTime(processName)




