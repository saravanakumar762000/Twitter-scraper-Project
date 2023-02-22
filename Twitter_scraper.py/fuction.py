import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools
from pymongo import MongoClient
import datetime

timestamp = datetime.datetime.now()



def scraping(search_term, since, until, number_of_tweets):

    scraped_tweets = sntwitter.TwitterSearchScraper(f'{search_term} since:{since} until:{until}').get_items()
    sliced_scraped_tweets = itertools.islice(scraped_tweets, number_of_tweets)
    global df
    df = pd.DataFrame(sliced_scraped_tweets)
    return df

def upload_in_Mongo(search_term):
    client=MongoClient("mongodb://Localhost:27017/")
    db=client["scraping"]
    twitter_data=db["twitter_data"]
    
    data=df.to_dict(orient="records")
    twitter_data.insert_one({"search":f"{search_term}","twitter_data":data})
    