from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# store latest news title

title = soup.find_all('div', class_='content_title')

news_title = title[0].text
news_title

# store paragraph of the latest news

body = soup.find_all('div', class_='article_teaser_body')

news_p = body[0].text
news_p


# store the current Featured Mars Image and assign the url string to a variable 

url = 'https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA23061'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

image = soup.select_one('figure.lede img[src]')['src']
featured_image_url = "https://www.jpl.nasa.gov/" + image
featured_image_url


# scrape the latest Mars weather tweet

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

weather = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
mars_weather = weather[0].text
mars_weather

browser.quit()

# Mars Facts

url = 'https://space-facts.com/mars/'

table = pd.read_html(url)
table

# scrape the table and covert it to panda dataframe

df = table[0]
df.columns = ['Description', 'Value']
df

# covert to html

html_table = df.to_html()
html_table = html_table.replace('\n', '')

# save the table directly to a file

df.to_html('table.html')


# Mars Hemispheres

hemisphere_image_urls = [
    
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]



def scrape():
    mars_data = {
        "news_title": news_title,
        "news_sum": news_p,
        "mars_image": featured_image_url,
        "mars_weather": mars_weather,
        "mars_fact": html_table,
        "hemisphere_image": hemisphere_image_urls
    }

    return mars_data



