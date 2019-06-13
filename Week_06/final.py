#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


dt = pd.read_csv('/Users/hankiho/Desktop/movie_review.csv')


# In[4]:


dt.head() # 상위 5개만 볼 수 있는 함수


# In[5]:


len (dt) # 데이터 길이를 확인 할 수 있는 함수


# In[12]:


dt['id'].head() #한개의 Feature를 인덱싱한는 방법, 리스트랑 비슷하다고 보면된다.


# In[8]:


dt['id'].nunique() #고유값 확인 방법


# In[52]:


dt['title'].value_counts().head(7) #attribute들의 갯수들을 확인하는 방법


# In[15]:


dt[dt['title'] == '기생충'] #특정 attribute만 인덱싱 하는 방법
parasite = dt[dt['title'] == '기생충']


# In[19]:


print ('평균 평점은: ', parasite['score'].mean())
print ('최저 평점은: ', parasite['score'].min())
print ('최고 평점은: ', parasite['score'].max())


# In[44]:


parasite[(parasite['score'] == 1) | (parasite['score'] == 2)]


# In[35]:


parasite.loc[(parasite['score'] > 5)]


# In[42]:


import seaborn as sns
sns.distplot(parasite["score"], bins = 20, color = "b")


# In[43]:


sns.countplot(data = parasite, x = 'score')


# In[49]:


dt[(dt['title'] == '기생충') | (dt['title'] == '걸캅스')]


# In[53]:


dt_01 = dt[(dt['title'] == '0.0MHz') | (dt['title'] == '어벤져스: 엔드게임')]


# In[55]:


sns.countplot(data = dt_01, x = 'score', hue = 'title')


# In[66]:


pd.DataFrame(dt.groupby('title')['score'].mean()).sort_values(by = 'score', ascending = False)


# In[68]:


parasite['report']


# In[72]:


df_review = str(parasite['report'])
df_review


# In[73]:


#특수문자와 숫자 제거
import re

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def cleanNumber(readData):
    text = re.sub('[0-9]', '', readData)
    return text


# In[75]:


import nltk
from konlpy.tag import Twitter; t = Twitter()


# In[76]:


# 특수문자, 숫자 제거 후 토큰화
tokens_ko = t.morphs(cleanNumber(cleanText(df_review)))


# In[77]:


stop_words = ['가','요','을','수','에','제','를','이','도','닉네임','입니다','된',
              '좋','는','로','으로','것','은','다','니다','대','들','이라','네','n',
              '들','데','의','때','겠','고','게','네요','한','일','할','\n','r',
              '하는','주','려고','인데','거','좀','는데','전','이라','했','주려','t',
              '뭐','까','있는','습니다','다면','했','주려','무지','합니다','에서','\\','\xa0'
              '지','있','못','후','중','줄','과','에서','해','단어','라고','합','부터']
tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]


# In[82]:


ko = nltk.Text(tokens_ko)
ko.vocab().most_common(30)


# In[85]:


from wordcloud import WordCloud
wc = WordCloud(font_path = '/Users/hankiho/anaconda3/lib/python3.6/site-packages/pytagcloud/fonts/NanumBarunGothic.ttf',
              background_color='white', max_words=2000, stopwords = stop_words)
wc = wc.generate(df_review) #스트링으로 변환해야됨

plt.figure(figsize=(8,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[ ]:




