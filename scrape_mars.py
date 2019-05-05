# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd



def scrap():
    mars_dict = {}

    executable_path = {'executable_path':'c:/Users/Kayla/Anaconda5/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)  

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.nasa_db
    db.articles

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
    browser.visit(url)
    response = browser.html
# Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response, 'html.parser')

        #title
    title = soup.find('div', class_='content_title').text
    title

        # paragraph
    paragraph = soup.find('div', class_="article_teaser_body").text
    print(paragraph)

    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url_image)
    full_image_button = browser.find_by_id("full_image")
    full_image_button.click()

    more_info_button = browser.find_link_by_partial_text("more info")
    more_info_button.click()   

    response_2 = browser.html
    # Create BeautifulSoup object; parse with 'lxml'
    soup_2 = BeautifulSoup(response_2, 'html.parser')    

    image = soup_2.find('figure', class_="lede").find("img")["src"]
    print(image)


    # https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18432_hires.jpg

    full_image = "https://www.jpl.nasa.gov" + image
    print(full_image)

    # MARS WEATHER
    # MARS WEATHER
    url_3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_3)
    response_3 = browser.html
    soup_3 = BeautifulSoup(response_3, 'html.parser')

    soup_3.find('div', class_='js-tweet-text-container').p.text

    url_4 = 'https://space-facts.com/mars/'

    pd.read_html(url_4)[0]


    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    url_5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemispheres = soup.select('div.item')

    hemisphere_image_urls = []

    for h in hemispheres:
        title = (h.find('h3').text).replace(' Enhanced', '')
            
        #click the hemisphere
        browser.click_link_by_partial_text(title)
        
        #make new soup of that page
        soup = BeautifulSoup(browser.html, 'html.parser')
        
        #find the full image
        full = soup.find('a', text='Sample')
        
        #get the img url
        img_url = full['href']
        
        #make a dict and append to the list
        hemisphere_image_urls.append({'title': title, 'img_url': img_url})
        
        #go back 
        browser.back()

    #close browser
    browser.quit()    

    hemisphere_image_urls

    return mars_dict