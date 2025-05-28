'''resources
https://langchain-ai.github.io/langgraph/concepts/low_level/#graphs
https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph
https://langchain-ai.github.io/langgraph/concepts/low_level/#state
'''

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class GraphState(TypedDict):
    count: int

def developer(state):
    print("--------- Developer ----------")
    state["count"] += 1
    return state

def build_graph():
    builder = StateGraph(GraphState)
    builder.add_node("developer", developer)
    builder.add_edge(START, "developer")
    builder.add_edge("developer", END)

    memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)
    return graph


def main():

    graph = build_graph()

    config = {"configurable": {"thread_id": "1"}}
    inputs = {"count": 0}

    result = graph.invoke(inputs, config)

    while True:
        user_input = input(">> ")

        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        count = graph.get_state(config).values["count"]
        result = graph.invoke({"count": count}, config)
        print(result)


if __name__ == "__main__":
    main()
