from parse_data import *
# from get_order import *
import time
import sys
import threading


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


def dfs_fast(node):
    global rev_edges
    global rev_nodes
    global node_list
    global idx
    rev_nodes[node] = 1
    neighbors = rev_edges[node]
    if not neighbors:
        node_list[idx] = node
        idx += 1
    else:
        for n in neighbors:
            if rev_nodes[n] == 0:
                dfs_fast(n)
        node_list[idx] = node
        idx += 1


def get_order_fast():
    global rev_nodes
    for node in rev_nodes.keys():
        if rev_nodes[node] == 0:
            dfs_fast(node)


def second_dfs(node):
    global edges
    global nodes
    count = 1
    nodes[node] = 1
    neighbors = edges[node]
    if not neighbors:
        return 1
    else:
        for n in neighbors:
            if not nodes[n]:
                count += second_dfs(n)
    return count


def get_scc():
    global nodes
    global node_list
    global scc_dict
    print('last 10 elements in node list', node_list[-10:])
    while node_list:
        n = node_list.pop()
        print('running dfs on ', n)
        if nodes[n] == 0:
            scc_dict[n] = second_dfs(n)


if __name__ == '__main__':
    # node_list = [0 for i in range(64900)]
    # idx = 0
    # edges, rev_edges, nodes, rev_nodes = get_graph('test.txt')
    # start = time.time()
    # res = get_order(rev_edges, rev_nodes)
    # end = time.time()
    # print('Runtime on 212019 edges and 64900 nodes', end-start)
    # Runtime on 212019 edges and 64900 nodes 0.0375363826751709

    # edges, rev_edges, nodes = get_graph('test.txt')
    # start = time.time()
    # res = get_order_fast()
    # end = time.time()
    # print(res[:10])
    # print('dfs_fast runtime on 212019 edges and 64900 nodes', end-start)
    # dfs_fast runtime on 212019 edges and 64900 nodes 0.04773855209350586

    # edges, rev_edges, nodes = get_graph('test2.txt')
    # start = time.time()
    # thread = threading.Thread(target=get_order_fast)
    # thread.start()
    # # res = get_order_fast()
    # end = time.time()
    # print(node_list[:30])
    # print('dfs_fast runtime on 1523182 edges and 336127 nodes', end-start)
    # dfs_fast runtime on 1523182 edges and 336127 nodes 0.015808582305908203

    sys.setrecursionlimit(100000)
    threading.stack_size(67108864)
    node_list = [0 for i in range(875714)]
    idx = 0
    edges, rev_edges, nodes, rev_nodes = get_graph('SCC.txt')
    start = time.time()
    thread = threading.Thread(target=get_order_fast)
    thread.start()
    end = time.time()
    print('dfs_fast runtime on 5105043 edges and 875714 nodes', end - start)

    # with open('graph_ordering.txt', 'w') as f:
    #     for node in node_list:
    #         f.write(node+'\n')

    # scc_dict = {}
    # thread2 = threading.Thread(target=get_scc())
    # thread2.start()
    # sorted_scc = sorted(scc_dict, keys=lambda x:scc_dict[x], reverse=False)
