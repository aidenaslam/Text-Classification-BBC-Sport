import requests
from bs4 import BeautifulSoup
import pandas as pd

def bbc_sport_news(url_list):
    """ Scrape news headlines from BBC Sport """    
    headlines_list = []
    source_list = [] 
    
    for url in url_list:
   
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')    
        news_items = soup.find_all('div', class_="gs-c-promo")

        # Grab headlines and label sport
        sport = (url.split('/')[-1])
        for headline in news_items:
            headlines_list.append(headline["data-bbc-title"])
            source_list.append(sport)

        # Combine headline and type of sport
        dataset = pd.DataFrame(zip(headlines_list,source_list))
        dataset.columns = ['Headline', 'Sport']
        
    return dataset

def sky_sports_news(url_list):
    """ Scrape news headlines from Sky Sports News """    
    headlines_list = []
    source_list = []

    for url in url_list:    
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')    
        news_items = soup.find_all('div', class_="news-list__body")
        # Grab headlines        
        sport = (url.split('/')[-1])    
        for headline in news_items:
            headlines_list.append(headline.p.get_text())
            source_list.append(sport)               
        # Combine headline and type of sport
        dataset = pd.DataFrame(zip(headlines_list, source_list))
        dataset.columns = ['Headline', 'Sport']
            
    return dataset 