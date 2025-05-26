"""Minimal MCP server example for cybersecurity.

This FastAPI application exposes endpoints that leverage a simple MCP
agent to perform cybersecurity tasks.  The `/scan` endpoint uses the
agent to run a lightweight nmap scan on the provided target.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from .mcp_cyber_agent import invoke_agent

app = FastAPI(title="MCP Cybersecurity Server")

class ScanRequest(BaseModel):
    target: str

class QueryRequest(BaseModel):
    question: str

@app.post("/scan")
def scan(req: ScanRequest):
    """Run the MCP agent to scan the given target."""
    result = invoke_agent(f"Scan the IP address {req.target}")
    return {"result": result}


@app.post("/agent")
def agent(req: QueryRequest):
    """Run an arbitrary question through the MCP agent."""
    return {"result": invoke_agent(req.question)}


if __name__ == "__main__":  # pragma: no cover - manual execution
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
