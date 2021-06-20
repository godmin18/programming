from bs4 import BeautifulSoup
import requests

html = '''
<html>
    <body>
        <div>
            <span>
                <a herf = 'http://www.naver.com'>naver</a>
                <a herf = 'https://www.google.com'>google</a>
                <a herf = 'http://www.daum.net'>daum</a>
            </span>
        </div>
    </body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
#print(soup, type(soup))

# find, findall 속성을 사용하여 태그 찾기
firsttag = soup.find('a').get_text() #첫번쨰 a태그만 반환
alltag = soup.find_all('a') #모든 a태그를 리스트로 반환

print(firsttag)
print(type(alltag), alltag[0], alltag[1], alltag[2], sep='\n')

for tag in soup.find_all('a'):
    print(tag.get_text())