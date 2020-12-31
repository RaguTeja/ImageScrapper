import requests   # To request the google server for data
from bs4 import BeautifulSoup   # to parse html code for scrapping the required data
import os  # To manage paths

class Scrapper:

    # step 1: retrieve the url of which categorical images you need

    def create_url(self,search_term):
        keyword = search_term.split()
        key_word = '+'.join(keyword)
        url = "https://www.google.co.in/search?q=" + key_word + "&source=lnms&tbm=isch"
        return url

    # step 2: take the raw html code

    def scrap_html(self,url):
        r = requests.get(url)
        bs = BeautifulSoup(r.text, 'html.parser')
        return bs

    # step 3: retrieve the image urls we need

    def get_imagelist(self,raw):
        images = []
        for url in raw.findAll('img'):
            images.append(url['src'])
        return images

    # step 4: download the images into our local server
    def download_images(self,images,image_name,freq=5):
        if not os.path.exists('static'):
            os.makedirs('static')
        count = 1
        for i,url in enumerate(images):
            if count <= freq:
                filename = image_name + str(i)
                try:
                    with open('static/{}.jpg'.format(filename), 'wb') as f:
                        image = requests.get(url)
                        f.write(image.content)
                except Exception as e:
                    print('error while downloading images',e)
            else:
                break
            count += 1
        return 0

    # step 5: Deleting the images in the local server.
    def delete_images(self,list_images):
        try:
            for image in list_images:
                os.remove('./static/'+image)
        except Exception as e:
            print('Error in deleting images',e)

        return 0
