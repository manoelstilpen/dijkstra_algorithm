## Dijkstra Algorithm

Dijkstra Shortest Path implementation in Python based on: https://gist.github.com/econchick/4666413
This program has three parameters:

- -file file: specifies the file containing the graph (should follow the format in input.txt)
- --origin node: specifies the initial node
-  --dest node: specifies the destination node -- used for printing the shortest path

### Input file format

The input file format should follow the model below:

The first line should contain how many nodes(**n**) and edges(**m**) you have
The next **m** lines specifies the edges, for example:
```
a   b   15
```
In this case, we have ```a -> b``` with 15 of weight.

In the end you should specify your **n** nodes as follow:
```0 a```
```1 b```
