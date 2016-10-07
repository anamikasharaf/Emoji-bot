import pdb	# This is the Python debugger
import sys
import tweepy, time

def authenticate_twitter_handle():
	#Corresponding information from my Twitter application:
	CONSUMER_KEY = 'fLmz7gBoJKRWadvJH7iS0Fg4c'
	CONSUMER_SECRET = 'xV1QWW4HQ0B3uMGZ2A7dQQxl1rwQ7m81DrCOtesUeXOK162EYL'
	ACCESS_TOKEN = '2909884898-RoNhu9ZKA2h2xoRdDTWmVDxwxmOhOJ7tFEi08va'
	ACCESS_TOKEN_SECRET = 'k68aPRqMrGhqXCF6tHWVs1sEx0kQuTyIrtq5AN6NZ5g8R'
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api

def post_emoji(api):
	top = api.home_timeline()[0]
	last_post = ""
	while True:
		l = api.home_timeline()
		if top.id != l[0].id:
			top = l[0]
	        emoji_string = retrieve_emoji(top.text)
	        if (len(emoji_string) > 0):
		        post_message = emoji_string
		        if (last_post != post_message and len(post_message) > 0 and len(post_message) <= 140):
		        	s = api.update_status(post_message)
		        	last_post = post_message
		time.sleep(30)

# Master emoji dictionary
emoji_dict = dict()

# This function reads the emoji data file,
# creates a dictionary and loads the emoji data
# into the dictionary. The keys of the dictionary are
# the emotion trigerring words (such as "happy", "sad")
# and values are the emojis associated with those words.
def load_emoji_data():
	# Read the emoji data file
	f = open("emoji_data.txt", "r")
	# Costruct a dictionary and populate with emoji data
	# The keys are keywords, the values are the emojis
	for line in f:
		line = line.strip().decode("utf-8")
		tokens = line.split(",")
		try:
			assert(len(tokens) == 2)
		except:
			pdb.set_trace()
		k = tokens[0].strip()
		v = tokens[1].strip()
		if k not in emoji_dict:
			emoji_dict[k] = v

def retrieve_emoji(line):
	input_sent = line
	#print "Input sentence is = " + input_sent
	input_sent = input_sent.strip()
	line_tokens = input_sent.split()
	emoji_string = ""
	for tok in line_tokens:
		tok = tok.strip()
		if tok in emoji_dict:
			emoji_string += " " + emoji_dict[tok]
	return emoji_string

def main():
	api = authenticate_twitter_handle()
	load_emoji_data()
	post_emoji(api)

if __name__=="__main__":
	main()


