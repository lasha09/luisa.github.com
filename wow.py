import json

from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetSearch = "automation"

tweetFile = open('../TwitterData/automation_tweets_large.json', "r")
tweetData = json.load(tweetFile)
tweetFile.close()

combinedTweets = ""
for tweet in tweetData:
    combinedTweets += tweet['text']

tweetblob = TextBlob (combinedTweets)

wordsToFilter = [ "about", "https", "in", "the", "thing", "will", "could", "would", "because", "colors", "i", "and", "find", "you", "your","do", "to", "is", "for", "ai", "iot","no","our","have","of","but","can","with","by","at","home","this","it","on","that","from", tweetSearch]
filteredDictionary = dict()

for word in tweetblob.words:
    if len(word) < 2:
        continue
    if not word.isalpha():
        continue
    if word.lower() in wordsToFilter:
        continue
    if len(word) < 5 and word.upper() !=word:
        continue;

    filteredDictionary[word.lower()] = tweetblob.word_counts[word.lower()]

wordcloud =WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation= "bilinear")
plt.axis("off")
plt.show()
