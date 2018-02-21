# Twittercompbot


I wrote this small bot after inspiration on github from:

robbiebarrat developing the twitter-contest-enterer https://github.com/robbiebarrat/twitter-contest-enterer
rhiever developing the TwitterFollowBot https://github.com/rhiever/TwitterFollowBot

What i found was that both did what i needed from a bot, but not combined.

The twitter-contest-enterer retweeted tweets but did not like the same tweet or follow the user. The TwitterFollowBot would like, follow and retweet but not all the same person, it would act in a very sporadic way. This does not mean in any way that they are bad bots, they just didn't fulfill my required purpose.

Over time i have looked at many Twitter scripts, taken bits from some, drop some from others and come up with a working solution.
The purpose of this bot is with minimal set up it will fulfil your contest entering requirements. I understand that everyone wants the easy option so that a script will 'just work', i have done my best to make this happen for you.

Prequisites:

Twython
Python
Minor scripting knowledge
Twitter account with developer permissions
30 minutes of your time

#Instructions for Linux/Pi

Copy and paste below taking care on extra spaces

sudo apt-get install python-setuptools python-dev build-essential

sudo easy_install pip

sudo pip install --upgrade virtualenv

#At this point check your python version with:

python -V

If you have Python 2.x then run:

sudo pip install twython

If you have Python 3.x then run:

sudo pip3 install twython

#Make sure you are in your home directory then:

git clone https://github.com/mablono5/twittercompbot

cd twitter-compbot

sudo nano config.py

#In here you need to put in your twitter dev account keys

Ctrl X to save then y, press enter

python twittercompbot.py

DONE!

