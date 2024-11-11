import requests
from bs4 import BeautifulSoup

def scrap_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text()
        
        if content:
            return str(content)
        return ""
 
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return ""

def clean_content(result):
    lines = result.splitlines()
    cleaned_lines = []
    for line in lines:
        cleaned_line =' '.join(line.split())
        if cleaned_line:
            cleaned_lines.append(cleaned_line)
        cleaned_content ="\n".join(cleaned_lines)
         
    

    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
    ]

