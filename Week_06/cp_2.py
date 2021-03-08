import os
import time
import requests
from bs4 import BeautifulSoup as bs

import pandas as pd

def crawl_cp(keyword):
    url = 'https://www.coupang.com/np/search?q=' + keyword + '&channel=user'
    
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
                }
    
    webpage = requests.get(url, headers = headers)
    soup = bs(webpage.content, "html.parser")
    name = [x.text for x in soup.find_all('div', class_ = 'name')]
    df = pd.DataFrame(name)
    df['cate'] = keyword
    df.columns = ['mall_name','cate']
    return df

if __name__ == "__main__":
    empty_df = []
    for keyword in ['여성 청바지','여성 악세사리']:
        empty_df.append(crawl_cp(keyword))
    df = pd.concat(empty_df)
