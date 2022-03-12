import requests
from bs4 import BeautifulSoup
import streamlit as st
number = st.number_input('test',1)
url = 'https://pokemonkorea.co.kr/pokedex/view/{}'
response = requests.get(url.format(number))

if response.status_code == 200:
    print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    a = soup.find_all("div", {'class':'col-lg-6 col-12'})
    for i in a:
        abc = i.text.strip()
        ab = abc.split("\n")
    for i in range(len(ab)):
        if ab[i] != '':
            print(ab[i])
st.write('test')
if st.button('test'):
    for i in range(len(ab)):
        if ab[i] != '':

            st.write(ab[i])
