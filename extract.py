'''
USAGE
python3 extract.py \
	[ folder that contains assignments ] \
	[ grade report file ] \
	[ start UNI ] \
	[ end UNI ]

Note that the paths can be absolute or relative.
Absolute paths have a leading slash.
Relative paths don't.
'''

import sys 
import os
import shutil
import re


def main():
	if(len(sys.argv) != 5):
		submissionsPath = input('Enter problem set/programming project directory: ')

		# While the path isn't valid
		while not os.path.exists(submissionsPath):
			print('Specified folder does not exist.')
			submissionsPath = input(
				'Enter problem set/programming project directory: ')

		gradeReportPath = input('Enter name of grade report file: ')

		# While the path isn't valid
		while not os.path.exists(gradeReportPath):
			print('Specified folder does not exist. Please use relative path.')
			gradeReportPath = input(
				'Enter problem set/programming project directory: ')

		startUNI = input('Enter first UNI in your group: ')
		endUNI = input('Enter the last UNI in your group: ')

	else:
		submissionsPath = sys.argv[1]
		gradeReportPath = sys.argv[2]
		startUNI = sys.argv[3]
		endUNI = sys.argv[4]

	gradeReport = open(gradeReportPath, 'r').read()

	# RE is customized to Courseworks submission download naming.
	folderRE = re.compile('.*, .*\((?P<uni>.*)\)')

	# Navigate to the submissions path
	os.chdir(submissionsPath)

	# Compile list of matching folders
	folderList = [f for f in os.listdir(submissionsPath) if folderRE.match(f)]

	for folder in folderList:
		uni = folderRE.match(folder).group('uni')
		if uni >= startUNI and uni <= endUNI: 
			os.rename(folder, uni)
			with open(uni+'.txt', 'w') as customGR: 
				customGR.write(gradeReport)
		else: 
			shutil.rmtree(folder)


if __name__ == '__main__':
    main()



