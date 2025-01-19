from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from concurrent.futures import ThreadPoolExecutor

# Template for extracting specific information
instruction_template = (
    "You are tasked with extracting specific information from the following content: {dom_content}. "
    "Follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract data that directly matches this description: {parse_description}. "
    "2. **No Additional Text:** Exclude any extra comments or explanations. "
    "3. **Empty Response:** If no match is found, return an empty string ('')."
    "4. **Direct Response:** Your response should only include the data requested, with no other text."
)

# Initialize the model and prompt
llama_model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(instruction_template)

def extract_data_with_ollama(dom_chunks, query_description):
    chain = prompt | llama_model

    def process_chunk(chunk):
        try:
            response = chain.invoke({"dom_content": chunk, "parse_description": query_description})
            return response
        except Exception as e:
            print(f"Error processing chunk: {e}")
            return ""

    # Process chunks in parallel
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_chunk, dom_chunks))

    # Combine the results
    return "\n".join(results)
