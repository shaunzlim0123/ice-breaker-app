import os
from dotenv import load_dotenv
import tweepy
import requests
from setuptools.package_index import user_agent

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    wait_on_rate_limit=True  # This parameter tells Tweepy to pause until the rate limit resets
)

def scrape_user_tweets(username, mock=False, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """

    tweet_list = []

    if mock:
        HARRISON_TWITTER_GIST = "https://gist.githubusercontent.com/shaunzlim0123/17bf56275333dd5319eaf98a3e6be85d/raw/1914eeda602d191f50d25602e3b998f394e67d2c/shaun-lim-twitter.json"
        tweets = requests.get(HARRISON_TWITTER_GIST, timeout=5).json()

        for tweet in tweets:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
            tweet_list.append(tweet_dict)

    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )

        print(tweets)

        for tweet in tweets.data:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

    return tweet_list

if __name__ == "__main__":
    pass