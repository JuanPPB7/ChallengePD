import numpy as np
from numpy import random as rd

global rooms

def lis(list_garb):
	n = len(list_garb)
	cont = 0
	global rooms
	rooms = []
	lis = [1]*n

	"""if n == 1:
		return rooms[0]"""

	for i in range (1, n):
		for j in range(0, i):
			if list_garb[i] > list_garb[j] and lis[i]< lis[j] + 1 :
				lis[i] = lis[j]+1
				#rooms[cont] = list_garb[j]
				#cont = cont + 1

	maximum = 0
	#print (rooms)

	for i in range(n):
		maximum = max(maximum, lis[i])

	return maximum

#list_garb = rd.randint(0,100,(1,100))
list_garb = [57, 889, 546, 867, 587, 34]
print (lis(list_garb))
print (list_garb)
#print (rooms)
