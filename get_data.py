import tweepy as tw
import pandas as pd



consumer_key = "Bin7OE3nLtLpfweuh51rYzm3o"

consumer_secret = "5A5MeYsJhkValxR9k6fJZAk6kszg5cnrJZxLoKUgdY3mA3ghuS"

access_token = "1534553416286228480-ZnZgZfwZkzinGFGg4prVlyoDrZoxOJ"

access_token_secret = "1PZld6wdE02YAqgm1wusBKsqcgKDDnjfcghTfv65SqrEz"

auth = tw.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

search_words = "brunei"

date_since = "2022-01-01"

lang = "en"

tweets = tw.Cursor(api.search_tweets,q=search_words,lang=lang,).items(10000)

df = [[tweet.id,tweet.text, tweet.user.screen_name, tweet.user.followers_count, tweet.favorite_count, tweet.retweet_count,tweet.user.location, str(tweet.created_at)] for tweet in tweets]

raw_df = pd.DataFrame(df, columns = ['id','text','user','user_followers','favorite_count', 'retweet_count','location','datetime'])

raw_df.to_csv(r"raw_brunei_tweets_tweepy.csv", index = False)