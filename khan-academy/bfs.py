#!/usr/bin/env python3

queue = []

def enqueue(obj):
    queue.append(obj)

def dequeue():
    first = queue[0]
    queue.remove(first)
    return first

def empty():
    return len(queue) == 0

def do_bfs(graph, source):
    bfs_info = [{'distance': None, 'predecessor': None} for _ in graph]
    bfs_info[source]['distance'] = 0

    enqueue(source)

    while (not empty()):
        actual = dequeue()

        for neighboor in graph[actual]:

            if (bfs_info[neighboor]['distance'] == None):
                bfs_info[neighboor]['distance'] = \
                    bfs_info[actual]['distance'] + 1
                bfs_info[neighboor]['predecessor'] = actual
                enqueue(neighboor)

    return bfs_info

def main():
    graph = [
            [1],
            [0, 4, 5],
            [3, 4, 5],
            [2, 6],
            [1, 2],
            [1, 2, 6],
            [3, 5],
            []
            ]
    
    bfs_info = do_bfs(graph, 3)
    
    for v in range(len(graph)):
        print("vertex ", v, ": distance = ", bfs_info[v]['distance'],
            ", predecessor = ", bfs_info[v]['predecessor'])


if __name__ == "__main__":
    main()
