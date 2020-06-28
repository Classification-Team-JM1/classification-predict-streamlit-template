import streamlit as st
import pandas as pd
import joblib,os
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from wordcloud import WordCloud
from collections import Counter
st.title("Sentiment Around Climate Change")
options = ["Information","Visuals", "Prediction"]
selection = st.sidebar.selectbox("Choose Option", options)
raw = pd.read_csv("resources/train.csv")
clean = pd.read_csv('resources/clean')

if selection == "Information":
    #image
    from PIL import Image
    img = Image.open("gw2.jpg")
    img2 = Image.open("gw.jpeg.jpg")
    #st.image(img, width = 300)
    st.image(img2, width = 400, caption = "How do the public view the climate change threat?")

    st.subheader("What Is Climate Change And Global Warming?")

    st.write("Climate change refers to a sustained change in overall tempreture and rainfall.")
    st.write("Global Warming is the ongoing increase in the average global tempreture")

    st.subheader("The Impact Of Climate Change Sentiment And Maximising Profit")
    st.write("This app will reveal the overall sentiment toward climate change by analysing recent")
    st.write("tweets ( post made on the social media application Twitter).")
    st.write("By understanding how potential consumers view climate change, companies can make informed")
    st.write("decisions on product development and marketing. This app will answer the question:")
    st.write("Do people see climate change as a real threat?")

    st.subheader("Take A Look At The Raw Data(view the tweets analysed)")

    if st.checkbox('Show raw data'): # data is hidden if box is unchecked
	    st.write(raw[['sentiment', 'message']]) # will write the df to the page
    st.header('A Quick Look At The Current Distribution Of Sentiment')
    data = pd.DataFrame(raw, columns = ['sentiment', 'message'] )
    st.write(data.plot(kind = 'hist', color = 'green'))
    st.pyplot()

    data = {'Sentiment Type': ['-1', '0', '1', '2'], 'Sentiment Meaning': ['Negative sentiment, opposing the belief that climate change is a threat', 'Neutral, an impartial stance on climate change', 'Positive, supporting the belief that climate change poses a threat', 'News Report, topical news reported on climate change'] }
    sentiment = pd.DataFrame(data, columns = ['Sentiment Type', 'Sentiment Meaning'])
    sentiment = sentiment.set_index('Sentiment Type')
    st.write(sentiment, width = 800)

    if st.checkbox('Interpretation Of Sentiment Distribution'):
        st.write('The majority of tweets reveal that most tweeters believe climate change is a real threat. Media coverage on climate change concerns substantiates the belief that climate change is a real threat. Tweeters who hold neutral sentiment or oppose the belief that climate change is a threat, remain in the minority  ')
        #st.write('Media coverage on climate change concerns substantiates the belief that climate change is a real threat')
        #st.write('Tweeters who hold neutral sentiment or oppose the belief that climate change is a threat, remain in the minority')

            	# Creating sidebar with selection box -
	            # you can create multiple pages this way


df_senti1 = raw[raw['sentiment']==1]
tweet_senti1 = " ".join(review for review in df_senti1.message)

