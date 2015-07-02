#(C) anupam kumar -https://github.com/anupamkumar08

import tweepy
import time
import os, random
# a random function
def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size 
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline() 
    return file.readline()

ckey='consumer key'
csecret='consumer secret'
akey='access key'
asecret='access secret'

auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)
x=1
while x==1 :
	s=get_random_line('xyz.csv');   # put your file EACH LINE MUST BE MAX 140 CHAR
	try:
		api=tweepy.API(auth)
		api.update_status(status=s)     # simply updating status
		time.sleep(60)
	except tweepy.error.TweepError:    # to evade match error
		pass
