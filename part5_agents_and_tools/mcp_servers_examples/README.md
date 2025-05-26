# MCP Server Cybersecurity Example

This folder contains an example **MCP (Master Control Program)** server inspired
by the "MCP From Scratch" article and adapted for cybersecurity.  The server
exposes endpoints for lightweight port scanning using `nmap` and for asking an
agent questions.  The agent can decide to invoke the scanning tool when needed.

> **Note**: The scanning functionality performs a fast `nmap` scan.  Use it only
> on systems you have permission to test.

## Files

- `mcp_server.py` – FastAPI server exposing `/scan` and `/agent` endpoints.
- `mcp_cyber_agent.py` – LangChain agent with a port scanning tool.

## Usage

1. Install the requirements (including `nmap`):
   ```bash
   sudo apt-get install nmap
   pip install fastapi uvicorn langchain langchain-openai python-nmap python-dotenv
   ```

2. Run the server:
   ```bash
   python mcp_server.py
   ```

3. Send a request to the `/scan` endpoint. For example:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"target": "192.168.1.1"}' http://localhost:8000/scan
   ```

   The response contains a JSON object with the list of open ports.

4. Ask the agent a question:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"question": "Scan 192.168.1.1"}' http://localhost:8000/agent
   ```

