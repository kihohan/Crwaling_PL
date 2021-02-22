import os
import time
import random
from PIL import Image

from selenium import webdriver 
from bs4 import BeautifulSoup as bs


driver = webdriver.Chrome('chromedriver')
keyword = '여성청바지'
for page_num in range(20):
    base_url = 'https://www.coupang.com/np/search?q=' + keyword + '&page=' + str(page_num)
    driver.get(base_url)
    
    urls = driver.find_elements_by_css_selector('div.search-content.search-content-with-feedback > ul.search-product-list > li > a ')
    post_urls = [ i.get_attribute('href') for i in urls ]
    
    for i in post_urls:
        driver.get(i)
        time.sleep(1)
        soup = bs(driver.page_source, 'html.parser')
        bd = soup.find_all('div', class_ = 'type-IMAGE_NO_SPACE')
        rating = soup.find('span', class_ = 'rating-star-num').get('style').split(':')[1].strip()
        comment_cnt = soup.find('span', class_ = 'count').text.split(' ')[0] + ';'
        price = soup.find('span', class_ = 'total-price').text.strip()
        info = rating + comment_cnt + price
        dir_path = 'C:\\Users\\지우컴퍼니\\Desktop\\Jupyter\\쿠팡_여성청바지'
        dir_name = info + '_' + str(random.randrange(1, 100000) )
        new_path = dir_path + '/' + dir_name + '/'
        os.mkdir(new_path)
        os.chdir(new_path)

        try:
            for i in range(len(bd)):
                img_url = bd[i].find('img').get('src').split('//')[1]
                os.system("curl " + img_url + " > " + str(i) + ".jpg")
                img = Image.open(str(i) + ".jpg")
        except:
            print(i)
    print('{0} page is completed'.format(page_num + 1))
