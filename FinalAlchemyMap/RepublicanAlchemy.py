
from alchemyapi import AlchemyAPI
import os
import json


def updateJsonFile():
 os.chdir(r'/Users/jmyeluri/Desktop/FinalMapAlchemy')
 jsonFile = open("info.json", "r")
 info = json.load(jsonFile)
 jsonFile.close()
 return info

def main():

	os.chdir(r'/Users/jmyeluri/Desktop/FinalMapAlchemy')
	file = open("states.txt")
	states = file.readlines()
	file.close()

	alchemyapi = AlchemyAPI()

	
	val1 = 0
	val2 = 0
	
	for x in range (0, len(states)):
		states[x] = states[x].strip()
		#info.append({'state': states[x], 'dem': val1, 'rep': val2 })

	info = updateJsonFile()	
	print(info)

	sentiment = 0

	#republican
	for z in range(0, 50):
		file = open(states[z] + "_republican_tweets.txt")
		statesData = file.readlines()
		file.close()
		sentiment = 0
		print(states[z])
		for i in xrange(15):
			response = alchemyapi.sentiment('text', statesData[i])
			print("")
			if response['status'] == 'OK':
				response['usage'] = ''
				if ('score' in response['docSentiment']):
					if(float(response['docSentiment']['score']) < 0):
						sentiment -= 1
					else:
						sentiment += 1
			else:
				print('Error in sentiment analysis call: ', response['statusInfo'])
		info[z]['rep'] = sentiment
		print(info[z]['rep'])
				#print('positive sentiment score: ', response['docSentiment']['score'])
				
		

	

	jsonFile = open("info.json", "w+")
 	jsonFile.write(json.dumps(info))
 	jsonFile.close()






	#print("counter: " + str(counter))
	#print("Negative: " +  str(sentiment[0]) +  "\nPositive: " + str(sentiment[1]))
	#print("Percentage positive sentiment: " + str((float(sentiment[1])/counter)*100))

























main()