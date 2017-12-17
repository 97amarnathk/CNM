import numpy as np

def getMList(xList, yList):
	A = np.zeros((len(xList)-2, len(xList)-2))
	B = np.zeros((len(xList)-2, 1))
	MList = []
	MList.append(0)
	for i in range(1, len(xList)-1):
		c0 = (xList[i] - xList[i-1])/6.0
		c1 = (xList[i+1] - xList[i-1])/3.0
		c2 = (xList[i+1] - xList[i])/6.0
		c3 = (1.0*(yList[i+1]-yList[i]))/(xList[i+1]-xList[i]) - (1.0*(yList[i]-yList[i-1]))/(xList[i]-xList[i-1])
		p = i-1
		B[p][0] = c3
		A[p][p] = c1
		if p-1>=0:
			A[p][p-1] = c0
		if p+1<=len(xList)-3:
			A[p][p+1] = c2
		print i, "] ", c0, c1, c2, " || ",c3
	Ainv = np.linalg.inv(A)
	sol = np.dot(Ainv,B)

	for num in sol:
		MList.append(num[0])

	MList.append(0)
	print MList
	return MList

#get s(n) for a given spline s
def getVal(n , xCurr, xPrev, yCurr, yPrev , MCurr, MPrev):
	C = (yPrev/(xCurr - xPrev)) - (MPrev * (xCurr - xPrev)/6.0)
	D = (yCurr/(xCurr - xPrev)) - (MCurr * (xCurr - xPrev)/6.0)
	A = D - C
	B = C*xCurr - D*xPrev
	s = ( (1/6.0) * (MPrev/(xCurr - xPrev)) * (xCurr - n)**3 ) + ( (1/6.0) * (MCurr/(xCurr - xPrev)) * (n - xPrev)**3 ) + (A*n + B)
	return s

def getSplines(xList,yList):
	MList = np.array(getMList(xList,yList))
	# print MList,"got MList "
	ansList = []
	splineRange = []
	for i in range(1, len(xList)):
		r = np.linspace(start = xList[i-1], stop = xList[i], num = 100)
		subList = []
		for n in r:
			subList.append( getVal(n , xList[i], xList[i-1], yList[i], yList[i-1] , MList[i], MList[i-1]))
		ansList = ansList + subList
		splineRange = splineRange + r.tolist()
	return np.array(ansList), np.array(splineRange)
