"""Minimal MCP server example for cybersecurity.

This script implements a small FastAPI application that exposes a ``/scan``
endpoint. Given an IP address, it performs a real (but limited) port scan using
the :mod:`python-nmap` module. The goal is to illustrate how an MCP-style server
could be structured for cybersecurity purposes.

.. important::
   Running network scanners may require the ``nmap`` binary to be installed on
   your system and might need elevated privileges depending on the target and
   scan options. This example performs a very basic scan and should only be used
   in controlled environments.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import nmap

app = FastAPI(title="MCP Server for Network Port Scanner")

class ScanRequest(BaseModel):
    target: str

@app.post("/scan")
def scan(req: ScanRequest):
    """Run an ``nmap`` scan against the provided target.

    The scan is intentionally limited (``-F`` for fast scan) to keep it quick.
    If ``nmap`` is not available, an error message is returned instead of
    raising an exception.
    """

    try:
        scanner = nmap.PortScanner()
    except nmap.PortScannerError as exc:
        return {"error": f"nmap not found: {exc}"}
    except Exception as exc:  # pragma: no cover - defensive
        return {"error": f"failed to initialize scanner: {exc}"}

    try:
        # ``-F`` performs a fast scan of fewer ports to reduce runtime.
        scanner.scan(req.target, arguments="-F")
    except Exception as exc:  # pragma: no cover - nmap errors
        return {"error": f"scan failed: {exc}"}

    open_ports = []
    if req.target in scanner.all_hosts():
        for proto in scanner[req.target].all_protocols():
            for port, data in scanner[req.target][proto].items():
                if data.get("state") == "open":
                    open_ports.append(port)

    return {"target": req.target, "open_ports": sorted(open_ports)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
