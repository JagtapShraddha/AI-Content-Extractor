import streamlit as st
from scraper import scrap_website, clean_content,split_dom_content
# from parse import parse_with_ollama

st.title("AI Web Scraper")

# Input field for URL
url = st.text_input("Enter a Website URL:")

# When the user clicks the 'Scrape' button
if st.button("Scrape"):
    st.write("Scraping the website...")

    # Scrape the website using the dynamic scraper
    result = scrap_website(url)

    if result:
        # Clean the scraped content
        cleaned_content = clean_content(result)
        # Store cleaned content in session state for use in other components
        st.session_state.dom_content = cleaned_content

        # Display cleaned content in a text area inside an expander
        st.subheader("Scraped Data:")
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
        
        # Input box for the user to describe what they want to parse
        parse_description = st.text_area("Describe what you want to parse:")
        
        # Button to trigger the parsing
        if st.button("Parse Content"):

            if parse_description:
                st.write("Parsing the content based on your description...")

                # Split the DOM content into chunks if it's too long
                dom_chunks = split_dom_content(st.session_state.dom_content)

                # Placeholder for parsing function (when implemented)
                # Assuming 'parse_with_ollama' will take the chunks and description
                # result = parse_with_ollama(dom_chunks, parse_description)
                
                # Display parsed results (for now, just a placeholder message)
                st.write(f"Parsed Content:\n\n[Placeholder for parsed result based on description: {parse_description}]")

            else:
                st.error("Please provide a description of what you want to parse.")

    else:
        st.error("No data was scraped. Please check the URL.")

# Function to split content into chunks
