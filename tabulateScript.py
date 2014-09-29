import os
import re
import math

LINEWITHTOTAL = 1

folder = raw_input("Enter the path of the folder containing grade reports, or enter 0 to use the current directory:")
currentDir = False
if folder == "0":
    currentDir = True
    folder = os.getcwd()
if folder[-1]!='/':
    folder+= '/'
print os.listdir(folder)
filesList = [f for f in os.listdir(folder) if not os.path.isdir(f) and \
(len(f.split('.'))>1 and f.split('.')[1] == 'txt') and re.match('\D{2,3}\d{4}',f,0)]
filesList.sort()
scoreTable = open(folder+'tabulatedScores.txt','w')
stringofScores = []
stats = []

for f in filesList:
    report = f
    if not currentDir:
        report = folder + f
    temp = open(report,'r')
    print(f)
    score = re.search('(\d+.?\d)/\d+.?\d',temp.readlines()[LINEWITHTOTAL],0).group(1)
    stringofScores.append(f.split('.')[0]+'\t\t'+score)
    stats.append(score)
    temp.close()


uniLast = re.compile('\D+(\D)\d{4}')
stringofScores = sorted(stringofScores, key=lambda score: re.match(uniLast, score, 0).group(1))
print stringofScores

for s in stringofScores:
    scoreTable.write(s)
    scoreTable.write('\n')

scoreTable.write('\n\n')


stats = [float(f) for f in stats]
print(stats)
stats.sort()
sumx = sum(stats)
mean = sumx/len(stats)
stddev = math.sqrt(sum([(x-mean)*(x-mean) for x in stats])/len(stats))
if(len(stats)%2 == 1):
	median = stats[int((len(stats)+1)/2)]
else:
	median = stats[len(stats)/2]
maxVal = stats[-1]
minVal = stats[0]


scoreTable.write('Mean:')
scoreTable.write(str(mean))
scoreTable.write('\nStddev:')
scoreTable.write(str(stddev))
scoreTable.write('\nMedian:')
scoreTable.write(str(median))
scoreTable.write('\nMax:')
scoreTable.write(str(maxVal))
scoreTable.write('\nMin:')
scoreTable.write(str(minVal))

scoreTable.close()

