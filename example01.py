'''
The GraphState will be created with a TypeDict and have a single entry point
and an edge to the end node.

It will consist of a single key "count" with an initial value of 0.

The Developer node will increment the count by 1 and return the state.

We will add memory to the graph to save the state of the graph.

Then, we will create a visualization of the graph.

Finally, we will run the graph and print the result.
'''

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class GraphState(TypedDict):
    count: int

builder = StateGraph(GraphState)

def developer(state):
    print('--------- Developer ----------')
    state['count'] += 1
    return state

builder.add_node('developer', developer)
builder.add_edge(START, 'developer')
builder.add_edge('developer', END)

config = {'configurable' : { 'thread_id' : 1}}
memory = MemorySaver()


graph = builder.compile(checkpointer=memory)
inputs = {"count" : 0 }
result = graph.invoke(inputs, config)
print(result)

while True:
    user_input = input(">> ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    count = graph.get_state(config).values["count"]
    result = graph.invoke({"count" : count}, config)
    print(result)
