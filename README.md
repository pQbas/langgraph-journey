# LangGraph Journey

Set of examples developed in langgraph to learn more about this library.

<details> <summary> Example 1 : States and Nodes</summary>

This example demonstrates a simple graph execution using a `GraphState` and a single `Developer` node.

The `GraphState` is initialized as a `TypeDict` with a single key, "count", starting at 0. It has one entry point and a direct edge to the end node.

The `Developer` node increments the "count" in the `GraphState` by 1 and returns the updated state.

Memory is added to the graph to persist the state between executions.

A visualization of the graph is generated to illustrate its structure.

Finally, the graph is executed, and the resulting "count" value is printed.

</details>
