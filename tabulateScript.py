import os
import re
import math

filesList = [f for f in os.listdir(os.getcwd()) if not os.path.isdir(f) and \
(f.split('.')[1] == 'txt') and re.match('\D+\d{4}',f,0)]
filesList.sort()
scoreTable = open('tabulatedScores.txt','w')
stringofScores = []
stats = []

for f in filesList:
    temp = open(f,'r')
    print(f)
    score = re.search('(\d+.?\d)/\d+.?\d',temp.readlines()[3],0).group(1)
    stringofScores.append(f.split('.')[0]+'\t\t'+score)
    stats.append(score)
    temp.close()


uniLast = re.compile('\D+(\D)\d{4}')
stringofScores = sorted(stringofScores, key=lambda score: re.match(uniLast, score, 0).group(1))

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

