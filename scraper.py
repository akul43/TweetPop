import tweepy

#Twitter API Auth. 
# Connect to tweepy.Clint library
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAALlAhgEAAAAAE0GktwXv%2FmPvLqiqen7Y86v%2FeT0%3DmiBqKF2DnTcF6wjOrzfgTFMlLpWuKviQo5YuBhwZ5gj3GOVqv9')
#Request API auth with given handler token
auth = tweepy.OAuth2BearerHandler('AAAAAAAAAAAAAAAAAAAAALlAhgEAAAAAE0GktwXv%2FmPvLqiqen7Y86v%2FeT0%3DmiBqKF2DnTcF6wjOrzfgTFMlLpWuKviQo5YuBhwZ5gj3GOVqv9')
#Connect to tweepy.API library
api = tweepy.API(auth)
