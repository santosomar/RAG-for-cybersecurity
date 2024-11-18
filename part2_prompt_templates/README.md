# Prompt Template Examples

This directory contains examples of how to create and use `ChatPromptTemplate` with LangChain for generating prompts for models.

## prompt_template_example.py

This script demonstrates various ways to create a `ChatPromptTemplate` using template strings and lists of messages. The examples are designed to show how to generate prompts for a model, specifically for cybersecurity topics.

### Examples

1. **Prompt from Template**
   - Uses a template string with a placeholder for the topic.
   - Example: "Explain the security concept {topic}."
   - Generates a prompt explaining the security concept of "XSS attacks".

2. **Prompt with Multiple Placeholders**
   - Uses a template string with multiple placeholders for adjectives and vulnerabilities.
   - Example: "Create a {adjective} explanation about a {vulnerability}."
   - Generates a detailed explanation about an XSS vulnerability.

3. **Prompt with System and Human Messages (Using Tuples)**
   - Uses a list of messages with system and human messages as tuples.
   - Example: System message for setting context and human message for specific instructions.
   - Generates obfuscation technique examples for a specified vulnerability type (XSS) and count.

### Usage

Ensure you have the required libraries installed and environment variables set up as specified in the `.env` file.

Run the script:
```bash
python prompt_template_example.py
```

This will execute the examples and print the generated prompts and model responses.

### Dependencies

- `dotenv`: For loading environment variables.
- `langchain`: For creating and managing prompt templates.
- `langchain_openai`: For interacting with the OpenAI model.

### Instructor

Omar Santos [@santosomar](https://github.com/santosomar)

For more information on LangChain Prompt Templates, refer to the [LangChain Prompt Template Documentation](https://python.langchain.com/v0.2/docs/concepts/#prompt-templates).
