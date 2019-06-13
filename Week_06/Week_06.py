#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
naver_movie = requests.get("https://movie.naver.com/movie/point/af/list.nhn?target=after").text
naver_movie_obj = bs(naver_movie,"html.parser")
naver_movie = naver_movie_obj.find('tbody')
movie_review = naver_movie.find_all('tr')
count_ = len(movie_review)


# In[3]:


print (movie_review[0].find('td',class_ = 'point').text)
print (movie_review[0].find('a',class_ = 'movie').text)

review_content = movie_review[0].find('a',class_ = 'report').get('href')

start = review_content.find('(')
end = review_content.find(')')
start_point = review_content[start + 1:end]
list_ = start_point.split(',')
review = list_[2]
print (review)


# In[4]:


for i in range(count_):
    print (movie_review[i].find('td',class_ = 'point').text)
    print (movie_review[i].find('a',class_ = 'movie').text)

    review_content = movie_review[i].find('a',class_ = 'report').get('href')

    start = review_content.find('(')
    end = review_content.find(')')
    start_point = review_content[start + 1:end]
    list_ = start_point.split(',')
    review = list_[2]
    print(review)


# In[5]:


result_score = []
result_title = []
result_review = []
for i in range(count_):
    result_score.append(movie_review[i].find('td',class_ = 'point').text)
    result_title.append(movie_review[i].find('a',class_ = 'movie').text)

    review_content = movie_review[i].find('a',class_ = 'report').get('href')

    start = review_content.find('(')
    end = review_content.find(')')
    start_point = review_content[start + 1:end]
    list_ = start_point.split(',')
    review = list_[2]
    result_review.append(review)


# In[6]:


data = {'score':result_score,'title':result_title,'report':result_review}
print(data)


# In[7]:


import pandas as pd
dt = pd.DataFrame(data,columns = ['score','title','report'])
dt


# In[2]:


page_num = int(input('크롤링 할 페이지 수: '))

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

result_score = []
result_title = []
result_review = []
result_id = []


for page in range(1,page_num):
    naver_movie_url = "https://movie.naver.com/movie/point/af/list.nhn?page=" + str(page)
    naver_movie = requests.get(naver_movie_url).text
    naver_movie_obj = bs(naver_movie,"html.parser")
    naver_movie = naver_movie_obj.find('tbody')
    movie_review = naver_movie.find_all('tr')
    

    for i in range(10):
        result_score.append(movie_review[i].find('td',class_ = 'point').text)
        result_title.append(movie_review[i].find('a',class_ = 'movie').text)
        result_id.append(movie_review[i].select('td')[4].find('a').text)

        review_content = movie_review[i].find('a',class_ = 'report').get('href')

        start = review_content.find('(')
        end = review_content.find(')')
        start_point = review_content[start + 1:end]
        list_ = start_point.split(',')
        review = list_[2]
        result_review.append(review)
data = {'id':result_id,'score':result_score,'title':result_title,'report':result_review}
dt = pd.DataFrame(data,columns = ['id','score','title','report'])


# In[14]:


dt.to_csv('/Users/hankiho/Desktop/df_result.csv', index = False, encoding = "utf-8-sig")


# In[16]:





# In[ ]:




