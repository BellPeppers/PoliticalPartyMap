#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
from TwitterAPI import TwitterAPI

CONSUMER_KEY = "blzC40MytkH9HguJYBUcttxxg"
CONSUMER_SECRET = "Mw37mXO7sXUNazbUkUlfsfjSzQCMIXNZXD3wuSmJeQj1tvnm2e"
ACCESS_TOKEN_KEY = "2658435840-MjNaSPPQso4aMFK1C1SgB5S8ISlRSAlQsPLFB74"
ACCESS_TOKEN_SECRET = "iTF4QJcKlu4ZCOJbtbJTTGvO1xHjRSB5JZJCrdTjyJQrB"
api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

SEARCH_TERM = 'Democrat',  'Bernie Sanders'
latitude = 40.758224    # geographical centre of search
longitude = -73.917404   # geographical centre of search
max_range = 1
count = 50
until = "2015-10-07"
lang = 'en'
demo_text = ""
demo_list = []

r = api.request('search/tweets', {'lang': lang, 'q': SEARCH_TERM, 'count': count, })
for item in r: #r is the list of tweets
    demo_list.append(item['text'])
alchemyapi = AlchemyAPI()

sentiment = [0.0,0.0]
geoplace = [0.0,0.0]
#Create sentiment list
#create sentiment counter
counter = 0
#for-loop over
for i in xrange(len(demo_list)):
    response = alchemyapi.sentiment('html', demo_list[i])
    print(demo_text)
    if (response['status'] == 'OK'):
        response['usage'] = ''
        if ('score' in response['docSentiment']):
            if(float(response['docSentiment']['score']) < 0):
                sentiment[0] += 1
            else:
                sentiment[1] += 1
            #print('positive sentiment score: ', response['docSentiment']['score'])
            counter += 1
    else:
        print('Error in sentiment analysis call: ', response['statusInfo'])

print("counter: " + str(counter))
print("Negative: " +  str(sentiment[0]) +  "\nPositive: " + str(sentiment[1]))
print("Percentage positive sentiment: " + str((float(sentiment[1])/counter)*100))

#print output in terms of percentages
