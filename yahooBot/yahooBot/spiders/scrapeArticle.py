import scrapy
from textblob import TextBlob
import json

class ArticlesSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        url = input("Enter the URL of the article: ")
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text = response.css('.caas-body > p::text').getall()
        blob = TextBlob(' '.join(text))
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_str = "positive"
        elif sentiment < 0:
            sentiment_str = "negative"
        else:
            sentiment_str = "neutral"

        print("Sentiment score:", sentiment)
        print("Sentiment:", sentiment_str)

        data = {
            "sentiment": sentiment,
            "sentiment_str": sentiment_str
        }
        filename = "sentiment.json"
        with open(filename, "w") as f:
            json.dump(data, f)

        yield data