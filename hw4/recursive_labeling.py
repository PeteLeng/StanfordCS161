from parse_data import *
import sys
import threading

scc_dict = {}


def get_list(filename='graph_ordering.txt'):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append(line.strip())
    return data


def get_scc():
    global nodes
    global node_list
    global scc_dict
    while node_list:
        n = node_list.pop()
        if nodes[n] == 0:
            scc_dict[n] = second_dfs(n)


def second_dfs(node):
    global edges
    global nodes
    # print('running dfs on node:', node)
    count = 1
    nodes[node] = 1
    neighbors = edges[node]
    if not neighbors:
        return 1
    else:
        for n in neighbors:
            if nodes[n] == 0:
                count += second_dfs(n)
    return count


if __name__ == '__main__':
    edges, rev_edges, nodes, rev_nodes = get_graph('SCC.txt')
    node_list = get_list()
    sys.setrecursionlimit(100000)
    threading.stack_size(67108864)
    thread = threading.Thread(target=get_scc)
    thread.start()
    # scc_sorted = sorted(scc_dict.values(), reverse=True)
    # print(scc_sorted[:10])
