import streamlit as st
import pandas as pd
from scraper import (
    retrieve_website_content as scrape_site,
    clean_html_content as cleanse_text,
    split_text_into_chunks as split_content,
    get_body_html as get_body_html,
)
from parse import extract_data_with_ollama as ollama_parse  

st.title("AI Content Extractor")

# Input for website URL
input_url = st.text_input("Paste the Website URL:")

# Scraping and Content Extraction
if st.button("Initiate Scraping"):
    st.write("Processing the website...")
    page_data = scrape_site(input_url)

    if page_data:
        # Extract and clean the content
        body_text = get_body_html(page_data)
        refined_content = cleanse_text(body_text)
        st.session_state.refined_content = refined_content

        # Display the extracted data
        st.subheader("Extracted Data:")
        with st.expander("Click to Reveal Content"):
            st.text_area("Content from the Web Page", refined_content, height=300)

    else:
        st.error("Failed to retrieve content from the provided URL. Please check the URL and try again.")

# File Saving Section
if "refined_content" in st.session_state:
    st.subheader("Save Extracted Content")
    save_format = st.selectbox("Choose file format:", ["TXT", "CSV", "JSON", "Excel"])
    save_button = st.button("Save Content")

    if save_button:
        content = st.session_state.refined_content
        if save_format == "TXT":
            output_file = "scraped_content.txt"
            with open(output_file, "w") as file:
                file.write(content)
            st.success(f"Content saved as {output_file}")
        elif save_format == "CSV":
            df = pd.DataFrame({"Content": [content]})
            output_file = "scraped_content.csv"
            df.to_csv(output_file, index=False)
            st.success(f"Content saved as {output_file}")
        elif save_format == "JSON":
            import json
            output_file = "scraped_content.json"
            with open(output_file, "w") as file:
                json.dump({"Content": content}, file, indent=4)
            st.success(f"Content saved as {output_file}")

# Parsing Section
if "refined_content" in st.session_state:
    st.subheader("Process the Extracted Content")
    parsing_request = st.text_area("How would you like to process the content?")

    if st.button("Start Parsing"):
        if parsing_request:
            st.write("Parsing content...")
            content_segments = split_content(st.session_state.refined_content)
            parsed_output = ollama_parse(content_segments, parsing_request)
            st.subheader("Parsed Output:")
            st.write(parsed_output)
        else:
            st.error("Please enter a parsing request.")