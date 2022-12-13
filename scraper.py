import tweepy

#Twitter API Auth. 
# Connect to tweepy.Clint library
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAALlAhgEAAAAAE0GktwXv%2FmPvLqiqen7Y86v%2FeT0%3DmiBqKF2DnTcF6wjOrzfgTFMlLpWuKviQo5YuBhwZ5gj3GOVqv9')
#Request API auth with given handler token
auth = tweepy.OAuth2BearerHandler('AAAAAAAAAAAAAAAAAAAAALlAhgEAAAAAE0GktwXv%2FmPvLqiqen7Y86v%2FeT0%3DmiBqKF2DnTcF6wjOrzfgTFMlLpWuKviQo5YuBhwZ5gj3GOVqv9')
#Connect to tweepy.API library
api = tweepy.API(auth)


def run_query(myQuery):
    #Search recent tweets by relevancy for the given keyword 
    tweets = client.search_recent_tweets(query= myQuery,max_results=50, sort_order='relevancy', tweet_fields=['id','text','lang'], user_fields=['verified'], expansions='author_id')

    tweet_link=[]
    for tweet in tweets[0]: #Search in tweet field
        if(tweet.data['lang'] == 'en'): #Take only english tweet content
            tweet_link.append("https://twitter.com/x/status/" + tweet.data['id'])
    return tweet_link