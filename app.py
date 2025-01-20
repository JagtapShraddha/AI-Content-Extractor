import streamlit as st
import pandas as pd
import json
from scraper import scrapeSite ,cleanseText,splitContent,getBody 
from parse import extractData  

#title
st.title("AI Content Extractor")

#user input
inputUrl = st.text_input("Enter the Website URL:")

# Content Extraction
if st.button("Initiate Scraping"):
    st.write("Processing the website...")
    page_data = scrapeSite(inputUrl)

    if page_data:
        
        text = getBody(page_data)
        refined_content = cleanseText(text)
        st.session_state.refined_content = refined_content

        # Display 
        st.subheader("Extracted Data:")
        with st.expander("Click to See Content"):
            st.text_area("Content Of Page", refined_content, height=300)

    else:
        st.error("Failed to retrieve content from the  URL. Please check the URL and try again.")






# save content in file
if "refined_content" in st.session_state:
    st.subheader("Save Extracted Content")
    saveformat = st.selectbox("Choose file format:", ["TXT", "CSV", "JSON"])
    savebutton = st.button("Save Content")

    if savebutton:
        content = st.session_state.refined_content
        if saveformat == "TXT":
            output_file = "extractedData.txt"
            with open(output_file, "w") as file:
                file.write(content)
            st.success(f"Content saved as {output_file}")
        elif saveformat == "CSV":
            df = pd.DataFrame({"Content": [content]})
            output_file = "extractedData.csv"
            df.to_csv(output_file, index=False)
            st.success(f"Content saved as {output_file}")
        elif saveformat == "JSON":
            
            output_file = "extractedData.json"
            with open(output_file, "w") as file:
                json.dump({"Content": content}, file, indent=4)
            st.success(f"Content saved as {output_file}")

        """ if "refined_content" in st.session_state:
            parse_description=st.text_area("describe what you want to parse")
            if st.button("parse content"): """



# Parsing 
if "refined_content" in st.session_state:
    st.subheader("Process the Extracted Content")
    message = st.text_area("What content you want ")

    if st.button("Start Parsing"):
        
        st.write("Parsing content...")
        content_segments = splitContent(st.session_state.refined_content)
        parsed_output = extractData(content_segments, message)
        st.subheader("Parsed content:")
        st.write(parsed_output)
        
