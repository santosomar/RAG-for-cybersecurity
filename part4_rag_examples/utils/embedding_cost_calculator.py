# This script calculates the cost of embedding a document using the OpenAI API.

# Instructor: Omar Santos @santosomar

# Import the os library to handle file paths
import os

# Import the tiktoken library to tokenize the text and calculate the cost
import tiktoken

# Define the file path for the document to calculate the embedding cost
file_path = os.path.join(os.path.dirname(__file__), "..", "data", "ssrf.txt")

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"The file {file_path} does not exist. Please check the path."
    )

# Read the content of the file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

tokenizer = tiktoken.get_encoding(
    "cl100k_base"
)  # Use the appropriate encoding for the model you are using

# Tokenize the text and count the tokens using the appropriate encoding for the model you are using
tokens = tokenizer.encode(text)
total_tokens = len(tokens)

# Calculate the cost based on OpenAI's pricing for the model you are using  
cost_per_million_tokens = 0.02  # $0.02 per million tokens
cost = (total_tokens / 1_000_000) * cost_per_million_tokens

# Print the results 
print(f"Total number of tokens: {total_tokens}")
print(f"Estimated cost for processing: ${cost:.6f}")
