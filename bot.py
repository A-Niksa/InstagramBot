# ---------------------------------------------------------------------------- #
#                             instagram bot backend                            #
# ---------------------------------------------------------------------------- #

# ----------------- importing necessary modules and packages ----------------- #
import json
from time import sleep
from instapy import InstaPy
from random import randint

# -------------------------- reading from json file -------------------------- #
with open("info.json", "r") as jFile:
    informationDict = json.loads(jFile.read())

# ------------------------- getting user information ------------------------- #
botDict = informationDict["botinfo"]
username = botDict["username"]
password = botDict["password"]

# -------------------------- getting input usernames ------------------------- #
inputUsernames = informationDict["usernames"]

# -------------- getting lists of positive and negative messages ------------- #
messages = informationDict["messages"]
positiveMessages = messages["positive"]
positiveMessagesIndex = randint(0, 9)
negativeMessages = messages["negative"]
negativeMessagesIndex = randint(0,9)


# ---------------------- creating session and logging in --------------------- #
session = InstaPy(username = username, password = password)
session.login()

# ----------------------- following the input usernames ---------------------- #
session.follow_by_list(inputUsernames, times = 1, sleep_delay = 600)
sleep(5)

# --------------------- grabbing followers and followings -------------------- #
followData = dict()
for user in inputUsernames:
    followers = session.grab_followers(username = user, amount = "full")
    #print(followers)
    #followers = [follower for follower in followers]
    numberOfFollowers = len(followers)
    followings = session.grab_following(username = user, amount = "full")
    #followings = [following for following in followings]
    followData[user] = {"number of followers": numberOfFollowers,
     "followers": followers, 
     "followings": followings}

# ------------- exporting followers and followings to a json file ------------ #
with open("followdata.json", "w") as jFile:
    json.dump(followData, jFile, indent = 4)

# ----------------------- replying to positive comments ---------------------- #
session.set_use_meaningcloud(enabled = True,
                            license_key = "5473a8083d457bdf7e4f75d0b1f5bf03",
                            polarity = "P",
                            agreement = "AGREEMENT",
                            subjectivity = "SUBJECTIVE",
                            confidence = 90)
session.set_do_comment(enabled = True, percentage = 25)
session.set_comment_replies(replies = [positiveMessages[positiveMessagesIndex]], media = None)
session.interact_by_comments(usernames = inputUsernames,
                            posts_amount = 1,
                            comments_per_post = 5,
                            reply = True,
                            interact = True,
                            randomize = True,
                            media = None)

# ----------------------- replying to negative comments ---------------------- #
session.set_use_meaningcloud(enabled = True,
                            license_key = "5473a8083d457bdf7e4f75d0b1f5bf03",
                            polarity = "N",
                            agreement = "AGREEMENT",
                            subjectivity = "SUBJECTIVE",
                            confidence = 90)
session.set_do_comment(enabled = True, percentage = 25)
session.set_comment_replies(replies = [negativeMessages[negativeMessagesIndex]], media = None)
session.interact_by_comments(usernames = inputUsernames,
                            posts_amount = 1,
                            comments_per_post = 5,
                            reply = True,
                            interact = True,
                            randomize = True,
                            media = None)

# ----------------------- replying to neutral comments ----------------------- #
session.set_use_meaningcloud(enabled = True,
                            license_key = "5473a8083d457bdf7e4f75d0b1f5bf03",
                            polarity = "P",
                            agreement = "AGREEMENT",
                            subjectivity = "SUBJECTIVE",
                            confidence = 90)
session.set_do_comment(enabled = True, percentage = 25)
messagesList = [positiveMessages, negativeMessages]
positivityIndex = randint(0, 1)
messageIndex = randint(0, 9)
session.set_comment_replies(replies = [messagesList[positivityIndex][messageIndex]], media = None)
session.interact_by_comments(usernames = inputUsernames,
                            posts_amount = 1,
                            comments_per_post = 5,
                            reply = True,
                            interact = True,
                            randomize = True,
                            media = None)

# --------------------------- liking and commenting -------------------------- #
session.set_comments([positiveMessages[positiveMessagesIndex]])
session.set_do_like(enabled = True, percentage = 100)
session.set_do_comment(enabled = True, percentage = 20)
session.interact_by_users(inputUsernames, media = None)

# ------------------------------ ending session ------------------------------ #
session.end()