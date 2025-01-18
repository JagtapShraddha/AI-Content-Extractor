import streamlit as st
from scraper import (
    retrieve_website_content as scrape_site,
    clean_html_content as cleanse_text,
    split_text_into_chunks as split_content,
    get_body_html as get_body_html,
)
from parse import extract_data_with_ollama as ollama_parse  

st.title("AI Content Scraper")

input_url = st.text_input("Paste the Website URL:")

if st.button("Initiate Scraping"):
    st.write("Processing the website...")
    page_data = scrape_site(input_url)

    if page_data:
        body_text = get_body_html(page_data)
        refined_content = cleanse_text(body_text)
        st.session_state.refined_content = refined_content

        st.subheader("Extracted Data:")
        with st.expander("Click to Reveal Content"):
            st.text_area("Content from the Web Page", refined_content, height=300)

if "refined_content" in st.session_state:
    parsing_request = st.text_area("How would you like to process the content?")

    if st.button("Start Parsing"):
        if parsing_request:
            st.write("Parsing content...")
            content_segments = split_content(st.session_state.refined_content)
            parsed_output = ollama_parse(content_segments, parsing_request)
            st.write(parsed_output)

