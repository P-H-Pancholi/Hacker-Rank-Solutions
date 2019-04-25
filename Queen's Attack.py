n,k = map(int,input().split())
rQueen,cQueen = map(int,input().split())


#Initialize the Row and Columns for each attack
rTop = -1
cTop = -1
rBottom = -1
cBottom = -1
rRight = -1
cRight = -1
rLeft = -1
cLeft = -1
rTopRight = -1
cTopRight = -1
rBottomRight = -1
cBottomRight = -1
rBottomLeft = -1
cBottomLeft = -1
rTopLeft = -1
cTopLeft = -1

#Get the input for Obstacle

for interation in range(0,k):
	rObstacle, cObstacle = map(int,input().split())

	#calculation for attack to thr
	# TOP
	if (rObstacle < rTop or rTop == -1) and rObstacle > rQueen and cObstacle == cQueen:
		rTop = rObstacle
		cTop = cObstacle
	#TOP RIGHT
	if (rObstacle - rQueen == cObstacle - cQueen and cObstacle > cQueen and rObstacle > rQueen and ((rObstacle < rTopRight and cObstacle < cTopRight) or rTopRight == -1)):
        rTopRight = rObstacle;
        cTopRight = cObstacle;
	#Right
    if((cObstacle < cRight or rRight == -1) and cObstacle > cQueen and rObstacle == rQueen):
        rRight = rObstacle;
        cRight = cObstacle;
    #Bottom Right
    if(rQueen - rObstacle == cObstacle - cQueen and cObstacle > cQueen and rObstacle < rQueen and ((rObstacle > rBottomRight and cObstacle < cBottomRight) or rBottomRight == -1)):
        rBottomRight = rObstacle;
        cBottomRight = cObstacle;
    #Bottom
    if((rObstacle > rBottom or rBottom == -1) and rObstacle < rQueen and cObstacle == cQueen):
        rBottom = rObstacle;
        cBottom = cObstacle;
    #Bottom Left
    if(rQueen - rObstacle == cQueen - cObstacle and cObstacle < cQueen and rObstacle < rQueen and ((rObstacle > rBottomLeft and cObstacle > cBottomLeft) or rBottomLeft == -1)):
        rBottomLeft = rObstacle;
        cBottomLeft = cObstacle;
    #Left
    if((cObstacle > cLeft or rLeft == -1) and cObstacle < cQueen and rObstacle == rQueen):
        rLeft = rObstacle;
        cLeft = cObstacle;
    #Top Left
    if(cQueen - cObstacle == rObstacle - rQueen and cObstacle < cQueen and rObstacle > rQueen and ((rObstacle < rTopLeft and cObstacle > cTopLeft) or rTopLeft == -1)):
        rTopLeft = rObstacle;
        cTopLeft = cObstacle;

#calculation of the totol steps
total_steps = 0

#RIght
total_steps += (cRight - cQueen - 1) if (cRight != -1) else (n - cQueen)
#Left
total_steps += (cQueen - cLeft - 1) if (cLeft != -1) else (cQueen - 1)
#TOP
total_steps += (rTop - rQueen - 1) if (rTop != -1) else (n - rQueen)
#Bottom
total_steps += (rQueen - rBottom - 1) if (rBottom != -1) else (rQueen -1)
#Top RIGHT
total_steps += (cTopRight - cQueen - 1) if (rTopRight != -1) else min(n - cQueen, n - rQueen)
#Top Left
total_steps += (cQueen - cTopLeft -1) if (cTopLeft != -1) else min(cQueen - 1, n - rQueen)
#Bottom RIGHT
total_steps += (cBottomRight - cQueen -1) if (cBottomRight != -1) else min(n - cQueen, rQueen - 1)
#Bottom Left
total_steps += (cQueen - cBottomLeft - 1) if (rBottomLeft != -1) else min(cQueen - 1, rQueen - 1)

print(total_steps)
