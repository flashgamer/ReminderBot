#!/usr/bin/env python
"""Main code body for Twitter Reminder Bot

Twitter Reminder Bot is a TwitterBot that takes in an event and a time and
tweets at the user at the given time reminding them of the event."""

#imports
import tweepy
from secret import *
from wordnik import *


#Information about the app
__author__ = "Jonathan Jiang"
__credits__ = ["Jonathan Jiang"]
__version__ = "1.0.0"
__maintainer__ = "Jonathan Jiang"
__email__ = "jjiang85@gatech.edu"
__status__ = "Development"

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access.token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

##wordnikUrl = 'http://api.wordnik.com/v4'
##wordnikAPI = ''
##client = swagger.ApiClient(wordnikAPI, wordnikUrl)

tweet = "Test tweet"

api.update_status(tweet)
