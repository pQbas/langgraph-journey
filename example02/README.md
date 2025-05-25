We will create a simple graph that will hold a list of the Fibonacci numbers

Our StateGraph will use TypeDict and have a single entry point and an edge to the 
end node.

It will consist of a single key "Fibonacci" with an initial value of [0]

The fibonacci_reducer function will be used to update the state by adding the next
Fibonacci number to the list

The state will be updated by the custom reducer, while the Developer node will be a noop

