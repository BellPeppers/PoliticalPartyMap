#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

def PoliticalTweetStream(party, searchTerms, state, locationCoordinates, tweetCount):
    access_token = "97325888-4TiheE2EDlLRrRd0i3RyL99uIRMIjqOgMJilVWxsO"
    access_token_secret = "pHpBZnMavx1lTGA1UnS6Uzs6VvLJuwIBP7ExYXqbozoqg"
    consumer_key = "BuAsYJarW7WleTg0PrsvrrF2O"
    consumer_secret = "REOFH6Ue0vewobC1WILncfQrweqPIHc94JTjCBh3iuPhkckYPz"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    class StdOutListener(StreamListener):

        def __init__(self, api=None):
            super(StdOutListener, self).__init__()
            self.num_tweets = 0

        def on_data(self, data):
            #record = {'Text': status.text, 'Created At': status.created_at}
            #print record #See Tweepy documentation to learn how to access other fields
            self.num_tweets += 1
            if self.num_tweets <= tweetCount:
                decoded = json.loads(data)
                fileTitle = state + '_' + party + '_tweets.txt'
                tweet = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
                with open(fileTitle, 'a+') as f:
                    f.write(tweet + '\n')
                return True
            else:
                return False

        def on_error(self, status):
            print 'Error on status', status

        def on_limit(self, status):
            print 'Limit threshold exceeded', status

        def on_timeout(self, status):
            print 'Stream disconnected; continuing...'


    stream = Stream(auth, StdOutListener())
    stream.filter(track=searchTerms, locations = locationCoordinates) #looking at New York City atm

def main():

    # number of tweets per state
    tweetCt = 5

    # open file with state info and save into array

    file = open("states.txt")
    states = file.readlines()
    file.close()

    # run stream for each state based on array

    for x in range (0, len(states)):
        states[x] = states[x].strip()
        if x%5 == 0:
            state = states[x]
        if x%5 == 1:
            lat1 = float(states[x])
        if x%5 == 2:
            long1 = float(states[x])
        if x%5 == 3:
            lat2 = float(states[x])
        if x%5 == 4:
            long2 = float(states[x])
            locationCoord = [long1,lat1,long2,lat2]

            # run stream after the data for each state has been collected for the array
            #republican run
            PoliticalTweetStream('republican', ['republican', 'Jeb Bush', 'Donald Trump'], state, locationCoord, tweetCt)
            #democrat run
            PoliticalTweetStream('democrat', ['democrat', 'Hilary Clinton', 'Bernie Sanders'], state, locationCoord, tweetCt)

main()
