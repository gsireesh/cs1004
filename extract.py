'''
USAGE : extract.py [ folder that contains assignments ] [ grade report file ]
'''

import sys 
import os
import subprocess
import re



pwd = os.getcwd()

if(len(sys.argv) != 3):
	relPath = input('Enter problem set/programming project directory:')
	gradeReportPath = input('Enter name of grade report file:')
else:
	relPath = sys.argv[1]
	gradeReportPath = sys.argv[2]

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
	os.rename(f, uni)
	with open(uni+'.txt', 'w') as customGR: 
		customGR.write(gradeReport)




