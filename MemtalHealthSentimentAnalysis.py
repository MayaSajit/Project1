pip install textblob
import streamlit as st
import pandas as pd
from textblob import TextBlob
df = pd.read_csv('/Tracking_Mental_Health.csv')
column_name = 'Significant mental challenges'
def custom_sentiment(text):
  if text=='No Challenges':
    return 1
  elif text.lower()=='death of nearones' or text.lower()=='fake friendship' or text.lower()=="career anxiety" or text.lower()=='breakup' :
    return -1
  else:
    blob = TextBlob(text)
    return blob.sentiment.polarity
df['sentiment'] = df[column_name].apply(custom_sentiment)
#df['Sentiment Category'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
overall_sentiment_score = df['sentiment'].mean()
st.title("Sentiment Analysis App")
st.write("Sentiment Scores for Significant mental challenges")
if overall_sentiment_score >= 0.05:
  st.write("Overall Sentiment: Positive 😊")
elif overall_sentiment_score <= -0.05:
  st.write("Overall Sentiment: Negative 😞")
else:
  st.write("Overall Sentiment: Neutral 😐")
