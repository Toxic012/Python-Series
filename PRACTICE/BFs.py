# import collections

# def bfs(Graph,root):
#     visited = set()
#     queue = collections.deque([root])
#     visited.add(root)
    
#     while queue:
#         print(queue)
#         vertex = queue.popleft()
        
#         for neig in Graph[vertex]:
#             if neig not in visited:
#                 visited.add(neig)
#                 queue.append(neig)
#     print(visited)            

# if __name__ =="__main__":
#     Graph={
#         0:[1,2,4,5],    
#         1:[0,3],
#         2:[0,3,6],
#         3:[1,2],
#         4:[0,5,6],
#         5:[0,4],
#         6:[2,4]
#     }
    
#     bfs(Graph,0)
    
    
from collections import deque

def topo_sort(graph):
    indegree = {i:0 for i in graph}
    # print(indegree)

    for node in graph:
        print(node)
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    queue = deque()

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(order)>0:
        return True
    else:
        return False

graph = {
1:[0],
0:[]
}

print(topo_sort(graph))