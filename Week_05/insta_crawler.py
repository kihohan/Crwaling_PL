#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm_notebook
import time
import random

account = str(input('account: '))

chromedriver_dir = '/home/kiho/바탕화면/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)
driver.get("https://www.instagram.com/" + account + "/")

#계정에 포스터가 몇개 있는지확인
totalCount = driver.find_element_by_class_name('g47SY').text
time.sleep(0.1)
print("totalCount :", totalCount)

#바탕화면에 저장 할 폴더 생성
def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
root_dir = '/home/kiho/바탕화면'
work_dir = root_dir + '/' + account
make_folder(work_dir)

#저장 경로 정해주기
result_route = "/home/kiho/바탕화면/" + account + '/'
if not os.path.isdir(result_route):
    os.makedirs(result_route)
#첫번째 포스트 클릭
driver.find_element_by_class_name('_9AhH0').click() 
def get_image1():
    try:
        soup = bs(driver.page_source,'html.parser')

        like_obj = soup.find('div',class_ = 'Nm9Fw')
        like = like_obj.text

        inst_obj = soup.find('div', class_ = '_97aPb')
        
        image_obj = inst_obj.find('div',class_ = 'eLAPa _23QFA')
        image_url = image_obj.find('img', class_ = 'FFVAD')['src']

        outfile = like + '_' + str(random.randint(1, 10000)) + '.jpg'
        urllib.request.urlretrieve(image_url, result_route + outfile)
    except:
        soup = bs(driver.page_source,'html.parser')

        like_obj = soup.find('div',class_ = 'Nm9Fw')
        like = like_obj.text

        inst_obj = soup.find('div', class_ = '_97aPb')
        
        image_obj_2 = inst_obj.find('div',class_ = 'eLAPa kPFhm')
        image_url = image_obj_2.find('img', class_ = 'FFVAD')['src']

        outfile = like + '_' + str(random.randint(1, 10000)) + '.jpg'
        urllib.request.urlretrieve(image_url, result_route + outfile)
def get_image2():
    soup = bs(driver.page_source,'html.parser')

    like_obj = soup.find('div',class_ = 'Nm9Fw')
    like = like_obj.text

    inst_obj = soup.find('div', class_ = '_97aPb')
        
    image_obj_2 = inst_obj.find('div',class_ = 'eLAPa RzuR0')
    image_url = image_obj_2.find('img', class_ = 'FFVAD')['src']

    outfile = like + '_' + str(random.randint(1, 10000)) + '.jpg'
    urllib.request.urlretrieve(image_url, result_route + outfile)
def get_image():
    try:
        get_image1()
    except:
        get_image2()
def next_post_click():
    #다음 포스터 클릭
    wait = WebDriverWait(driver, 10)
    next_post_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow')))
    next_post_button.click()
def get_video():
    soup = bs(driver.page_source,'html.parser')
    inst_obj = soup.find('div', class_ = '_97aPb')
        
    video = inst_obj.find('div', class_ = '_5wCQW')
    video_live = video.find('video', class_ = 'tWeCl')['src'] #동영상
    outfile = str(random.randint(1, 10000)) + '.mp4'
    urllib.request.urlretrieve(video_live, result_route + outfile)
def insta_crawler_iamge_video():
    try:
        get_image()
    except:
        get_video()
def insta_crawler_final():
    next_post_click()
    try:
        time.sleep(1)
        insta_crawler_iamge_video()
    except:
        time.sleep(5)
        insta_crawler_iamge_video()

post_count = int(input('post_count: '))
insta_crawler_final()
for c in range(post_count - 1):
    insta_crawler_final()
    
print(post_count,'개가 크롤링 되었습니다.')
driver.close()


# In[ ]:




