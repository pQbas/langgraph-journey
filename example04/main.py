'''
Ahora que ya sabemos mejor como funcionan los reducers

Vamos a crear un ejemplo donde vamos a tener un grafo que siempre agrege nuevos mensajes

Todos los mensajes van a ser siempre un string 'Hola'

Para esto se va a usar el reducer que viene por defecto llamado `add_message`

Una de las cosas nuevas que van a aparecer es algo llamado HumanMessage, la cual se va
a revisar en la siguiente sección
'''


from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    messages: Annotated[list, add_messages]


def simple_node(state : State):
    return {"messages" : ["Hola"]}


builder = StateGraph(State)

builder.add_node("simple_node", simple_node)

builder.add_edge(START, "simple_node")
builder.add_edge("simple_node", END)

config = {"configurable" : {'thread_id' : 1}}
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)

initial = { "messages" : ["Primer Mensaje"]}
result = graph.invoke(initial, config)
print(len(result['messages']))

result = graph.invoke(result, config)
print(len(result['messages']))


result = graph.invoke(result, config)
print(len(result['messages']))
