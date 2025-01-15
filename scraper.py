import requests
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

SCRAPER_API_URL = "http://api.scraperapi.com"
API_KEY = "27151b483204a4bc441d02205a569fab"

def scrap_website(url):
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = Service(chrome_driver_path),options=options)
    #response = requests.get(f"{SCRAPER_API_URL}?api_key={API_KEY}&url={url}")
        
    try:
        driver.get(url)
        print("page loaded")
        html = driver.page_source
        time.sleep(5)

        return html
    
        

        # soup = BeautifulSoup(response.content, 'html.parser')
        # content = soup.get_text()
        # # Check if the request was successful
        # if response.status_code == 200:
        #     soup = BeautifulSoup(response.content, 'html.parser')
        #     content = soup.get_text()
        #     if content:
        #         return str(content)
        #     return ""
            
        
        

    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return None
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


        
def clean_content(body_content):
    soup = BeautifulSoup(body_content,'html.parser')
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator = "\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
   

    # # Split the result into lines
    # lines = result.splitlines()
    
    # # List to store cleaned lines
    # cleaned_lines = []
    
    # for line in lines:
    #     # Strip extra spaces from each line and remove empty lines
    #     cleaned_line = ' '.join(line.split())
    #     if cleaned_line:  # Only append non-empty lines
    #         cleaned_lines.append(cleaned_line)
    
    # # Join all the cleaned lines back into a single string with newlines between them
    # cleaned_content = "\n".join(cleaned_lines)
    
    return cleaned_content
    
def split_dom_content(dom_content, max_length=6000):
    if not dom_content:
        return []

    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]