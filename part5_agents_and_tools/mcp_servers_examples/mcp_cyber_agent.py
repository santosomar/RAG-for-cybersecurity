from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import Tool
from langchain.tools import StructuredTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import nmap
import datetime

load_dotenv()


def get_current_time() -> str:
    """Return the current time in H:MM AM/PM format."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


def scan_ports(target: str):
    """Perform a fast nmap scan of the target and return open ports."""
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-F")
    open_ports = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            open_ports.extend(nm[host][proto].keys())
    return sorted(set(open_ports))


class ScanInput(BaseModel):
    target: str = Field(..., description="IP address or host to scan")


tools = [
    Tool(name="Time", func=get_current_time, description="Get the current time"),
    StructuredTool.from_function(
        name="PortScanner",
        func=scan_ports,
        description="Scan a host for open ports",
        args_schema=ScanInput,
    ),
]

prompt = hub.pull("hwchase17/react")
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
)

