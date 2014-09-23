'''
USAGE : extract.py [ folder that contains assignments ] [ grade report file ]
[ start UNI ] [ end UNI ]
'''

import sys 
import os
import shutil
import re



pwd = os.getcwd()

if(len(sys.argv) != 5):
	relPath = input('Enter problem set/programming project directory: ')
	gradeReportPath = input('Enter name of grade report file: ')
	startUNI = input('Enter first UNI in your group: ')
	endUNI = input('Enter the last UNI in your group: ')
else:
	relPath = sys.argv[1]
	gradeReportPath = sys.argv[2]
	startUNI = sys.argv[3]
	endUNI = sys.argv[4]

gradeReport = open(gradeReportPath, 'r').read()

folderRE = re.compile('.*, .*\((?P<uni>.*)\)')

folder = pwd+'/'+relPath

if not os.path.exists(folder):
	print('Specified folder does not exist!')
	sys.exit(1)


os.chdir(folder)

folderList = [f for f in os.listdir(folder) if folderRE.match(f)]


for f in folderList:
	uni = folderRE.match(f).group('uni')
	if uni >= startUNI and uni <= endUNI: 
		os.rename(f, uni)
		with open(uni+'.txt', 'w') as customGR: 
			customGR.write(gradeReport)
	else: 
		shutil.rmtree(f)






