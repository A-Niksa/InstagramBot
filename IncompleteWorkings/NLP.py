# ---------------------------------------------------------------------------- #
#                    sentimental natural language processing                   #
# ---------------------------------------------------------------------------- #

# ----------------------- importing necessary libraries ---------------------- #
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from random import randint
import subprocess

# -------------------------- reading from json file -------------------------- #
with open("info.json", "r") as jFile:
    informationDict = json.loads(jFile.read())

# -------------- getting lists of positive and negative messages ------------- #
messages = informationDict["messages"]
positiveMessages = messages["positive"]
positiveMessagesIndex = randint(0, 9)
negativeMessages = messages["negative"]
negativeMessagesIndex = randint(0,9)

# ------------------- getting captions of the last 10 posts ------------------ #
subprocess.call("CaptionSearch.py", shell = True)


# ---------------------------- sentiment analysis ---------------------------- #
darthVader = SentimentIntensityAnalyzer()
sentimentScores = []
sentimentResults = []
for post in p:
    sentimentDictionary = darthVader.polarity_scores(post)
    if sentimentDictionary['compound'] >= 0.05:
        sentimentResults.append("Positive")
    elif sentimentDictionary['compound'] <= 0.05:
        sentimentResults.append("Negative")
    else:
        sentimentResults.append("Neutral")

