"""Cybersecurity MCP example based on the 'MCP From Scratch' article.

This script shows how to build a minimal Master Control Program (MCP)
for cybersecurity tasks using LangChain. The agent is equipped with a
port scanning tool that leverages `nmap` as well as a simple time
utility. It follows the structure from the original article but focuses
on cybersecurity use cases.
"""

from __future__ import annotations

import datetime
from typing import List

from dotenv import load_dotenv
import nmap
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool, StructuredTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()  # Load environment variables like OPENAI_API_KEY

# ---------------------------------------------------------------------------
# Tool implementations
# ---------------------------------------------------------------------------

def get_current_time(*args, **kwargs) -> str:
    """Return the current time in H:MM AM/PM format."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


def scan_ports(ip: str) -> str:
    """Scan ``ip`` using nmap and return a list of open ports."""
    nm = nmap.PortScanner()
    try:
        nm.scan(ip, arguments="-F")
    except Exception as exc:  # pragma: no cover - depends on system nmap
        return f"Error running nmap: {exc}"

    open_ports: List[int] = []
    if ip in nm.all_hosts():
        for proto in nm[ip].all_protocols():
            open_ports.extend(nm[ip][proto].keys())
    return f"Open ports for {ip}: {sorted(open_ports)}"


class ScanInput(BaseModel):
    ip: str = Field(..., description="IP address to scan")


# Register tools with LangChain
TOOLS = [
    Tool(name="Time", func=get_current_time, description="Get the current time"),
    StructuredTool(
        name="PortScanner",
        func=scan_ports,
        description="Scan an IP address for open ports using nmap",
        args_schema=ScanInput,
    ),
]

# ---------------------------------------------------------------------------
# Agent setup
# ---------------------------------------------------------------------------

PROMPT = hub.pull("hwchase17/react")
LLM = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

AGENT = create_react_agent(llm=LLM, tools=TOOLS, prompt=PROMPT, stop_sequence=True)
AGENT_EXECUTOR = AgentExecutor.from_agent_and_tools(agent=AGENT, tools=TOOLS, verbose=True)


def invoke_agent(question: str) -> str:
    """Run the agent with the provided ``question`` and return its output."""
    result = AGENT_EXECUTOR.invoke({"input": question})
    return result["output"]


if __name__ == "__main__":  # pragma: no cover - example usage
    import sys

    query = sys.argv[1] if len(sys.argv) > 1 else "What time is it?"
    print(invoke_agent(query))
