import json

# importing textblob file from textblob to retrieve tweetsmall json file
from textblob import TextBlob

# import numpy as np
import matplotlib.pyplot as plt
#
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
#
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()


import matplotlib.pyplot as plt
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# creating 2 list
polarityList = []
subjectivityList = []

# adding polarity and subjectivity into their lists
for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarityList.append(tweetblob.polarity)
    subjectivityList.append(tweetblob.subjectivity)

# code for average of polarity and subjectivity lists
print(polarityList[0])
print(subjectivityList[0])

# set the 2 lists
print()
print("Polarity List")
print(polarityList)
print()
print("Subjectivity List")
print(subjectivityList)

# matplotlib code
plt.hist(polarityList, bins=[-1.1, -.75, -.5, -.25, 0, .25, .5, .75, 1.1])

# x and y labels for the Histogram for polarity
plt.xlabel('polarities')
plt.ylabel('number of tweets')

#main tile of tweet polarity
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])

# set the histogram to graph and show
plt.grid(True)
plt.show()


# subjectivity code for histogram
plt.hist(subjectivityList, bins=[-1.1, -.75, -.5, -.25, 0, .25, .5, .75, 1.1])

plt.xlabel('subjectivity')
plt.ylabel('number of tweets')

plt.title('Histogram of Tweet Subjectivity')
plt.axis([-1.1, 1.1, 0, 100])

plt.grid(True)
plt.show()

# the polarity vs the subjectivity lists
plt.plot(polarityList, subjectivityList, 'ro')
plt.xlabel('polarity')
plt.ylabel('subjectivity')
plt.title('tweet polarity vs. subjectivity')
plt.axis([-1.1, 1.1, 0.1, 1.1])
plt.grid(True)
plt.show()
