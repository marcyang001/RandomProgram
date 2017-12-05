import subprocess, time
import argparse


##########################################
"""
Script to automatically shutdown an application after a certain time

Two important variables:
	1. processName: the name of the application which the user wants to turn off
	2. totalSecond: the time after which the application will shutdown

"""



processName = "FaceTime"
totalSecond = 60


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--process", help="proces name which you want to shutdown",
                    action="store")
parser.add_argument("-s", "--second", help="the time in seconds after which the application will shutdown",
                    action="store")
parser.add_argument("-u", "--password", help="[optional] super-user password for making the computer sleep",
                    action="store")
args = parser.parse_args()

password = args.password

if args.process != None:
	processName = args.process

if args.second != None:
	totalSecond = int(args.second)



##########################################


def get_pid(name):
	ps = subprocess.Popen(('ps', '-ax'), stdout=subprocess.PIPE)
	output = subprocess.check_output(('grep', name), stdin=ps.stdout)
	ps.wait()

	pid = 999999
	try:
		pid = int(output.split("\n")[0].split()[0])
	except ValueError:
		print "Oops!  That was no valid number.  Try again..."

	return pid

#processName by Default is FaceTime
def killProcess(processName):

	pid = str(get_pid(processName))
	
	try:
		output = subprocess.check_output(('kill', '-9', pid))
	except Exception:
		output = "no process"

	return output

def letPCSleep(password):

	if password != None:
		ps = subprocess.Popen(("echo", password), stdout=subprocess.PIPE)
		output = subprocess.check_output(['sudo', 'shutdown', '-s', '+1'], stdin=ps.stdout)
		ps.wait()




# Loop until totalSecond is 0
while totalSecond != 0:
	print ">>>>>>>>>>>>>>>>>>>>>", totalSecond, " second(s)"
	# Sleep for a second
	time.sleep(1)
	# Increment the minute total
	totalSecond -= 1

killProcess(processName)
letPCSleep(password)



