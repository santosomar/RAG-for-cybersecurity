"""MCP server example for cybersecurity tasks.

This FastAPI application exposes endpoints to perform lightweight port scanning
and to interact with an agent capable of deciding when to run a scan.  The
implementation is inspired by the "MCP From Scratch" article but adapted for
cybersecurity use cases.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nmap

from mcp_cyber_agent import agent_executor

app = FastAPI(title="MCP Cybersecurity Server")

class ScanRequest(BaseModel):
    target: str


class AgentRequest(BaseModel):
    question: str

@app.post("/scan")
def scan(req: ScanRequest):
    """Perform a fast nmap scan and return open ports."""
    try:
        open_ports = scan_ports(req.target, arguments="-F")
        return {"target": req.target, "open_ports": sorted(set(open_ports))}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
@app.post("/agent")
def agent(req: AgentRequest):
    """Ask the MCP agent a question. It may choose to run a scan."""
    try:
        result = agent_executor.invoke({"input": req.question})
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
