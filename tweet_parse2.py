from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

with open("twitter_data2.txt") as f:
    for line in f:
        try:
            myText = line
            response = alchemyapi.sentiment("text", myText)
            print "Sentiment: "
            print response["docSentiment"]["type"]
        except:
            continue
