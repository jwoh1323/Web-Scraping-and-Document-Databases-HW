from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # store latest news title

    title = soup.find_all('div', class_='content_title')

    news_title = title[0].text

    # store paragraph of the latest news

    body = soup.find_all('div', class_='article_teaser_body')

    news_p = body[0].text


    # store the current Featured Mars Image and assign the url string to a variable 

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image = soup.find_all('a', class_= 'button fancybox')
    image = image[0]['data-fancybox-href']

    featured_image_url = "https://www.jpl.nasa.gov/" + image


    # scrape the latest Mars weather tweet

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    weather = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather = weather[0].text


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

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all('h2', class_ = 'title')
    title = title[0].text

    img = soup.find_all('a', target = '_blank')
    img = img[0]['href']

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title2 = soup.find_all('h2', class_ = 'title')
    title2 = title2[0].text

    img2 = soup.find_all('a', target = '_blank')
    img2 = img2[0]['href']

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title3 = soup.find_all('h2', class_ = 'title')
    title3 = title3[0].text

    img3 = soup.find_all('a', target = '_blank')
    img3 = img3[0]['href']

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title4 = soup.find_all('h2', class_ = 'title')
    title4 = title4[0].text

    img4 = soup.find_all('a', target = '_blank')
    img4 = img4[0]['href']

    browser.quit()

    hemisphere_image_urls = [
        
        {"title": title, "img_url": img},
        {"title": title2, "img_url": img2},
        {"title": title3, "img_url": img3},
        {"title": title4, "img_url": img4},
    ]

    mars_data = {
        "news_title": news_title,
        "news_sum": news_p,
        "mars_image": featured_image_url,
        "mars_weather": mars_weather,
        "mars_fact": html_table,
        "hemisphere_image": hemisphere_image_urls
    }

    return mars_data



