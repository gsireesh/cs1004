#!/usr/bin/env python
import os, sys

# usage: ./send_grades_mutt <assignment_number>

if __name__ == '__main__':

    assignment_name = raw_input("What assignment are you grading? ")

	current_path = os.getcwd()

	grades_folder = "hw"+ sys.argv[1] + "/" ##### wherever the grade reports are

	grade_reports = os.listdir(grades_folder)
	print sys.argv[1] #####pass in assignment #
	for report in grade_reports:

		if ".txt" in report:
			uni = report.replace(".txt", "")
			report = grades_folder + report
			print uni+"\n"
			os.system("mutt -s \"[cs1004] " + assignment_name +"\" -c your-uni@columbia.edu -c cannon@cs.columbia.edu "+uni+"@columbia.edu < "+report)
			print report+" sent! \n"
