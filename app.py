import streamlit as st
from scraper import scrap_website, clean_content,split_dom_content,extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")


url = st.text_input("Enter a Website URL:")


if st.button("Scrape"):
    st.write("Scraping the website...")

    # Scrape the website using the dynamic scraper
    result = scrap_website(url)
    body_content = extract_body_content(result)

    if body_content:
        # Clean the scraped content
        cleaned_content = clean_content(body_content)
        
        st.session_state.dom_content = cleaned_content

       
        st.subheader("Scraped Data:")
        with st.expander("View  Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
        
if "dom_content" in st.session_state:    
    parse_description = st.text_area("Describe what you want to parse:")
        
       
    if st.button("Parse Content"):

        if parse_description:
            st.write("Parsing the content...")

            # Split the DOM content into chunks if it's too long
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)

                    


