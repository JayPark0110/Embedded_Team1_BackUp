from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup

def daum_news():
  r = requests.get('https://news.daum.net/')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all("a", {"data-tiara-layer":"article"})

  print("Daum_News")
  for i in range(12):
    print(i+1, str(news_tit[i].text).strip())
  print()

def daum_sports_ws():
  r = requests.get('https://sports.daum.net/worldsoccer')
  html_doc = r.content
  soup = BeautifulSoup(html_doc, 'html.parser')
  news_tit = soup.find_all("a", {"data-tiara-layer":"rankingnews popular news_list"})

  print("Daum_Sports_WorldSoccer")
  for i in range(len(news_tit)):
    print(i+1, str(news_tit[i].text).strip())
  print()


def naver_weather():
  html = requests.get('https://weather.naver.com/today/09140104')
  soup = BeautifulSoup(html.text, 'html.parser')
  data1 = soup.find('div', {'class': 'today_weather'})
  
  find_currenttemp = data1.find('strong',{'class': 'current'}).text
  # print(find_currenttemp+'C')

  data2 = data1.findAll('dd')
  if(len(data2)==3):
    find_rain = '0%'
    find_hum = data2[0].text
    find_wind = data2[1].text
    find_sens = data2[2].text
  else:
    find_rain = data2[0].text
    find_hum = data2[1].text
    find_wind = data2[2].text
    find_sens = data2[3].text
  
  # print("습도 :",find_hum)
  # print("바람 :",find_wind)
  # print("체감온도 :",find_sens+'C')
  

  data3 = soup.find('ul', {'class' : 'today_chart_list'})
  data_dust = data3.findAll('em')
  find_dust = data_dust[0].text
  find_ultra = data_dust[1].text
  find_uv = data_dust[2].text
  # print('현재 미세먼지: '+find_dust)
  # print('현재 초미세먼지: '+find_ultra)
  # print('현재 자외선: '+find_uv)

  text = ('현재 날씨\n' + find_currenttemp+'C\n' + '강수확률 : ' + find_rain + '\n습도 : ' + find_hum + "\n바람 : " + find_wind +"\n체감온도 : " + find_sens+'C' + '\n현재 미세먼지 : '+ find_dust + '\n현재 초미세먼지 : '+ find_ultra + '\n현재 자외선 : '+ find_uv)

  return text
  

def naver_current_weather():    
  html = requests.get('https://weather.naver.com/today/09140104')
  soup = BeautifulSoup(html.text, 'html.parser')
  data1 = soup.find('div', {'class': 'today_weather'})
  find_currenttemp = data1.find('strong',{'class': 'current'}).text
  
  return find_currenttemp # 온도만 출력

def naver_current_weather_Icon():    
  html = requests.get('https://weather.naver.com/today/09140104')
  soup = BeautifulSoup(html.text, 'html.parser')
  data1 = soup.find('div', {'class': 'today_weather'})
  data_icon = data1.select('i')[-1]['data-ico']
  
  return (data_icon)

naver_current_weather_Icon()

naver_weather()
