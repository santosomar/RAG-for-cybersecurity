# MCP Server Cybersecurity Example

This folder contains an example of a minimal **MCP (Master Control Program)** server related to cybersecurity. The example is inspired by the "MCP From Scratch" article.

The example demonstrates how to create a simple FastAPI server that exposes an
endpoint to perform a basic cybersecurity task. The server uses ``python-nmap``
to perform a lightweight port scan for a given IP address.

> **Note**: This example is intentionally simple and should not be used for real security assessments. It is only meant to demonstrate how you could structure an MCP-style server for cybersecurity use cases.

## Files

- `mcp_server.py` – Minimal FastAPI server exposing a `/scan` endpoint that runs
  an ``nmap`` fast scan.

## Usage

1. Install the requirements and ensure the ``nmap`` binary is available:
   ```bash
   sudo apt-get install nmap      # or use your package manager
   pip install fastapi uvicorn python-nmap
   ```

2. Run the server:
   ```bash
   python mcp_server.py
   ```

3. Send a request to the `/scan` endpoint. For example:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"target": "192.168.1.1"}' http://localhost:8000/scan
   ```

   The response contains a JSON object with the open ports discovered on the target.

