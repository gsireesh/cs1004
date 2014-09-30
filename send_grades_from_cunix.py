#### run in cunix
#### run from outside the hw# directory, pass in assignment #
#### replace text Programming Project with Problem Set if necessary

import os, sys

if __name__ == '__main__':


	current_path = os.getcwd()

	grades_folder = "hw" + sys.argv[1] + "/" ##### put grade reports in hw1, hw2 etc.

	grade_reports = os.listdir(grades_folder)
	print sys.argv[1] ##### pass in assignment #
	for report in grade_reports:

		if ".txt" in report:
			uni = report.replace(".txt", "")
			report = grades_folder + report
			print uni+"\n"
			os.system("mutt -s \"[cs1004] Programming Project "+str(sys.argv[1])+"\" -c your-uni@columbia.edu -c cannon@cs.columbia.edu "+uni+"@columbia.edu < "+report)
			print report+" sent! \n"
