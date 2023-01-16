# -*- coding: utf-8 -*-
"""All Candidate Vader and Exploratory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W-YPAHNnJN7fNW-2uoG2AEdEkFr92Mmk

## **Sentiment Analysis for Each Candidate Tweets**
"""

import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('stopwords')

#from nltk.stem import PorterStemmer
import nltk.corpus
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import string

!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('wordnet')

import nltk
nltk.download('omw-1.4')

from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

df_Peter = pd.read_excel('PeterObi.xlsx', names=['hashtags', 'text','user', 'user_location','source_device', 'user_created_at','user_followers_count','user_following_count','user_verified','tweet_place','tweet_geo','tweet_created_at']) 
df_Peter

df_Atiku = pd.read_excel('AtikuAbubakar.xlsx', names=['hashtags', 'text','user', 'user_location','source_device', 'user_created_at','user_followers_count','user_following_count','user_verified','tweet_place','tweet_geo','tweet_created_at']) 
df_Atiku

df_Tinubu = pd.read_excel('BolaTinubu.xlsx', names=['hashtags', 'text','user', 'user_location','source_device', 'user_created_at','user_followers_count','user_following_count','user_verified','tweet_place','tweet_geo','tweet_created_at']) 
df_Tinubu

df = pd.concat([df_Atiku, df_Peter, df_Tinubu], names=['hashtags', 'text','user', 'user_location','source_device', 'user_created_at','user_followers_count','user_following_count','user_verified','tweet_place','tweet_geo','tweet_created_at'])

df

PeterTweets = df_Peter['text'].dropna()

AtikuTweets = df_Atiku['text'].dropna()

TinubuTweets = df_Tinubu['text'].dropna()

PeterTweets

AtikuTweets

TinubuTweets

dfP_text = PeterTweets.to_frame
ghP = PeterTweets.to_frame()

ghP

dfA_text = AtikuTweets.to_frame
ghA = AtikuTweets.to_frame()

dfT_text = TinubuTweets.to_frame
ghT = TinubuTweets.to_frame()

