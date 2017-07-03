from nltk.corpus import wordnet as wn
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from pyspark import SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.types import *
import pandas as pd

def sentiment_score(sc):
    
    #spark = HiveContext(sc)
    sqlContext = HiveContext(sc)
    df = sqlContext.read.json("/user/skk456/project/twitterData.json")
    text_list = df.select(df['text'], df['id'])
    text = df.select("text").rdd.flatMap(lambda x: x).collect()
    tweet_id = df.select("id").rdd.flatMap(lambda x: x).collect()
    tweets = map(lambda tweet: tokenize.sent_tokenize(tweet), text)
    sia =  SentimentIntensityAnalyzer()
    score = map(lambda tweet: sia.polarity_scores(str(tweet)), tweets)
    comp = map(lambda i: i['compound'], score)
    pos = map(lambda i: i['pos'], score)
    neu = map(lambda i: i['neu'], score)
    neg = map(lambda i: i['neg'], score)
    
    score = pd.DataFrame()
    score['id'] = tweet_id
    score['positive'] = pos
    score['negative'] = neg
    score['neutral'] = neu
    score['compound'] = comp
    
    score_spark = sqlContext.createDataFrame(score)
    score_spark.rdd.saveAsTextFile('project/output1')
    
    
    #return (score_spark.coalesce(1).write.option("header", "true").csv("sentiment_score"))
    
    
sc = SparkContext()
sentiment_score(sc)
