import os
def main():

	os.chdir(r'/Users/jmyeluri/Desktop/FinalMapAlchemy')
	file = open("states.txt")
	states = file.readlines()
	file.close()

	#alchemyapi = AlchemyAPI()

	
	val1 = 0
	val2 = 0
	info = []
	for x in range (0, len(states)):
		states[x] = states[x].strip()
		print(states[x])
		info.append({'state': states[x], 'dem': val1, 'rep': val2 })

main()