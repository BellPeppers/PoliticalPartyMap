
from alchemyapi import AlchemyAPI
import os
import json


def main():

	os.chdir(r'/Users/jmyeluri/Desktop/FinalMapAlchemy')
	file = open("states.txt")
	states = file.readlines()
	file.close()

	alchemyapi = AlchemyAPI()

	
	val1 = 0
	val2 = 0
	info = []
	for x in range (0, len(states)):
		states[x] = states[x].strip()
		info.append({'state': states[x], 'dem': val1, 'rep': val2 })




	sentiment = 0

	#democrat
	for z in range(0, 49):
		file = open(states[z] + "_democrat_tweets.txt")
		statesData = file.readlines()
		file.close()
		sentiment = 0
		print(states[z])
		for i in xrange(5):
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
		info[z]['dem'] = sentiment
				#print('positive sentiment score: ', response['docSentiment']['score'])
				
	sentiment1 = 0		

	#republican
	for y in range(0, 49):
		file = open(states[y]+ "_republican_tweets.txt")
		statesData = file.readlines()
		file.close()
		sentiment1 = 0
		print(states[y])
		for j in xrange(5):
			response = alchemyapi.sentiment('text', statesData[j])
			print("")
			if response['status'] == 'OK':
				response['usage'] = ''
				if ('score' in response['docSentiment']):
					if(float(response['docSentiment']['score']) < 0):
						sentiment1 -= 1
					else:
						sentiment1 += 1
			else:
				print('Error in sentiment analysis call: ', response['statusInfo'])
		info[z]['rep'] = sentiment1


	with open('info.txt', 'w') as outfile:
		json.dump(info, outfile)






	#print("counter: " + str(counter))
	#print("Negative: " +  str(sentiment[0]) +  "\nPositive: " + str(sentiment[1]))
	#print("Percentage positive sentiment: " + str((float(sentiment[1])/counter)*100))

























main()