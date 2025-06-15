# Prompt Template Examples

This directory contains examples and documentation about creating and using `ChatPromptTemplate` with LangChain for generating prompts for models, with a focus on cybersecurity applications.

## Files Overview

### chat_prompt_template.py
Demonstrates how to create and use chat prompt templates to generate responses to user questions. This script shows how to work with LangChain's chat templates and includes examples of system messages, user inputs, and AI responses.

### messages_placeholders.py
Illustrates the use of message placeholders in prompt templates, allowing for dynamic inclusion of message lists within prompts. This is particularly useful when building interactive chat systems or maintaining conversation history.

### prompt_template_example.py
Provides various examples of creating `ChatPromptTemplate` using template strings and lists of messages. The examples focus on cybersecurity-specific scenarios and show different ways to structure prompts for security-related tasks.

### prompt_engineering_techniques.md
A comprehensive guide documenting various advanced prompting techniques for enhancing LLM interactions. Includes detailed information about:
- Chain-of-Thought reasoning
- Tree-of-Thought approaches
- ReAct patterns
- Self-Correction methods
- System-Level Instructions
- Contextual Priming
Each technique is explained with implementation ideas and integration notes for LangChain Expression Language (LCEL) and LangGraph.

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
