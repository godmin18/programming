import requests

r = requests.get('https://www.google.co.kr')
print(r, type(r)) #r 응답은 객체로 저장된다.

#text라는 속성으로 응답의 내용을 볼 수 있다.
print(r.text)