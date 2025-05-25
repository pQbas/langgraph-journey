from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def sum(a:int, b:int) -> int:
    '''Returns the sum of two numbers'''
    print('Tool execution')
    return a + b

tools = [sum]

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash").bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def llm(state : State):
    return {"messages" : model.invoke(state["messages"])}

def should_continue(state: State):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END



builder = StateGraph(State)

builder.add_node("llm", llm)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, 'llm')
builder.add_conditional_edges("llm", should_continue, ['tools', END] )
# builder.add_edge('tools', END)
builder.add_edge('tools', 'llm')

graph = builder.compile()

# Ejemplo de chatbot simple

user_input = input(">> ")
state = {
    "messages": [
        SystemMessage(content="Eres un asistentente de IA, tu nombre es Cubasky, posees una tool de suma llamada sum"),
        HumanMessage(content = user_input)
    ]
}

state = graph.invoke(state)
print('response:', state["messages"][-1].content)

while True:
    user_input = input(">> ")
    state["messages"].append(HumanMessage(content=user_input))
    state = graph.invoke(state)
    print('response:', state["messages"][-1].content)
