import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/cat/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
getRents = soup.findAll('div', 'r-ent')

i = 0
list1=[0]

for getRent in getRents:
    i += 1
    meta = getRent.find('div', 'title').find('a')
    if meta:
        getTitle = meta.text.strip()    #取得標題
        getHref = meta.get('href')   #取得網址
        getDate = getRent.find('div', 'date').text    #取得日期
        getAuthor = getRent.find('div', 'author').text    #取得作者
        list1.append('https://www.ptt.cc' + getHref)    #將網址存入清單
        print('{0:0>2}. {1:5} {2:<15}{3}'.format(i, getDate, getAuthor, getTitle))
    else:
        getDate = getRent.find('div','date').text
        list1.append(' ')
        print('{0:0>2}. {1:5} {2:>23}'.format(i, getDate, '(本文已被刪除)'))
    
x = int(input('請輸入文章編號：'))    #選擇文章
while x>i or x<=0:
    x = int(input('無此編號，請重新輸入：'))

new_url = list1[x]    #所選文章的網址

if new_url==' ':
    print('本文已被刪除')
else:
    new_response = requests.get(new_url)    #取得所選文章之HTML
    new_soup = BeautifulSoup(new_response.text, 'html.parser')
    getScreens = new_soup.findAll('div', 'bbs-screen bbs-content')
    for getScreen in getScreens:
        print(getScreen.text)

os.system('pause')    #按任意按鍵以繼續