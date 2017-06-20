#!/usr/bin/python

import argparse
from collections import defaultdict
from pprint import pprint

class Graph:
    def __init__(self):
        self.__nedges = 0
        self.__nvertex = 0
        self.__nodes = set()
        self.__edges = defaultdict(list)
        self.__distances = {}
        self.__visited = {}

    def read_file(self, filename):
        with open(filename) as file:
            self.__nvertex, self.__nedges = file.readline().split()
            
            for _ in range(int(self.__nedges)):
                src, dest, weight = file.readline().split()
                self.__edges[src].append(dest)
                #uncomment for undirect graph
                #self.__edges[dest].append(src)
                #self.__distances[(dest,src)] = int(weight)
                self.__distances[(src, dest)] = int(weight)

            for _ in range(int(self.__nvertex)):
                line = file.readline()
                if len(line) > 1:
                    id, name = line.split()
                    self.__nodes.add(name)

        # print self.__edges

    def dijkstra(self, origin):
        self.__visited = {origin: 0}
        path = {}

        nodes = set(self.__nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in self.__visited:
                    if min_node is None:
                        min_node = node
                    elif self.__visited[node] < self.__visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = self.__visited[min_node]

            for edge in self.__edges[min_node]:
                weight = current_weight + self.__distances[(min_node,edge)]
                if edge not in self.__visited or weight < self.__visited[edge]:
                    self.__visited[edge] = weight
                    path[edge] = min_node

#        pprint(path)
        return path

    def print_path(self, path, origin, dest):
        path_to = []
        vertex = dest
        path_to.append(vertex)
        total_path = 0
        while vertex != origin:
            path_to.append(path[vertex])
            total_path += self.__visited[path[vertex]]
            vertex = path[vertex]

        for v in reversed(path_to):
            print v

        print self.__visited[dest]
#        pprint(path_to)
        return path_to


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the minimum path in a graph")
    parser.add_argument('--file', action='store', required=True, dest='filename',
                        help='File containing edges and vertex')
    parser.add_argument('--origin', action='store', required=True, dest='origin',
                        help='Origin vertex')
    parser.add_argument('--dest', action='store', required=True, dest='dest',
                        help="Destination vertex")
    arguments = parser.parse_args()

    graph = Graph()
    graph.read_file(arguments.filename)
    path = graph.dijkstra(arguments.origin)
    graph.print_path(path, arguments.origin, arguments.dest)
