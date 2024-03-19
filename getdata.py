from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import requests

def get_data(url:str, header:dict, name:str, attrs:dict):
    r = requests.get(url, headers=header)
    print(r)
    soup = BeautifulSoup(r.content, "html.parser")
    
    all_data = soup.find_all(name, attrs)

    try:
        for i in all_data:
            img_tags = i.find_all('img')            

            for img_tag in img_tags:
                img_url = img_tag['src']

                if not img_url.startswith('http'):
                    img_url = url + img_url

                
                search_string = ".jpg"
                index = img_url.find(search_string)

                if index != -1:
                    img_url = img_url[:index + len(search_string)]

                
                img_data = urlopen(img_url).read()

                
                with open(os.path.basename(img_url), 'wb') as img_file:
                    img_file.write(img_data)

            print("Resimler başarıyla indirildi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    