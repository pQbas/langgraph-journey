'''
En este tutorial se va a crear un grafo que tenga como estado una lista de números
enteros

Esta lista de números irá aumentando cada vez que se ejecute el grafo

[0] 
[0,1]
[0,1,2]
[0,1,2,3]
'''

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing import Annotated


def my_reducer(current_state: list[int] | None, update_state: list[int] | None ) -> list[int]:
    if current_state is None:
        current_state = [] 
    elif update_state is None:
        return current_state
    print('-------------------------')
    print('current:', current_state)
    print('update:',update_state)
    # new_state = update_state
    # new_state = current_state + update_state
    # new_state = [update_state[0]]
    # new_state = current_state + [update_state[-1]]
    new_state = list(set(current_state + update_state))
    return new_state

class GraphState(TypedDict): 
    numbers: Annotated[list[int], my_reducer]


def add_number_node(state: GraphState):
    new_number = state["numbers"][-1] + 1
    return { "numbers" : [new_number] }


builder = StateGraph(GraphState)

builder.add_node('developer', add_number_node)
builder.add_edge(START, 'developer')
builder.add_edge('developer', END)

config = {'configurable' : { 'thread_id' : 1}}
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)

print(">> First call")
inputs = {"numbers" : [0] }
result = graph.invoke(inputs, config)
print(result)

print(">> Second call")
numbers = graph.get_state(config).values["numbers"]
result = graph.invoke({"numbers" : numbers}, config)
print(result)


print(">> Third call")
numbers = graph.get_state(config).values["numbers"]
result = graph.invoke({"numbers" : numbers}, config)
print(result)
