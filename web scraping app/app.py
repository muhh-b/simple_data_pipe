import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from facebook_utils import login_to_facebook, search_hashtag
from image_utils import download_image
from mongodb_utils import store_to_mongodb

# Variables pour les chemins et les informations d'identification
CHROMEDRIVER_PATH = r'C:\chromedriver.exe'
USERNAME = os.getenv('FACEBOOK_USERNAME')
PASSWORD = os.getenv('FACEBOOK_PASSWORD')
MONGODB_URL = "mongodb://username:password@localhost:27017/data_scraping"
HASHTAG = "harcèlement"

if __name__ == "__main__":
    # Pilote Selenium Chrome 
    browser = webdriver.Chrome(CHROMEDRIVER_PATH)

    # Connectez-vous à Facebook
    login_to_facebook(browser, USERNAME, PASSWORD)

    # Recherchez le hashtag
    search_hashtag(browser, HASHTAG)

    # Récupérez les posts et téléchargez les images
    try:
        posts = browser.find_element_by_xpath('//*[@id="root"]/div[1]')
        links = posts.find_elements_by_link_text("Actualité intégrale")
        pubs = []
        for link in links:
            pub = {}
            page_content = requests.get(link.get_attribute('href')).content
            soup = BeautifulSoup(page_content, 'html.parser')
            pub['text'] = soup.p.text
            pub['image'] = soup.img["src"]
            img_url = soup.img["src"]
            filename = os.path.join(default_dir, img_url.split("/")[-1])  # Assurez-vous que default_dir est défini quelque part
            download_image(img_url, filename)
            pubs.append(pub)
    except Exception as e:
        print(f"Erreur lors de la récupération des posts et du téléchargement des images: {e}")
    
    # Stockez les données dans MongoDB
    store_to_mongodb(pubs, MONGODB_URL)

    # Fermez le navigateur
    browser.quit()

