'''
We will create a simple graph that will hold a list of the Fibonacci numbers

Our StateGraph will use TypeDict and have a single entry point and an edge to the 
end node.

It will consist of a single key "Fibonacci" with an initial value of [0]

The fibonacci_reducer function will be used to update the state by adding the next
Fibonacci number to the list

The state will be updated by the custom reducer, while the Developer node will be a 
noop


'''
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing import Annotated

def fibonacci(n:int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2) 

def fibonacci_reducer(current: list[int], update: int | None) -> list[int]:
    if current is None:
        current  = []
    if update is None:
        return current
    return sorted(list(set(current + update)))

class GraphState(TypedDict):
    fibonacci: Annotated[list[int], fibonacci_reducer]

builder = StateGraph(GraphState)

def developer(state):
    # print('inside the node:', state["fibonacci"])
    return state

builder.add_node("developer", developer)

builder.add_edge(START, "developer")
builder.add_edge("developer", END)

config = {"configurable" : {"thread_id" : 1}}
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


initial = {"fibonacci" : [0]}
result = graph.invoke(initial, config)

print(result)
n = 0
while True:
    next_fibonacci = fibonacci(n)
    print("Next fibonacci number", next_fibonacci)

    result = graph.invoke({"fibonacci" : [next_fibonacci]}, config)
    print("State:", result)

    n += 1

    user_input = input(">> ")

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Good bye")
        break
