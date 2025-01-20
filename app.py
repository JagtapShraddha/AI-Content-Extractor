import streamlit as st
import pandas as pd
from scraper import scrapeSite ,cleanseText,splitContent,getBody 
from parse import extractData  

st.title("AI Content Extractor")


inputUrl = st.text_input("Paste the Website URL:")

# Scraping and Content Extraction
if st.button("Initiate Scraping"):
    st.write("Processing the website...")
    page_data = scrapeSite(inputUrl)

    if page_data:
        # Extract and clean the content
        text = getBody(page_data)
        refined_content = cleanseText(text)
        st.session_state.refined_content = refined_content

        # Display the extracted data
        st.subheader("Extracted Data:")
        with st.expander("Click to See Content"):
            st.text_area("Content Of Page", refined_content, height=300)

    else:
        st.error("Failed to retrieve content from the provided URL. Please check the URL and try again.")

# File Saving Section
if "refined_content" in st.session_state:
    st.subheader("Save Extracted Content")
    saveformat = st.selectbox("Choose file format:", ["TXT", "CSV", "JSON"])
    savebutton = st.button("Save Content")

    if savebutton:
        content = st.session_state.refined_content
        if saveformat == "TXT":
            output_file = "scraped_content.txt"
            with open(output_file, "w") as file:
                file.write(content)
            st.success(f"Content saved as {output_file}")
        elif saveformat == "CSV":
            df = pd.DataFrame({"Content": [content]})
            output_file = "scraped_content.csv"
            df.to_csv(output_file, index=False)
            st.success(f"Content saved as {output_file}")
        elif saveformat == "JSON":
            import json
            output_file = "scraped_content.json"
            with open(output_file, "w") as file:
                json.dump({"Content": content}, file, indent=4)
            st.success(f"Content saved as {output_file}")

# Parsing Section
if "refined_content" in st.session_state:
    st.subheader("Process the Extracted Content")
    message = st.text_area("How would you like to process the content?")

    if st.button("Start Parsing"):
        
        st.write("Parsing content...")
        content_segments = splitContent(st.session_state.refined_content)
        parsed_output = extractData(content_segments, message)
        st.subheader("Parsed Output:")
        st.write(parsed_output)
        
