import tweepy
import time
consumer_key='fDYcoJhpaSvs5nabFwYchgQc3'
consumer_secret='aprp5QIivoA3UCcQcf92sriJwpIh8eiNQt1FfhVfAptNhD9QTL'
access_token='1181501855374823424-V3yj1v5wFZFYodSffrRWnCh3L6DaOd'
access_token_secret='kjWQuq5u33rWVIg85d8cHcicN7QTIlJo9ODnKf287qkXO'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


FILE='key.txt'
def read_reply_id(FILE):
    file_read=open(FILE,'r')
    last_id=int(file_read.read().strip())
    file_read.close()
    return last_id
def store_reply_id(FILE,last_id):
    file_write =open(FILE,'w')
    file_write.write(str(last_id))
    file_write.close()
    return 

def reply():    
    tweets= api.mentions_timeline(read_reply_id(FILE),tweet_mode='extended')
    for tweet in reversed(tweets):
            if'#sricha' in tweet.full_text.lower():
                print("Replied to id : " + str(tweet.id)) 
                api.update_status("@" +tweet.user.screen_name + " HI Sricharan !!",tweet.id)
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                store_reply_id(FILE,tweet.id)   

while True:
    reply()
    time.sleep(60)