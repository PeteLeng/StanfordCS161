# Compute strongly connected components
# Double DFS
# Compute the time ordering in the first pass
# - reverse the edges

# Compute the components in the second pass
import numpy as np

def dfs(edges, nodes, node):
    global node_list
    global idx
    nodes[node] = 1
    neighbors = edges[node]
    if not neighbors:
        node_list[idx] = node
        idx += 1
    else:
        for n in neighbors:
            if nodes[n] == 0:
                dfs(edges, nodes, n)
        node_list[idx] = node
        idx += 1

def get_order(edges, nodes):
    # idx = 0
    for node in nodes.keys():
        if nodes[node] == 0:
            dfs(edges, nodes, node)
    return node_list

if __name__ == '__main__':
    nodes = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
    edges = {'1':['2'], '2':['3', '4'], '3':['1'], '4':['6'], '5':['4'], '6':['5']}
    node_list = [0 for i in range(len(nodes))]
    idx = 0
    l1 = get_order(edges, nodes)
    print(l1)
    print(nodes)
