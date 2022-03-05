import requests
from bs4 import BeautifulSoup

url = 'https://pokemonkorea.co.kr/pokedex/view/{}'
response = requests.get(url.format(input()))

if response.status_code == 200:
    print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print("soup", soup)
    # a = soup.find_all("div", {'class':'bx-txt'})
    # p = soup.find_all(attrs={'class':'bx-txt'})
    # t = soup.find_all(attrs={'class':'badge badge-quad badge-grass'})
    a = soup.find_all("div", {'class':'col-lg-6 col-12'})
    print(a)
    # count = 0
    # #print("soup hi", soup.h3)
    # print(t)
    index = 1
    for i in a:
        print(i.text.strip())
        #print(index, i.text.strip())
        #index += 1