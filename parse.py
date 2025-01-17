from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template for extracting specific information
instruction_template = (
    "You are tasked with extracting specific information from the following content: {dom_content}. "
    "Follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract data that directly matches this description: {parse_description}. "
    "2. **No Additional Text:** Exclude any extra comments or explanations. "
    "3. **Empty Response:** If no match is found, return an empty string ('')."
    "4. **Direct Response:** Your response should only include the data requested, with no other text."
)

# Initialize the model
llama_model = OllamaLLM(model="llama3.2")

def extract_data_with_ollama(dom_chunks, query_description):
    # Create a prompt from the template
    prompt = ChatPromptTemplate.from_template(instruction_template)
    chain = prompt | llama_model

    results = []

    # Process each chunk of the DOM content
    for index, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": query_description})
        print(f"Processing batch {index} of {len(dom_chunks)}")
        results.append(response)
    
    # Combine the results from all chunks
    return "\n".join(results)

