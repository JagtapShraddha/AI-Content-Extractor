import requests
from selenium import webdriver as wbd
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# SCRAPER_API_URL = "http://api.scraperapi.com"

# API_KEY = "27151b483204a4bc441d02205a569fab"

def scrapeSite(url):
    driverpath = "./chromedriver"
    chromeoptions = wbd.ChromeOptions()
    browserinstance = wbd.Chrome(service=Service(driverpath)  , options=chromeoptions)

    
        # Open the URL
    browserinstance.get(url)
    print("Page loaded successfully!")

    pageSource = browserinstance.page_source
    time.sleep(5)

    return pageSource

    browserinstance.quit()

    # def scrap_website(url):
    
    #     response = requests.get(url)
    #     response.raise_for_status()  
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     content = soup.get_text()

def getBody(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')

    body = soup.body
    return str(body) if body else ""

def cleanseText(rawHtml):
    soup = BeautifulSoup(rawHtml, 'html.parser')
    
    # Remove unwanted tags (script, style)
    for tag in soup(["script", "style"]):

        tag.extract()

    
    cleanText = soup.get_text(separator="\n")
    return "\n".join([line.strip() for line in cleanText.splitlines() if line.strip()])

def splitContent(long_text, chunk_limit=6000):
   
    if not long_text:
        return []
    return [long_text[i:i + chunk_limit] for i in range(0, len(long_text), chunk_limit)]
