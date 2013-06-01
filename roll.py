import random
import os

def cls():
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )

def getAllPossibilities(ndice):
	possibilities = []
	if ndice == 2:
		for i in range(6):
			for j in range(6):
				possibilities.append(i+j+2)
	possibilities.sort()
	return possibilities
	#for i in range(ncice):
	#	for side in range(6):

def roll(possibilities):
	index = random.randint(0, len(possibilities)-1)
	return possibilities.pop(index)

if __name__ == "__main__":
	ndice = 2

	fairnessrange = raw_input("Be fair for every n*36 rolls [default=1]: ")
	pos = getAllPossibilities(2) * int(fairnessrange)
	players = []

	while True:
		pname = raw_input("Please enter a player name: ")
		if not pname:
			break
		players.append(pname)

	n = 0
	cls()
	while True:
		try:
			import sys
			#sys.stdout.write("\r")

			player = players[n % len(players)]
			sys.stdout.write("%s:" % player)
			raw_input()
			#print "\r"
			cls()
			

			if not len(pos):
				pos = getAllPossibilities(2)

			print (player + ":").ljust(15), roll(pos)

			n+=1
			#print pos
		except KeyboardInterrupt:
			break