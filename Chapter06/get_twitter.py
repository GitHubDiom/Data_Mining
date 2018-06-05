import twitter
import tweepy
import os


consumer_key = "59tyrGqNHCdGB92eFYEsqcjdg"
consumer_secret = "DhglQERO5u936QibJP8YLbu6w60zmrxzl7jM0KmTQZZ0AXhr10"
access_token = "16065520-USf3DBbQAh6ZA8CnSAi6NAUlkorXdppRXpC4cQCKk"
access_token_secret = "DowMQeXqh5ZsGvZGrmUmkI0iCmI34ShFzKF3iOdiilpX5"
authorization = twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret)

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

output_filename = os.path.join(os.path.expanduser("~"), "For Data Analysis",
                                                        "Data_Mining","Chapter06","Dataset","python_tweets.json")
api = tweepy.API(auth,proxy='https://127.0.0.1:8118')

for status in tweepy.Cursor(api.home_timeline).items(2):
    print(status.text)