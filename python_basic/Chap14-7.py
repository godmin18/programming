from bs4 import BeautifulSoup
import requests

html = '''
<html>
    <head>
        <title>작품과 작가 모음</title>
    </head>
    <body>
        <h1>책 정보</h1>
        <p class = 'book_title'>토지</p>
        <p class = 'author'>박경리</p>
        <p class = 'book_title'>태백산맥</p>
        <p class = 'author'>조정래</p>
        <p class = 'book_title'>감옥으로부터의 사색</p>
        <p class = 'author'>신영복</p>
    </body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')

#soup은 객체 형태로 다양한 객체로 정보를 찾을 수 있다.
print(soup.html)
print(soup.html.head)
print(soup.html.head.title)
print(soup.html.body)
print(soup.html.body.h1)

#find, find_all를 사용하면 속성을 사용하여 디테일한 스크래핑을 할 수 있다.
titles = soup.find_all('p', {'class':'book_title'})
authors = soup.find_all('p', {'class':'author'})
print(titles, authors)

