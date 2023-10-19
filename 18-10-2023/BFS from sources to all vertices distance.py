from collections import deque

def build_graph(number_of_vertices):
    graph = [[] for i in range(number_of_vertices)]
    #Node 0 edges
    graph[0].append([0,1,5])
    graph[0].append([0,2,8])
    #Node 1 edges
    graph[1].append([1,3,10])
    graph[1].append([1,0,5])
    graph[1].append([1,4,10])
    #Node 2 edges
    graph[2].append([2,3,7])
    graph[2].append([2,0,8])
    #Node 3 edges
    graph[3].append([3,2,7])
    graph[3].append([3,1,10])
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

def bfs(graph,queue,visited,psf):
    while queue:
        #print(psf)
        """removed_node = queue.popleft()
        visited.add(removed_node)
        psf[removed_node]+=str(removed_node)
        print(psf[removed_node])
        for nbr in graph[removed_node]:
            if nbr[1] not in visited:
                queue.append(nbr[1])
                psf[queue[-1]]+=psf[removed_node]
                visited.add(nbr[1])"""
        print(queue)
        removed_node = queue.popleft()
        visited.add(removed_node[0])
        psf=str(removed_node[1])+str(removed_node[0])
        print(psf)
        for nbr in graph[removed_node[0]]:
            if nbr[1] not in visited:
                queue.append([nbr[1],psf])
                visited.add(nbr[1])



def main():
    number_of_vertices = 8
    graph = build_graph(number_of_vertices)
    """print("graph = ",end=" ")
    print(graph)"""
    queue = deque()
    visited = set()
    start = 2
    #psf = ["" for i in range(number_of_vertices)]
    psf=""
    queue.append([start,""])
    bfs(graph,queue,visited,psf)

main()