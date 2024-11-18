# Prompt Chaining Examples

This directory contains examples demonstrating the use of LangChain Expression Language (LCEL) for creating and managing prompt chains.

## Files

### `basic_chain_example.py`
A demonstration of how to create and execute a basic prompt chain using LangChain. This example showcases:
- Creating chains using LCEL (LangChain Expression Language)
- Working with ChatOpenAI models
- Using prompt templates
- Implementing custom processing steps with RunnableLambda
- Parsing and transforming outputs

The example specifically creates a chain that:
1. Takes input about a cybersecurity topic and desired number of tips
2. Processes it through a GPT-4 model
3. Converts the output to uppercase
4. Adds a word count to the final result

## Setup Requirements

1. Install required dependencies:
```bash
pip install langchain langchain-openai python-dotenv
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

To run the basic chain example:
```bash
python basic_chain_example.py
```

## Key Concepts

- **Prompt Templates**: Structured templates for generating consistent prompts
- **LCEL**: LangChain Expression Language for creating chains using the `|` operator
- **RunnableLambda**: Custom transformation steps in the chain
- **Output Parsing**: Converting model outputs into desired formats

## Note

This directory focuses on demonstrating prompt chaining techniques in LangChain, particularly useful for creating complex, multi-step AI interactions with intermediate processing steps.


### `branching_chains.py`
A sophisticated example demonstrating how to implement conditional branching in LangChain chains for vulnerability assessment. This example:
- Classifies security vulnerabilities by severity (critical, high, medium, low)
- Generates appropriate responses based on the classification
- Uses different prompt templates for each severity level
- Implements branching logic using RunnableBranch

Key features:
- Classification chain for determining vulnerability severity
- Specialized response templates for each severity level
- Automated branching based on classification results
- Complete end-to-end processing pipeline

Example usage:
```bash
python branching_chains.py
```

---


I'll explain the `parallel_chains.py` file in detail:

# Parallel Chains for Penetration Testing

This file demonstrates how to create parallel processing chains in LangChain for automated penetration testing workflows. Here's a breakdown of its key components and functionality:

## Purpose
The script creates an automated penetration testing plan by running two parallel chains:
1. A reconnaissance chain that identifies potential information gathering techniques
2. An exploitation chain that suggests possible attack vectors
These are then combined into a comprehensive penetration testing plan.

## Key Components

### 1. Setup and Configuration
```python
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableLambda
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```
- Uses ChatOpenAI with GPT-4 for AI processing
- Implements RunnableParallel for concurrent execution
- Uses RunnableLambda for custom function integration

### 2. Initial Assessment
```python
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert ethical hacker and penetration tester."),
    ("human", "Outline the main characteristics and potential entry points of the target system {target_system}."),
])
```
Creates an initial prompt to gather basic information about the target system.

### 3. Reconnaissance Function
```python
def perform_reconnaissance(target_info):
    '''Generates reconnaissance techniques and tools recommendations'''
    recon_template = ChatPromptTemplate.from_messages([
        ("system", "You are an expert ethical hacker specializing in reconnaissance."),
        ("human", "Given this target information: {target_info}, list potential reconnaissance techniques and tools...")
    ])
```
- Specializes in information gathering techniques
- Generates specific recommendations for reconnaissance tools
- Takes target information as input

### 4. Exploitation Function
```python
def plan_exploitation(target_info):
    '''Generates exploitation methods and tools recommendations'''
    exploit_template = ChatPromptTemplate.from_messages([
        ("system", "You are an expert ethical hacker specializing in exploitation techniques."),
        ("human", "Based on this target information: {target_info}, suggest potential exploitation methods...")
    ])
```
- Focuses on potential attack vectors
- Suggests relevant exploitation tools and methods
- Uses target information to customize recommendations

### 5. Plan Generation
```python
def create_pentest_plan(recon, exploit):
    '''Combines reconnaissance and exploitation into a complete plan'''
    return f"Reconnaissance Phase:\n{recon}\n\nExploitation Phase:\n{exploit}"
```
Merges the outputs from both chains into a structured penetration testing plan.

### 6. Chain Construction
```python
# Define individual branches
recon_branch_chain = (
    RunnableLambda(lambda x: perform_reconnaissance(x)) | model | StrOutputParser()
)
exploit_branch_chain = (
    RunnableLambda(lambda x: plan_exploitation(x)) | model | StrOutputParser()
)

# Combine into final chain
chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"reconnaissance": recon_branch_chain, "exploitation": exploit_branch_chain})
    | RunnableLambda(lambda x: create_pentest_plan(x["branches"]["reconnaissance"], x["branches"]["exploitation"]))
)
```
- Creates parallel processing branches for reconnaissance and exploitation
- Uses LCEL (LangChain Expression Language) for chain composition
- Implements parallel execution using RunnableParallel
- Combines results into a final plan

## Usage
```python
result = chain.invoke({"target_system": "E-commerce website with cloud infrastructure"})
print(result)
```
- Takes a target system description as input
- Outputs a complete penetration testing plan with both reconnaissance and exploitation phases

## Benefits
1. **Parallel Processing**: Improves efficiency by running reconnaissance and exploitation analysis simultaneously
2. **Modular Design**: Easy to modify or extend individual components
3. **Structured Output**: Generates organized, comprehensive penetration testing plans
4. **Specialized Expertise**: Each chain focuses on specific aspects of penetration testing
5. **Scalability**: Can be extended to include additional parallel branches for other testing phases

This script demonstrates advanced LangChain concepts while providing practical utility for automated penetration testing planning.