def clean_textA(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = str(text).lower()
    text = re.sub('rt', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'[ðŸâ€]', '', text)
    text = re.sub(r'[â€™â€¦]', '', text)
    text = re.sub('tâ', '', text)
    text = re.sub('x9d', '', text)
    text = re.sub('ÿ', '', text)
    text = re.sub('t ', '', text)
    text = re.sub(r'[â€™]', '', text)
    text = re.sub(r'[œðŸ]', '', text)
    text = re.sub(r'[ðŸ‘‡ðŸ‘‡ðŸ¤ŒðŸ“¢ðŸ•Šï]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub(r"@([a-zA-Z0-9_]{1,50})",'',str(text))

    return text

def clean_textP(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = str(text).lower()
    text = re.sub('rt', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub(r"@([a-zA-Z0-9_]{1,50})",'',str(text))
    return text

def clean_textT(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = str(text).lower()
    text = re.sub('rt', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'[ðŸâ€]', '', text)
    text = re.sub(r'[â€™â€¦]', '', text)
    #text = re.sub('tâ', '', text)
    text = re.sub('x9d', '', text)
    text = re.sub('ÿ', '', text)
    #text = re.sub('t ', '', text)
    text = re.sub(r'[â€™]', '', text)
    text = re.sub(r'[œðŸ]', '', text)
    text = re.sub(r'[ðŸ‘‡ðŸ‘‡ðŸ¤ŒðŸ“¢ðŸ•Šï]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub(r"@([a-zA-Z0-9_]{1,50})",'',str(text))

    return text

def Text_Processing(Text):
  Processed_Text = list()
  Lemmatizer = WordNetLemmatizer()

 
 

  # Tokens of Words
  Tokens = nltk.word_tokenize(Text)


  # Removing Stopwords and Lemmatizing Words
  # To reduce noises in our dataset, also to keep it simple and still 
  # powerful, we will only omit the word `not` from the list of stopwords

  

  for word in Tokens:
    if word not in stop_words:
      Processed_Text.append(Lemmatizer.lemmatize(word))

 

 

  return(" ".join(Processed_Text))

 

 

  return Text

#applying function to data
ghP["text"]= ghP["text"].apply(lambda text: clean_textP(text))

ghP["text"].head(15)

#applying function to data
ghA["text"]= ghA["text"].apply(lambda text: clean_textA(text))

#applying function to data
ghT["text"]= ghT["text"].apply(lambda text: clean_textT(text))

ghP["text"]= ghP["text"].apply(lambda Text: Text_Processing(Text))

ghP["text"]

ghA["text"]= ghA["text"].apply(lambda Text: Text_Processing(Text))

ghT["text"]= ghT["text"].apply(lambda Text: Text_Processing(Text))

analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score["compound"]

ghP["polarity"]=ghP["text"].apply(sentiment_analyzer_scores)

ghA["polarity"]=ghA["text"].apply(sentiment_analyzer_scores)

ghT["polarity"]=ghT["text"].apply(sentiment_analyzer_scores)

def sentiment_col(y):
    if y >= 0.05 :
        return 'positive'
    elif y > -0.05 <0.05 :
        return 'neutral'
    elif y <= 0.05:
        return 'negative'

ghP["polarity"]=ghP["text"].apply(sentiment_analyzer_scores)

ghP['polarity'] = ghP['polarity'].apply(sentiment_col)

ghP['polarity']

polp=ghP['polarity'].groupby(ghP['polarity']).size().reset_index(name='count')

polp.head(15)
polp=polp.iloc[:60,::]
polp

polarityP=polp['polarity']
TotalPol=polp['count']
explode=[0.1,0.1,0.1]
colors = ['lightcoral', 'lightblue', 'lightgreen']

plt.pie(TotalPol, labels = polarityP, radius=1.1, colors=colors, autopct='%2.1f%%', explode=explode)
plt.title('Sentiment Analysis for Peter Obi Tweeets')
#plt.legend(labels)
plt.show()

ghA['polarity'] = ghA['polarity'].apply(sentiment_col)

ghA['polarity']

polA=ghA['polarity'].groupby(ghA['polarity']).size().reset_index(name='count')

polA.head(15)
polA=polA.iloc[:60,::]
polA

polarityA=polA['polarity']
TotalPolA=polA['count']
explode=[0.1,0.1,0.1]
colors = ['lightcoral', 'lightblue', 'lightgreen']

plt.pie(TotalPolA, labels = polarityA, radius=1.1, colors=colorsA, autopct='%2.1f%%', explode=explode)
plt.title('Sentiment Analysis for Atiku Abubakar Tweeets')
#plt.legend(labels)
plt.show()

ghT['polarity'] = ghT['polarity'].apply(sentiment_col)

polT=ghT['polarity'].groupby(ghT['polarity']).size().reset_index(name='count')

polT.head(15)
polT=polT.iloc[:60,::]
polT

polarityT=polT['polarity']
TotalPolT=polT['count']
explode=[0.1,0.1,0.1]
colorsT = ['yellow', 'lightblue', 'lightgreen']

plt.pie(TotalPolT, labels = polarityT, radius=1.1, colors=colorsT, autopct='%2.1f%%', explode=explode)
plt.title('Sentiment Analysis for Tinubu Tweeets')
#plt.legend(labels)
plt.show()

import seaborn as sns
from matplotlib import style
style.use('ggplot')
import matplotlib.pyplot as plt
import random
#dl_df = df.copy()
dfPeter = ghP.groupby('polarity').size().reset_index(name='coun')
n = dfPeter['polarity'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(1000)
c = random.choices(all_colors)

# Plot Bars
plt.figure(figsize=(10,5), dpi= 200)
plt.bar(dfPeter['polarity'], dfPeter['coun'], color=['black', 'blue', 'green'], width=.5)
for i, val in enumerate(dfPeter['coun'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':25}) 

plt.title('Sentiment Analysis for Peter Obi Tweets')

# Plot Bars
plt.figure(figsize=(10,5), dpi= 200)
plt.bar(dfPeter['polarity'], dfPeter['coun'], color=['red', 'blue', 'green'], width=.5)
plt.bar(dfAtiku['polarity'], dfAtiku['coun'], color=['red', 'blue', 'green'], width=.5)
plt.bar(dfTinubu['polarity'], dfTinubu['coun'], color=['red', 'blue', 'green'], width=.5)

for i, val in enumerate(dfPeter['coun'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':25}) 
plt.xticks(r + width/2,['positive','negative','neutral'])
plt.legend()
plt.title('Sentiment Analysis for Peter Obi Tweets')

"""Plot Vader Sentiment for Atiku"""

import seaborn as sns
from matplotlib import style
style.use('ggplot')
import matplotlib.pyplot as plt
import random
#dl_df = df.copy()
dfAtiku = ghA.groupby('polarity').size().reset_index(name='coun')
n = dfAtiku['polarity'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(1000)
c = random.choices(all_colors)

# Plot Bars
plt.figure(figsize=(10,5), dpi= 200)
plt.bar(dfAtiku['polarity'], dfAtiku['coun'], color=['red', 'blue', 'green'], width=.5)
for i, val in enumerate(dfAtiku['coun'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':25}) 

plt.title('Sentiment Analysis for Atiku Tweets')

# Plot Bars
plt.figure(figsize=(10,5), dpi= 200)
plt.bar(dfAtiku['polarity'], dfAtiku['coun'], color=['red', 'blue', 'green'], width=.5)
for i, val in enumerate(dfAtiku['coun'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':25}) 

plt.title('Sentiment Analysis for Atiku Tweets')

"""Plot Vader Sentiment for Tinubu Tweets"""

import seaborn as sns
from matplotlib import style
style.use('ggplot')
import matplotlib.pyplot as plt
import random
dfTinubu = ghT.groupby('polarity').size().reset_index(name='coun')
n = dfTinubu['polarity'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(1000)
c = random.choices(all_colors)

# Plot Bars
plt.figure(figsize=(10,5), dpi= 200)
plt.bar(dfTinubu['polarity'], dfTinubu['coun'], color=['red', 'blue', 'green'], width=.5)
for i, val in enumerate(dfTinubu['coun'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':25}) 

plt.title('Sentiment Analysis for Tinubu Tweets')

# Plot Bars
plt.figure(figsize=(10,5), dpi= 200)
plt.bar(dfTinubu['polarity'], dfTinubu['coun'], color=['red', 'blue', 'green'], width=.5)
for i, val in enumerate(dfTinubu['coun'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':25}) 

plt.title('Sentiment Analysis for Tinubu Tweets')

"""Plots of Sentiments of individual candidates"""

import pandas as pd
import matplotlib.pyplot as plot
# Create DataFrame
dfsentiment = pd.DataFrame({"Atiku Abubakar":[27.6,33.1,39.4],
                   "Peter Obi":[25.2, 29.7, 45.1],
                   "Bola Tinubu":[26.9, 42.8, 30.3]},
                  index = ["Negative", "Neutral", "Positive"])

# Create unstacked multiple columns bar
dfsentiment.plot(kind="bar", figsize = (8, 4), color=['red', 'green', 'blue'],  title="Sentiment Analysis of Individual Candidate Data")

"""#**CREATING WORD CLOUD FOR PETER OBI TWEETS**"""

from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

#Function to Create Wordcloud
def create_wordcloud(text):
    mask = np.array(Image.open("/content/cloud.jpg"))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="black",
    mask = mask,
    max_words=3000,
    stopwords=stopwords,
    repeat=True)
    wc.generate(str(text))
    wc.to_file("wc.png")
    print("Word Cloud Saved Successfully")
    path="wc.png"
    display(Image.open(path))

#Creating wordcloud for all tweets
create_wordcloud(ghP["text"].values)

#Creating wordcloud for all tweets
create_wordcloud(ghP["text"].values)

#Creating wordcloud for all tweets
create_wordcloud(ghA["text"].values)

#Creating wordcloud for all tweets
create_wordcloud(ghT["text"].values)

"""#**EXPLORATORY ANALYSIS FOR INDIVIDUAL CANDIDATE TWEETS**"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns
import re
import collections
import random

"""#TIMESERIES FOR CANDIDATE TWEETS"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PLOT NUMBER OF TWEET AGAINST TWEET CREATED DATE


timestamp = df_Peter['tweet_created_at'].dropna()
df_Peter['tweet_created_at'] = pd.to_datetime(df_Peter['tweet_created_at'])

 
# Group the data by month and count the number of tweets
tweet_count = df_Peter.groupby(pd.Grouper(key='tweet_created_at', freq='D')).count()
plt.rcParams["figure.figsize"] = (10,6)
# Plot the number of tweets over Date Created
color = 'purple'
plt.plot(tweet_count.index, tweet_count['text'],color=color )
plt.xlabel("Date")
plt.ylabel("Number of Tweets")
plt.title("Number of Tweets for Peter Obi Over Tweet Created Date")
plt.show()

timeseriesP = df_Peter['tweet_created_at'].dropna()

timeseriesP

df_Peter['Date_new'] = pd.to_datetime(timeseriesP).dt.date
df_Peter['Time'] = pd.to_datetime(timeseriesP).dt.time
df_Peter.head(5)

nf=df_Peter.groupby('Date_new').size().reset_index(name='tweet_volume')
nf.head(15)
nf=nf.iloc[:60,::]
nf

"""Plot Time Series for Peter Obi (Tweet Dates)"""

nf.plot.bar(x='Date_new', y="tweet_volume", rot=90, title="Time Series for Peter Obi (Tweet Dates)")


#Using Seaborn
axp=sns.barplot(x='Date_new', y='tweet_volume', data=nf, palette='Spectral')

plt.xlabel('Date Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""Plot Time Series for Atiku (Tweet Dates)"""

timeseriesA = df_Atiku['tweet_created_at'].dropna()
df_Atiku['DateNew'] = pd.to_datetime(timeseriesA, errors='coerce').dt.date
df_Atiku['Time'] = pd.to_datetime(timeseriesA, errors='coerce').dt.time
df_Atiku.head(5)

nA=df_Atiku.groupby('DateNew').size().reset_index(name='tweet_counts')
nA.head(15)
nA=nA.iloc[:60,::]
nA

nA.plot.bar(x='DateNew', y="tweet_counts", rot=90, title="Time Series for Atiku (Tweet Dates)")


#Using Seaborn
axA=sns.barplot(x='DateNew', y='tweet_counts', data=nA, palette='tab10')

plt.xlabel('Date Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""Plot Time Series for Tinubu (Tweet Dates)"""

#PLOT NUMBER OF TWEET AGAINST TWEET CREATED DATE


timestampT = df_Tinubu['tweet_created_at'].dropna()
df_Tinubu['tweet_created_at'] = pd.to_datetime(df_Tinubu['tweet_created_at'])

 
# Group the data by month and count the number of tweets
tweet_count = df_Tinubu.groupby(pd.Grouper(key='tweet_created_at', freq='D')).count()
plt.rcParams["figure.figsize"] = (10,6)
# Plot the number of tweets over Date Created
color = 'blue'
plt.plot(tweet_count.index, tweet_count['text'],color=color )
plt.xlabel("Date")
plt.ylabel("Number of Tweets")
plt.title("Number of Tweets for Atiku Abubakar Over Tweet Created Date")
plt.show()

timeseriesT = df_Tinubu['tweet_created_at'].dropna()

df_Tinubu['DateT_new'] = pd.to_datetime(timeseriesT).dt.date
df_Tinubu['Time'] = pd.to_datetime(timeseriesT).dt.time
df_Tinubu.head(5)

nT=df_Tinubu.groupby('DateT_new').size().reset_index(name='tweet_count')

nT.head(15)
nT=nT.iloc[:60,::]
nT

nT.plot.bar(x='DateT_new', y="tweet_count", rot=90, title="Time Series for Tinubu (Tweet Dates)")


#Using Seaborn
axT=sns.barplot(x='DateT_new', y='tweet_count', data=nT, palette='rocket_r')

plt.xlabel('Date Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""Time Series for Peter Obi (Tweet Time)"""

tmP=df_Peter.groupby('Time').size().reset_index(name='tweet_volume')

tmP.head(15)
tmP=tmP.iloc[:60,::]
tmP

tmP.plot.bar(x='Time', y="tweet_volume", rot=90, title="#Time Series for Peter Obi (Tweet Time)")


#Using Seaborn
axS=sns.barplot(x='Time', y='tweet_volume', data=tmP, palette='Spectral')

plt.xlabel('Time Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""Time Series for Atiku (Tweet Time)"""

tmA=df_Atiku.groupby('Time').size().reset_index(name='tweet_volume')

tmA.head(15)
tmA=tmA.iloc[:60,::]
tmA

tmA.plot.bar(x='Time', y="tweet_volume", rot=90, title="#Time Series for Atiku (Tweet Time)")


#Using Seaborn
axX=sns.barplot(x='Time', y='tweet_volume', data=tmA, palette='tab10')

plt.xlabel('Time Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""Time Series for Tinubu (Tweet Time)"""

tmT=df_Tinubu.groupby('Time').size().reset_index(name='tweet_volume')

tmT.head(15)
tmT=tmT.iloc[:60,::]
tmT

tmT.plot.bar(x='Time', y="tweet_volume", rot=90, title="#Time Series for Tinubu (Tweet Time)")


#Using Seaborn
axB=sns.barplot(x='Time', y='tweet_volume', data=tmT, palette='rocket_r')

plt.xlabel('Time Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""USER CREATED DATES FOR PETER OBI TWEETS"""

#PLOT NUMBER OF TWEET AGAINST USER CREATED DATE
usercreated = df_Peter['user_created_at'].dropna()

usercreated

df_Peter['usercreated'] = pd.to_datetime(df_Peter['user_created_at']).dt.date

user=df_Peter.groupby('usercreated').size().reset_index(name='tweet_volume')

user.head(15)
user=user.iloc[:60,::]
user

user.plot.bar(x='usercreated', y="tweet_volume", rot=90, title="Time series of User Created Dates for Peter Obi Tweeets")


#Using Seaborn
axUP=sns.barplot(x='usercreated', y='tweet_volume', data=user, palette='Spectral')

plt.xlabel('Date Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""USER CREATED DATES FOR ATIKU TWEETS"""

#PLOT NUMBER OF TWEET AGAINST USER CREATED DATE
usercreatedA = df_Atiku['user_created_at'].dropna()

usercreatedA

from datetime import datetime

df_Atiku['usercreatedA'] = pd.to_datetime(usercreatedA, format='%a %b %m %H:%M:%S %z %Y' ,  errors='coerce').dt.date

df_Atiku['usercreatedA']

userA=df_Atiku.groupby('usercreatedA').size().reset_index(name='tweet_volume')

userA.head(15)
userA=userA.iloc[:60,::]
userA

userA.plot.bar(x='usercreatedA', y="tweet_volume", rot=90, title="Time series of User Created Dates for Atiku Tweeets")


#Using Seaborn
axA=sns.barplot(x='usercreatedA', y='tweet_volume', data=userA, palette='tab10')

plt.xlabel('Date Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""USER CREATED DATES FOR TINUBU TWEETS"""

#PLOT NUMBER OF TWEET AGAINST USER CREATED DATE
usercreatedT = df_Tinubu['user_created_at'].dropna()

df_Tinubu['usercreatedT'] = pd.to_datetime(df_Tinubu['user_created_at']).dt.date

userT=df_Tinubu.groupby('usercreatedT').size().reset_index(name='tweet_volume')

userT.head(15)
userT=userT.iloc[:60,::]
userT

userT.plot.bar(x='usercreatedT', y="tweet_volume", rot=90, title="Time series of User Created Dates for Tinubu Tweeets")


#Using Seaborn
axT=sns.barplot(x='usercreatedT', y='tweet_volume', data=userT, palette='rocket_r')

plt.xlabel('Date Tweet Created')
plt.ylabel('Number of Tweets')
plt.show(block=True)

"""#TWEET DEVICES FOR EACH CANDIDATE TWEETS"""

#TWEET DEVICES FOR PETER OBI TWEETS

# Prepare Data
def fill_column(x):
    if x == '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>':
        return 'Iphone'
    elif x== '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>':
        return 'Andrioid'
    elif x == '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>':
        return 'Web'
    else:
        return 'Others'

devices = df_Peter['source_device'].dropna()

#PLOT DEVICES

df_Peter['source_device'] = devices.apply(fill_column)
dfdevice = df_Peter.groupby('source_device').size().reset_index(name='counts')
n = dfdevice['source_device'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

dev=df_Peter.groupby(df_Peter['source_device']).size().reset_index(name='tweet_count')

dev.head(15)
dev=dev.iloc[:60,::]
dev

dev.plot.bar(x='source_device', y="tweet_count", rot=90, title="Tweet Devices for Peter Obi Tweeets")


#Using Seaborn
axDP=sns.barplot(x='source_device', y='tweet_count', data=dev, palette='Spectral')

plt.xlabel('Tweet Devices')
plt.ylabel('Total Tweet Count')
plt.show(block=True)

p=sns.barplot(x='source_device', y='tweet_count', data=dev, ci=None,)
sns.set(rc = {'figure.figsize':(15,6)})

p.set(title="Tweet Devices for Peter Obi Tweeets")

pdev=sns.barplot(x='source_device', y='tweet_count', palette='Spectral', data=dev, ci=None,order=dev.sort_values('tweet_count', ascending=False).source_device)
sns.set(rc = {'figure.figsize':(15,6)})
pdev.set(title="Tweet Devices for Peter Obi Tweeets")

#PIECHART
devType=dev['source_device']
Total=dev['tweet_count']
explode=[0.1,0.1,0.1,0.1]
colorsP = ['lightcoral', 'lightblue', 'lightgreen', 'yellow']

plt.pie(Total, labels = devType,radius=1.1, colors=colorsP, autopct='%2.1f%%', explode=explode)
plt.title('Tweet Devices for Peter Obi Tweeets')
plt.legend(devType)
plt.show()

"""TWEET DEVICES FOR ATIKU TWEETS"""

devicesA = df_Atiku['source_device'].dropna()

#PLOT DEVICES

df_Atiku['source_device'] = devicesA.apply(fill_column)
dfdeviceA = df_Atiku.groupby('source_device').size().reset_index(name='counts')
n = dfdeviceA['source_device'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

devA=df_Atiku.groupby(df_Peter['source_device']).size().reset_index(name='tweet_count')

devA.head(15)
devA=devA.iloc[:60,::]
devA

#BAR CHART
devA.plot.bar(x='source_device', y="tweet_count", rot=90, title="Tweet Devices for Atiku Tweeets")


#Using Seaborn
axDA=sns.barplot(x='source_device', y='tweet_count', data=devA, palette='tab10')

plt.xlabel('Tweet Devices')
plt.ylabel('Total Tweet Count')
plt.show(block=True)

pA=sns.barplot(x='source_device', y='tweet_count', data=devA, ci=None,)
sns.set(rc = {'figure.figsize':(10,6)})

pA.set(title="Tweet Devices for Atiku Tweeets")

#PIECHART
devTypeA=devA['source_device']
TotalA=devA['tweet_count']
explode=[0.1,0.1,0.1,0.1]

plt.pie(TotalA, labels = devTypeA, radius=1.1, autopct='%2.1f%%', explode=explode)
plt.title('Tweet Devices for Atiku Tweeets')
plt.legend(devTypeA)
plt.show()

"""TWEET DEVICES FOR TINUBU TWEETS"""

devicesT = df_Tinubu['source_device'].dropna()

#PLOT DEVICES

df_Tinubu['source_device'] = devicesT.apply(fill_column)
dfdeviceP = df_Tinubu.groupby('source_device').size().reset_index(name='counts')
nT = dfdeviceP['source_device'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=nT)

devT=df_Tinubu.groupby(df_Tinubu['source_device']).size().reset_index(name='tweet_count')

devT.head(10)
devT=devT.iloc[:60,::]
devT

#BAR CHART
devT.plot.bar(x='source_device', y="tweet_count", rot=90, title="Tweet Devices for Tinubu Tweeets")


#Using Seaborn
axDT=sns.barplot(x='source_device', y='tweet_count', data=devT, palette='rocket_r')

plt.xlabel('Tweet Devices')
plt.ylabel('Total Tweet Count')
plt.show(block=True)

#PIECHART
devTypeT=devT['source_device']
TotalT=devT['tweet_count']
explode=[0.1,0.1,0.1,0.1]
colorsA = ['yellow', 'lightblue', 'lightgreen','lightcoral']

plt.pie(TotalT, labels = devTypeT,colors=colorsA, radius=1.1, autopct='%2.1f%%', explode=explode)
plt.title('Tweet Devices for Tinubu Tweeets')
plt.legend(devTypeT)
plt.show()

"""#VERIFIED DEVICES FOR ATIKU TWEETS"""

#PLOTTING VERIFIED AND UNVERIFIED USERS
df_Peter.groupby(['user_verified'])['source_device'].count().plot.pie(figsize=(10,10),autopct='%1.1f%%')

vef=df_Peter.groupby(df_Peter['user_verified']).size().reset_index(name='tweet_count')

vefType=vef['user_verified']
Totalvef=vef['tweet_count']
explode=[0,0,0,0.1,0]

vef.head(15)
vef=vef.iloc[:60,::]
vef

# Verified Source  : Histogram
VerifiedSource = df_Peter['user_verified'].groupby(df_Peter['user_verified']).size().reset_index(name='counts')
VerifiedSource.plot.bar(x="user_verified", y="counts", rot=70, title="Trend for Verified Accounts");

#Tweet Source PieChart
y = VerifiedSource["user_verified"]
x = VerifiedSource["counts"]
#z = df2['DateCreated']
plt.pie(x, labels = y, autopct='%1.0f%%')
#plt.legend()
#myexplode = [0.2,0.1,0.1,0.1,0.,0.1,0.1,0.1,0.2,0.2]
plt.title("Percentage of Verified Users", bbox={'facecolor':'0.8', 'pad':4})
plt.show()

