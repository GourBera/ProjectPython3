'''
Created on May 21, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


from textblob import TextBlob
import textblob

print(dir(textblob))

statement = "Sentiment analysis with textblob has never been so easy."
statement1 = "Today Food was supper cool"
statement2 = "Is sentiment analysis good or bad you will say it was very nice?"


def SentimentAnalysis(statement):
    sentiment = TextBlob(statement)
    score = sentiment.sentiment.polarity
    print("Sentiment Score: " + "%.2f"%score )  


if __name__ == '__main__':
    SentimentAnalysis(statement)
    SentimentAnalysis(statement1)
    SentimentAnalysis(statement2)
