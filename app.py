import streamlit as st
from scraper import scrap_website,clean_content
#from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

if st.button("Scrape"):
    st.write("Scraping the website...")
    result = scrap_website(url)

    if result:
        
        cleaned_content = clean_content(result)
        st.session_state.dom_content = cleaned_content

        st.subheader("Scraped Data:")
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
        
        """ if "dom_content" in st.session_state:
            parse_description=st.text_area("describe what you want to parse")

            if st.button("parse content"):
                if parse_description:
                    st.write("parsing the content")

                    dom_chunks=split_dom_content(st.session_state.dom_content)
                    result = parse_with_ollama(dom_chunks,parse_description) """


       
        
    else:
        st.error("No data was scraped. Please check the URL.")
