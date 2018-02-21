#!/usr/bin/env python

from twython import Twython, TwythonError
import time
import random
from random import randint
from random import shuffle
from time import sleep
import config

twitter = Twython(config.APP_KEY, config.APP_SECRET, config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET)

#Add in some search queries from the config file
filter = " OR ".join(config.query)
blacklist = " -".join(config.ignore)
keywords = filter + blacklist

# The search queries above will loop using the count below
search_results = twitter.search(q=keywords)
try:
    for tweet in search_results["statuses"]:
        try:
            def retweet():
                twitter.retweet(id = tweet["id_str"])
                print ('Retweeted Tweet')
            def like():
                twitter.create_favorite(id = tweet["id_str"])
                print ('Liked Tweet')
            def follow():
                st=tweet["entities"]["user_mentions"]
                if st != []:
                    twitter.create_friendship(screen_name=st[0]["screen_name"])
                    print ('Followed User')

            # A randomizer was requested by someone on Github

            functions = [follow, like, retweet]
            shuffle(functions)

            for func in functions:
                func()

            # Adding a randomized sleep

            random.getstate()

            for i in xrange(1):
                n = random.randint(int(config.Min_time), int(config.Max_time))
                print "\nSleeping for " + str(n), "seconds \n"
                time.sleep(n)


        except TwythonError as e:
            print e

except TwythonError as e:
    print e

