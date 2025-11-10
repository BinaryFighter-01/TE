#A * search Algo

#Graph

graph= {
 'A': {'B': 1, 'C': 3},
 'B': {'C': 2, 'D': 4},
 'C': {'F': 2},
 'D': {},
 'E': {'F': 5},
 'F': {}

}

#Heurisitic Values

h = {
'A': 6,
'B': 5,
'C': 1,
'D': 3,
'E': 4,
'F': 0,

}


def a_star(start, goal):
    open_set = [start]
    closed_set = set()
    g = {start: 0}
    parent = {start:None}

    while open_set:
        node = min(open_set, key= lambda x: g[x]+h[x])
        if node == goal:
            path=[]
            while node:
                path.append(node)
                node = parent[node]
            print("Path:", "--->".join(path[::-1] ))
            return    


        open_set.remove(node)
        closed_set.add(node)


        for neighbour, cost in graph[node].items():
            if neighbour in closed_set:
                continue

        new_g= g[node]+cost
        if neighbour not in open_set or new_g <g.get(neighbour, float('inf')):
            g[neighbour] = new_g
            parent[neighbour] = node
            if neighbour not in open_set:
                open_set.append(neighbour)
                


    print("No Path Found ")


#Main
print("A* Traversal:  ")
a_star('A','F') 	
