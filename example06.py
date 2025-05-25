'''
En esta vamos a entender cómo crear un chatbot usando langgraph

'''
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class State(TypedDict):
    messages: Annotated[list, add_messages]

def llm(state : State):
    return {"messages" : model.invoke(state["messages"])}


builder = StateGraph(State)

builder.add_node("llm", llm)
builder.add_edge(START, 'llm')
builder.add_edge('llm', END)

graph = builder.compile()

# Ejemplo de chatbot simple

user_input = input(">> ")
state = {
    "messages": [
        SystemMessage(content="Eres un asistentente de IA, tu nombre es Cubasky"),
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
