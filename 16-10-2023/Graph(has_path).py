vertice=3
graph=[[[]] for i in range(vertice)]
graph[0]=[[0,1,3],[0,2,3]]
graph[1]=[[1,0,3],[1,2,3]]
graph[2]=[[2,0,3],[2,1,3]]
visited=[[False for i in range(vertice)]]
def has_path(graph,scr,des,visited):
    if scr==des:
        return True
    for i in graph[scr]:
        if visited==False:
            visited[scr]=True
            result=has_path(graph,i[scr],des,visited)
            if result==True:
                return True
    return False
print(has_path(graph,0,0,visited))





