# Usability Tester for Mini Mouse Macro files

import math

# Reading log lines from file
logFile = open('asdas.mmmacro','r')
logLines = logFile.readlines()
logFile.close()

# Spliting log lines into columns
logData = []
for line in logLines:
    logData.append(line.rstrip().split('|',5))

# Number of clicks
nc = 0
for logEntry in logData:
	if logEntry[4] == " Clique esquerdo para baixo":
		nc = nc + 1

print ("Número de clicks: " + str(nc))

# Task time
tt = 0
for logEntry in logData:
	tt = tt + int(logEntry[3])

print ("Tempo da tarefa: " + str(tt) + " ms")

# Mean wait time between clicks
print ("Tempo médio de espera entre cliques: " + str(tt/nc) + " ms")

# Mouse distance covered
md = 0
p1 = (800,800)
for logEntry in logData:
	if logEntry[4] == " Movimento do Mouse":
		p2 = (int(logEntry[1]),int(logEntry[2]))
		md = md + math.hypot(p2[0] - p1[0], p2[1] - p1[1])
		p1 = p2

print ("Distância do mouse coberta: " + str(int(md)))


