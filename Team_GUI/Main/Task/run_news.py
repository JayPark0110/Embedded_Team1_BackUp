import requests
from bs4 import BeautifulSoup


def daum_news():
  r = requests.get('https://news.daum.net/')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all("a", {"data-tiara-layer": "article"})
  
  news_list = []
  for i in range(12):
    news_list.append(str(news_tit[i].text).strip())
  return news_list


def daum_sports():
  r = requests.get('https://sports.daum.net/')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all(
      "a", {"data-tiara-layer": "rankingnews popular news_list"})
  
  news_list = []
  for i in range(len(news_tit)):
    news_list.append(str(news_tit[i].text).strip())
  return news_list

def daum_entertain():
  r = requests.get('https://entertain.daum.net/ranking/popular')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all(
      "a", {"data-tiara-type": "news"})

  news_list = []
  for i in range(len(news_tit)):
    news_list.append(str(news_tit[i].text).strip())
  return news_list

def daum_IT():
  r = requests.get('https://news.daum.net/digital#1')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all(
      "a", {"data-tiara-layer": "article_main"})
  news_tit2 = soup.find_all(
      "a", {"data-tiara-layer": "MCC cluster6 article_main"}
  )  
  
  news_list = []
  for i in range(len(news_tit)):
    news_list.append(str(news_tit[i].text).strip())
  
  for j in range(len(news_tit2)):
    news_list.append(str(news_tit2[j].text).strip())
  
  return news_list


def daum_economic():
  r = requests.get('https://news.daum.net/economic#1')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all(
      "a", {"data-tiara-layer": "article_main"})
  news_tit2 = soup.find_all(
      "a", {"data-tiara-layer": "MCC cluster6 article_main"}
  )  
  
  news_list = []
  for i in range(len(news_tit)):
    news_list.append(str(news_tit[i].text).strip())
  
  for j in range(len(news_tit2)):
    news_list.append(str(news_tit2[j].text).strip())
  
  return news_list
  
  

def daum_politics():
  r = requests.get('https://news.daum.net/politics#1')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all(
      "a", {"data-tiara-layer": "article_main"})
  news_tit2 = soup.find_all(
    "a", {"data-tiara-layer": "MCC cluster6 article_main"}
  )  
  
  news_list = []
  for i in range(len(news_tit)):
    news_list.append(str(news_tit[i].text).strip())
  
  for j in range(len(news_tit2)):
    news_list.append(str(news_tit2[j].text).strip())  
  return news_list
