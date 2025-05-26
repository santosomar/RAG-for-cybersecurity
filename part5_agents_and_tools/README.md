# Basic Agent and Tools Examples

This folder contains examples demonstrating the use of LangChain agents and tools.
It has the following files:

- `basic_agent_and_tools.py`: A basic example demonstrating a simple LangChain agent that uses tools to perform actions.
- `basic_agent_and_tools_scanner.py`: A basic example demonstrating a LangChain agent that uses tools to perform network scanning.

---


## Basic Agent and Tools Example

The script `basic_agent_and_tools.py`demonstrates the implementation of a simple LangChain agent that uses tools to perform actions. The example specifically shows how to create an agent that can tell the current time using a custom tool.

## Description

The script showcases:
- Creating a basic LangChain agent using the ReAct (Reason and Action) framework
- Implementing a custom tool (get current time)
- Using ChatOpenAI (GPT-4) as the underlying language model
- Executing the agent with a simple query

## Prerequisites

- Python 3.x
- OpenAI API key (must be set in `.env` file)

## Installation

1. Clone the repository
2. Install the required packages:
```bash
pip install langchain langchain-openai python-dotenv
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script using Python:
```bash
python basic_agent_and_tools.py
```

The script will:
1. Load the necessary environment variables
2. Create a custom time tool
3. Initialize the LangChain agent with the ReAct framework
4. Execute a test query asking for the current time
5. Display the response


## Features

- Custom tool implementation
- Integration with OpenAI's GPT-4 model
- ReAct framework implementation
- Verbose output for debugging and understanding agent behavior

## Note

The example uses `gpt-4.1-mini` as the model. Make sure to update the model name in the code if you want to use a different OpenAI model.


---

## Basic Agent with Network Scanning Tools

The script `basic_agent_and_tools_scanner.py` demonstrates the implementation of a LangChain agent equipped with basic network scanning capabilities using nmap. The agent combines OpenAI's language models with custom tools to perform network scanning operations and time-related queries.

## Features

- Custom agent using LangChain's ReAct (Reason and Action) framework
- Integration with OpenAI's GPT models
- Network scanning capabilities using nmap
- Current time retrieval functionality

## Prerequisites

- Python 3.x
- OpenAI API key (set in `.env` file)
- Required Python packages:
  ```bash
  pip install python-nmap langchain langchain-openai python-dotenv pydantic
  ```
- Nmap installed on your system

## Environment Setup

1. Create a `.env` file in the project root
2. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Available Tools

1. **Time Tool**
   - Returns the current time in H:MM AM/PM format
   - Usage: Ask the agent about the current time

2. **Scanner Tool**
   - Performs network scanning using nmap
   - Input: IP address or range
   - Returns: List of discovered hosts

## Usage Example

```python
# Initialize and run the agent
response = agent_executor.invoke({"input": "Scan the IP address 8.8.8.8"})
```

## Security Considerations

- This script performs network scanning operations which should only be used on networks you have permission to scan
- Always follow responsible security testing practices and applicable laws and regulations
- Be cautious when scanning IP addresses, as unauthorized scanning may be illegal in some jurisdictions

