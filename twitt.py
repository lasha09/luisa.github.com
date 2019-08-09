import json

tweetFile = open("../TwitterData/tweets_small.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("tweet id: ", tweetData[0]["id"])

print("tweet text: ", tweetData[0]["text"])

for tweet in tweetData:
    print("tweet text: " + tweet["text"])
#
# for index in range(len(tweetData)):
#     print("tweet text: " + tweetData[index]["text"])
