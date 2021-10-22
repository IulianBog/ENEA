from selenium import webdriver 
import random
from time import *

def open_youtube():
    driver = webdriver.Chrome() 
    driver.get("https://www.youtube.com")
    # preia toate titlurile de pe pagina de youtube
    user_data = driver.find_elements_by_xpath('//*[@id="video-title-link"]')
    links = []
    
    for i in user_data:
        #titlurile preluate sunt bagate intr-o lista sub forma de link
        links.append(i.get_attribute('href'))
    # este ales un link random
    driver.get(links[random.randint(1, len(links))])
    
    # fuctia sleep este folosita ca o metoda de asteptare pana apare pop-up-ul
    sleep(3)
    # apasarea butonului "accept" de la pop-up
    driver.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
