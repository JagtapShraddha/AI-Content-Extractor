import requests
from bs4 import BeautifulSoup

SCRAPER_API_URL = "http://api.scraperapi.com"
API_KEY = "27151b483204a4bc441d02205a569fab"

def scrap_website(url):
    try:
        response = requests.get(f"{SCRAPER_API_URL}?api_key={API_KEY}&url={url}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text()
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.get_text()
            if content:
                return str(content)
            return ""
            r
        
        

    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return None
        
def clean_content(result):
   
    # Split the result into lines
    lines = result.splitlines()
    
    # List to store cleaned lines
    cleaned_lines = []
    
    for line in lines:
        # Strip extra spaces from each line and remove empty lines
        cleaned_line = ' '.join(line.split())
        if cleaned_line:  # Only append non-empty lines
            cleaned_lines.append(cleaned_line)
    
    # Join all the cleaned lines back into a single string with newlines between them
    cleaned_content = "\n".join(cleaned_lines)
    
    return cleaned_content
    
def split_dom_content(dom_content, max_length=6000):
    if not dom_content:
        return []

    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]