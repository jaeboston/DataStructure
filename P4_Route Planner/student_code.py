import math
import heapq

def shortest_path(M,start,goal):
    print("shortest path called")

    #: init variables
    visited_list = [] #: contains node visited
    min_queue = [] #: contains tutple with (distance (g+h), node)
    
    
    #: add the start node
    start_g = 0
    start_h = compute_distance(M.intersections[start], M.intersections[goal])
    start_path = [start]
    
    min_queue.append((start_g+start_h, start_path, start_g, start_h)) #: tuple : (g+h, path, g, h)
  
    
    while min_queue:
        #print(f'min_queue={min_queue}')
    
        (g_h, path, g, h) = heapq.heappop(min_queue) #: get the min g+h tuple
        node = path[-1]
        if node == goal:
            return path
        visited_list.append(node)
        
        #print(f'M.roads[node]={M.roads[node]}')
            
        for neighbor_node in M.roads[node]:
            if neighbor_node not in visited_list or neighbor_node == goal:
            
                #: compute path
                newpath = path.copy()
                newpath.append(neighbor_node)
                #: compute g
                new_g = g + compute_distance(M.intersections[node], M.intersections[neighbor_node])
                #: compute h
                new_h = compute_distance(M.intersections[neighbor_node], M.intersections[goal])

                heapq.heappush(min_queue, (new_g+new_h, newpath , new_g, new_h)) #: tuple : (g+h, path, g, h)
    
    return []   
              
  
                


def compute_distance(cord1, cord2):
    
    x1 = cord1[0]
    x2 = cord2[0]
    
    y1 = cord1[1]
    y2 = cord2[1]
    
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    