#create word cloud in Visuals
if selection == "Visuals":
    from PIL import Image
    img = Image.open("gw2.jpg")
    img2 = Image.open("gw.jpeg.jpg")
    img3 = Image.open('banksy.jpg')
    #st.image(img, width = 300)
    st.image(img3, width = 400, caption = "Visualising the climate change threat")

    st.title('Insight From The Data')

  
    st.subheader('A Representation Of The Most Common Words In Each Sentiment Class')
    sent_groups = st.radio('Sentiment Views:',('Positive, those who believe climate change is a threat','Negative sentiment, opposing the belief that climate change is a threat', 'Neutral, an impartial stance on climate change', 'News Report, topical news reported on climate change'))
    if sent_groups == ('Positive, those who believe climate change is a threat'):
        df_senti1 = clean[clean['sentiment']==1]
        tweet_senti1 = " ".join(review for review in df_senti1.clean_stp_words)
        # Create and generate a word cloud image:
        wordcloud_1 = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_senti1)
        plt.imshow(wordcloud_1, interpolation='bilinear')
        #plt.set_title('Tweets under Pro Class 1',fontsize=50)
        plt.axis('off')
        #plt.axis("off")
        plt.show()
        st.pyplot()

        if st.checkbox('Interpretation of Diagram, Sentiment 1'):
            st.write('The bigger the word appears, the greater its occurance. Typical words amoung believers include to-tackle, to-fight, implying that many of the the tweeters believe action must be taken to combat climate change. This indicates a desire to take precautionary and action orientated measures to address the problem. Intrestingly, most of the tweets analysed support this view.')

    if sent_groups == 'Negative sentiment, opposing the belief that climate change is a threat':
        df_senti_neg1 = clean[clean['sentiment']==-1]
        tweet_senti_neg1 = " ".join(review for review in df_senti_neg1.clean_stp_words)
        # Create and generate a word cloud image:
        wordcloud_neg1 = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_senti_neg1)
        plt.imshow(wordcloud_neg1, interpolation='bilinear')
        #plt.set_title('Tweets under Pro Class 1',fontsize=50)
        plt.axis('off')
        #plt.axis("off")
        plt.show()
        st.pyplot()
        if st.checkbox('Interpretation of Diagram, Sentiment -1'):
            st.write('We see words such as man-made, scam, created-by appearing fairly often in only amoung this class. This reveals that many who hold this view do not only think its not a threat but many do not believe in the concept all together. Expressing the view that climate change may not even exist')

    if sent_groups == 'Neutral, an impartial stance on climate change':
        df_senti_0 = clean[clean['sentiment']==0]
        tweet_senti_0 = " ".join(review for review in df_senti_0.clean_stp_words)
        # Create and generate a word cloud image:
        wordcloud_0 = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_senti_0)
        plt.imshow(wordcloud_0, interpolation='bilinear')
        #plt.set_title('Tweets under Pro Class 1',fontsize=50)
        plt.axis('off')
        #plt.axis("off")
        plt.show()
        st.pyplot()
        if st.checkbox('Interpretation of Diagram, Sentiment 0'):
            st.write('Popular words in this class include care-about, think and maybe. This reflects uncertainty and possibly an apathetic attitude towards the matter. It also could reflect an interest in engaging the topic further.')

    if sent_groups == 'News Report, topical news reported on climate change':
        df_senti_2 = clean[clean['sentiment']==2]
        tweet_senti_2 = " ".join(review for review in df_senti_2.clean_stp_words)
        # Create and generate a word cloud image:
        wordcloud_2 = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_senti_2)
        plt.imshow(wordcloud_2, interpolation='bilinear')
        #plt.set_title('Tweets under Pro Class 1',fontsize=50)
        plt.axis('off')
        #plt.axis("off")
        plt.show()
        st.pyplot()
        if st.checkbox('Interpretation of Diagram, Sentiment 2'):
            st.write('Popular words in this class include Trump, global-warming, research, scientist and report. This reflects an interest in external validation to support a belief. News can have a powerful influence on the public. Validating climate change beliefs through media can impact overall sentiment on the matter')

    st.subheader('Take a look at the frequency of the 20 most common words in each class')
    Pro = clean[clean['sentiment']==1]
    Anti = clean[clean['sentiment']== -1]
    Neutral = clean[clean['sentiment']==0]
    News = clean[clean['sentiment']== 2]    
    common = st.selectbox('Select Sentiment Type',('Positive','Negative', 'Neutral','News'))
    st.write(common)
    if common == 'Positive':
        Pro['temp_list'] = Pro['clean_stp_words'].apply(lambda x:str(x).split())
        top = Counter([item for sublist in Pro['temp_list'] for item in sublist])
        temp_positive = pd.DataFrame(top.most_common(20))
        temp_positive.columns = ['Common_words','count']
        temp_positive = temp_positive.style.background_gradient(cmap='Greens_r')
        st.write(temp_positive, width=200)
    if common == 'Negative':
        Anti['temp_list'] = Anti['clean_stp_words'].apply(lambda x:str(x).split())
        top = Counter([item for sublist in Anti['temp_list'] for item in sublist])
        temp_neg = pd.DataFrame(top.most_common(20))
        temp_neg.columns = ['Common_words','count']
        temp_neg = temp_neg.style.background_gradient(cmap='Greens_r')
        st.write(temp_neg, width=200)
    if common == 'Neutral':
        Neutral['temp_list'] = Neutral['clean_stp_words'].apply(lambda x:str(x).split())
        top = Counter([item for sublist in Neutral['temp_list'] for item in sublist])
        temp_net = pd.DataFrame(top.most_common(20))
        temp_net.columns = ['Common_words','count']
        temp_net = temp_net.style.background_gradient(cmap='Greens_r')
        st.write(temp_net, width=200)
    if common == 'News':
        News['temp_list'] = News['clean_stp_words'].apply(lambda x:str(x).split())
        top = Counter([item for sublist in News['temp_list'] for item in sublist])
        temp_news = pd.DataFrame(top.most_common(20))
        temp_news.columns = ['Common_words','count']
        temp_news = temp_news.style.background_gradient(cmap='Greens_r')
        st.write(temp_news, width=200)       
    
    
    
    st.subheader('A Closer Look At The Data Distribution')
    temp = raw.groupby('sentiment').count()['message'].reset_index().sort_values(by='message',ascending=False)
    temp['percentage'] = round((temp['message']/temp['message'].sum())*100,0)
    labels1 = temp['sentiment']
    labels = ["Sentiment  %s" % i for i in temp['sentiment']]
    sizes = temp['percentage']

    fig1, ax1 = plt.subplots(figsize=(6, 6))
    fig1.subplots_adjust(0.3, 0, 1, 1)
 
    theme = plt.get_cmap('Greens_r')
    ax1.set_prop_cycle("color", [theme(1. * i / len(sizes))
                             for i in range(len(sizes))])
 
    _, _ = ax1.pie(sizes, startangle=90, labels = labels1,  radius=1800)
 
    ax1.axis('equal')
 
    total = sum(sizes)
    plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100)
            for l, s in zip(labels, sizes)],
    prop={'size': 7},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
    )
 
    plt.show()  # Equal aspect ratio ensures that pie is drawn as a circle.


    st.pyplot()   #c, use_container_width=True)

    if st.checkbox('Interpretation of Pie Chart'):
        st.write('More than half of the tweets analysed reflect a belief in climate change. Although it is not an overwhelming majority figure, believers are in the majority. As science begins to offer clearer evidence it is likely that many neutral tweeters could sway their beliefs. Less than ten percent of the sample population do not believe in climate change. If the sample is a good representation of the population than the market for evironmentally friendly or environmentally conscious goods and services could be a desireable product to fairly large sector of the population')
        

    

    
