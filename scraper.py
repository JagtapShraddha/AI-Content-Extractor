import requests
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# API endpoint and key (disabled for now)
# SCRAPER_API_URL = "http://api.scraperapi.com"
# API_KEY = "27151b483204a4bc441d02205a569fab"

def retrieve_website_content(url):
    driver_path = "./chromedriver"
    chrome_options = wd.ChromeOptions()
    browser_instance = wd.Chrome(service=Service(driver_path), options=chrome_options)

    try:
        # Navigate to the webpage
        browser_instance.get(url)
        print("Page loaded successfully!")
        page_source = browser_instance.page_source
        time.sleep(5)

        return page_source

    except Exception as error:
        print(f"Error during website retrieval: {error}")
        return None

    finally:
        browser_instance.quit()

def get_body_html(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    body = soup.body
    return str(body) if body else ""

def clean_html_content(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    # Remove unwanted tags (script, style)
    for tag in soup(["script", "style"]):
        tag.extract()

    # Extract clean text from the page
    clean_text = soup.get_text(separator="\n")
    return "\n".join([line.strip() for line in clean_text.splitlines() if line.strip()])

def split_text_into_chunks(long_text, chunk_limit=6000):
    # Break the long text into manageable chunks
    if not long_text:
        return []
    return [long_text[i:i + chunk_limit] for i in range(0, len(long_text), chunk_limit)]
