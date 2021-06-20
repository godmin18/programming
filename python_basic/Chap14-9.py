from bs4 import BeautifulSoup

f = open('C:/Users/min/Desktop/Git/programming/python_basic/test.html', 'rt', encoding='UTF-8')
html = f.read()
f.close()
soup = BeautifulSoup(html, 'lxml')

#p태그의 class속성이 book_title 조회
title = soup.select('p.book_title')
print(title)