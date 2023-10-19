from collections import deque 
def build_graph(vertices):
    graph=[[] for i in range(vertices)]
    
    graph[0].append([0,1,1])
    graph[0].append([0,2,2])
    #Node 1 edges
    graph[1].append([1,3,10])
    graph[1].append([1,0,5])
    graph[1].append([1,4,10])
    #Node 2 edges
    graph[2].append([2,3,7])
    graph[2].append([2,1,8])
    #Node 3 edges
    graph[3].append([3,2,7])
    graph[3].append([3,0,10])
    #Node 4 edges
    graph[4].append([4,7,10])
    graph[4].append([4,5,8])
    graph[4].append([4,1,10])
    #Node 5 edges
    graph[5].append([5,4,8])
    graph[5].append([5,6,3])
    #Node 6 edges
    graph[6].append([6,7,2])
    graph[6].append([6,5,3])
    #Node 7 edges
    graph[7].append([7,6,2])
    graph[7].append([7,4,10])
    #Final Graph
    return graph
def bfs(graph,queue,visited,psf,wsf):
    while queue:
        removed=queue.popleft()
        print("level of ",removed,"is",removed[1])
        visited.add(tuple(removed))
        psf=(removed[1]+str(removed[0]))
        print(psf,queue)
        next_level=removed[2]+1
        for nbr in graph[removed[0]]:
            if nbr[1] not in visited:
                queue.append([nbr[1],psf,next_level])
                visited.add(nbr[1])
def main():
    queue=deque()
    number_of_vertices = 8
    graph = build_graph(number_of_vertices)
    visited = set()
    start=2
    psf=""
    wsf=0
    queue.append([start,""])
    bfs(graph,queue,visited,psf,wsf)
    

main()

