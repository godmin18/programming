#호출된 URL 중 ? 이후에 나오는 것을 파라미터라고 한다.
#https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&uery=%ED%8C%8C%EC%9D%B4%EC%8D%AC

#?앞에는 서버 요청하는 경로, ? 뒤에 &으로 구분하여 파라미터를 표시한다. 파라미터는 =을 구분하여 키와 값으로 나뉜다.
#where=nexearch&
#sm=top_hty&
#fbm=1&
#ie=utf8&
#query=%ED%8C%8C%EC%9D%B4%EC%8D%AC  서버와 브라우저 사이의 인코딩 때문에 알아볼수없는 값으로 전달한다.

import webbrowser

naver_search_url="https://www.google.com/search?q="
search_word = ['파이썬', '데이터 분석', '인공지능', '딥러닝']
for word in search_word:
    url = naver_search_url + word
    webbrowser.open_new(url)