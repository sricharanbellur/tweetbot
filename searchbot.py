import tweepy
import time
consumer_key='fDYcoJhpaSvs5nabFwYchgQc3'
consumer_secret='aprp5QIivoA3UCcQcf92sriJwpIh8eiNQt1FfhVfAptNhD9QTL'
access_token='1181501855374823424-V3yj1v5wFZFYodSffrRWnCh3L6DaOd'
access_token_secret='kjWQuq5u33rWVIg85d8cHcicN7QTIlJo9ODnKf287qkXO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api =tweepy.API(auth)

hashtag = ("IPL","Cricket")
tweetNumber = 15

tweets = tweepy.Cursor(api.search,hashtag).items(tweetNumber)
for tweet in tweets:
    try:
        tweet.retweet()
        print("RT DONE")
        time.sleep(2)
    except tweepy.TweepError as e:
         print(e.reason)   
         time.sleep(2)