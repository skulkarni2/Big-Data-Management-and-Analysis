# Import the necessary methods from "twitter" library
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import json
from tweepy.streaming import StreamListener

json_data = open("api.json").read() #reading api key from api.json
api = json.loads(json_data)

ACCESS_TOKEN = str(api["ACCESS_TOKEN"])
ACCESS_SECRET = str(api["ACCESS_SECRET"])
CONSUMER_KEY = str(api["CONSUMER_KEY"])
CONSUMER_SECRET = str(api["CONSUMER_SECRET"])

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

class MyListener(StreamListener):
   def on_data(self, data):
       try:
           #json_data = status._json
#             tweet = json.loads(data)
           #print (tweet)
#             record = {'Text': data.text, 'Created At': data.created_at}
           with open('twitterData.json', 'a') as f:
               f.write(data)
#             es.index(index="idx_twp", doc_type="twitter_twp", id=tweet["id"], body=tweet)
       except Exception as e:
           #print("exception: "+e)
           pass

       def on_error(self, status):
           print(status)
           return True

def start_stream():
   while True:
       try:
           twitter_stream = Stream(auth, MyListener())
           twitter_stream.filter(locations=[-124, 24, -66, 49], languages=['en'], track = ["#NYTimes", "@nytimes"] )
       except:
           continue
        
start_stream()




