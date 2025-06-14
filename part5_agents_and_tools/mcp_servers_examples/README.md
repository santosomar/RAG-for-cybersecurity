# MCP Server Cybersecurity Example

This folder contains an example of a minimal **MCP (Master Control Program)**
implementation inspired by the "[MCP From Scratch](https://mirror-feeling-d80.notion.site/MCP-From-Scratch-1b9808527b178040b5baf83a991ed3b2)"
article.  The focus here is on cybersecurity use cases.

The example demonstrates how to create a simple FastAPI server that exposes
endpoints backed by a small LangChain agent.  The agent can perform a
lightweight nmap scan or answer general questions using OpenAI models.

> **Note**: This example is intentionally simple and should not be used for real
> security assessments. It is only meant to demonstrate how an MCP-style server
> can be structured for cybersecurity tasks.

## Files

- `mcp_cyber_agent.py` – LangChain agent with port scanning and time tools.
- `mcp_server.py` – FastAPI server exposing `/scan` and `/agent` endpoints.

## Prerequisites

- Python 3.x
- `nmap` installed on your system
- Python packages from `requirements.txt`
- An OpenAI API key set in the `.env` file

## Usage

1. Install the required packages:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. Ensure `nmap` is installed (e.g. `sudo apt-get install nmap`).
3. Run the server:
   First, navigate to the directory containing `mcp_server.py`:
   ```bash
   cd part5_agents_and_tools/mcp_servers_examples
4. Send a request to the `/scan` endpoint. Example:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"target": "192.168.1.1"}' http://localhost:8000/scan
   ```
5. You can also query the agent directly:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"question": "What time is it?"}' http://localhost:8000/agent
   ```
