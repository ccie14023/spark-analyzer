from wordcloud import WordCloud
from textblob import TextBlob
import os

def get_sentiment(text):
	f = open("messages","r")
	text = f.read()
	f.close()
	blob = TextBlob(text)
	return blob.sentiment.polarity

def make_cloud(text):
	wordcloud = WordCloud().generate(text)
	wordcloud.to_file("wc.png")

if __name__ == "__main__":
	
	f = open("messages","r")
	text = f.read()
	f.close()

	os.remove("wc.png")

	print get_sentiment(text)
	make_cloud(text)
