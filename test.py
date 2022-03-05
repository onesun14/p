import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

response = requests.get(url)

#200 뜨면 신호를 성공적으로 받았다는 것
if response.status_code == 200:
    print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print("soup", soup)

    #h1 tag 출력
    print("soup hi", soup.h1)

    #하위 목록 뽑기
    for ch in soup.h1.children:
        print(ch)
    #FindAll 은 원하는 찾고자 하는 것을 전체에서 list 형태로 return 한다.
    ex = soup.findAll("h1", {"class":"title"})
    print("ex", ex)
    top_list = soup.findAll("div", {"class":"tit3"})
    print("top_list", top_list)
    p = soup.find_all('p')
    top_list = soup.find_all(attrs={'class':'tit3'})
    print("top_list", top_list)
    index = 1
    #strip 은 공백을 제거하는 역할을 한다.
    for i in top_list:
        print(index, i.text.strip())
        index += 1

    #find_all 은 원하는 태그들을 볼 수 있따.
    soup.find_all(['h1', 'p'])