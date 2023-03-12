Article Sentiment Analysis

This project is a Python program that uses the Scrapy web crawling framework and the TextBlob natural language processing library to 
perform sentiment analysis on Finance articles. The program takes a user-inputted URL to a  Finance article, extracts the text content 
of the article using Scrapy selectors, and then uses TextBlob to calculate the sentiment polarity of the article. The sentiment polarity 
can be positive, negative, or neutral, and the program outputs the sentiment score to the console and to a JSON file.

Installation
To run the program, you will need to have Python 3 installed on your computer. You can download Python 3 from the
official Python website: https://www.python.org/downloads/

In addition, you will need to install the Scrapy and TextBlob libraries. You can install them using the following pip commands:

pip install scrapy
pip install textblob

Usage
To use the program, open a terminal or command prompt and navigate to the directory where the main.py file is located. Then run the following command:

python main.py

The program will prompt you to enter the URL of the Yahoo Finance article you want to analyze. Once you enter the URL, the program will scrape the article content, perform sentiment analysis using TextBlob, and output the sentiment score to the console and to a JSON file.

Sample Output
Here is an example of what the program output might look like:

[Enter the URL of the Yahoo Finance article: https://finance.yahoo.com/news/amazon-increases-minimum-wage-u-113547337.html

The sentiment of the article is slightly positive.
Sentiment score: 0.06666666666666667

Outputting sentiment score to sentiment.json...
Done.]

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the Scrapy and TextBlob documentation, as well as the many tutorials and examples available online.

