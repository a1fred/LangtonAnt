#!/usr/bin/python 

import time,os

def cls():
	pass
	os.system(['clear','cls'][os.name == 'nt'])

def printarea(area,ant):
	for x in range(len(area)):
		print "",
		for y in range(len(area[0])):
			if x == ant[0] and y == ant[1]:
				if area[x][y]: print '\b\033[40m'+"X"+'\033[0m',
				else: print '\b\033[1;31m'+"X"+'\033[0m',
			else:
				if area[x][y]: print '\b\033[40m'+"."+'\033[0m',
				else: print '\b\033[1;47m'+"*"+'\033[0m',
		print

def chgoto(cell, goto):
	if cell: # Black. Go +90
		if goto == "up": return "right"
		if goto == "down": return "left"
		if goto == "left": return "up"
		if goto == "right": return "down"
	else: # White. Go -90
		if goto == "up": return "left"
		if goto == "down": return "right"
		if goto == "left": return "down"
		if goto == "right": return "up"


def loop(areay, areax,antx, anty, goto):
	ant=[antx, anty]
	area = list ( list( False for x in range(areax) ) for y in range(areay))
	printarea(area,ant)
	print "Initial area. "+str(areax)+"x"+str(areay)+", ant on "+str(antx)+"x"+str(anty)+"."
	time.sleep(1)

	while True:
		stat='Black - "."; White - "*"'
		goto = chgoto(area[ant[0]][ant[1]], goto)
		area[ant[0]][ant[1]] = bool( area[ant[0]][ant[1]] -1 )

		if goto == "up": ant[1] -= 1
		if goto == "down": ant[1] += 1
		if goto == "left": ant[0] -= 1
		if goto == "right": ant[0] += 1

		stat += ", Go "+goto+"."

		ant[0] = ant[0] % len(area)
		ant[1] = ant[1] % len(area[0]) # outofrange sheld.

		cls()
		print "Langton Ant. a1fred."
		printarea(area, ant)
		print stat

		try: time.sleep(0.5)
		except: return
#		raw_input('')



if __name__ == "__main__":
	print "Langton Ant. a1fred."
	#loop ( area Y, area X, ant X, ant Y, where to move )
	loop(50,150,25,10, "down")

