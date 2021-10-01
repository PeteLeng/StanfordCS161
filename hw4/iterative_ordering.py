# Implement the DFS search iteratively
from parse_data import *
# EDGE_DICT, REV_EDGE_DICT, NODE_DICT, REV_NODE_DICT = get_graph('SCC.txt')
# NODE_SEQ = [0 for i in range(875714)]


def get_sequence_iter(rev_node_dict, rev_edge_dict):
    # global REV_NODE_DICT
    # global REV_EDGE_DICT
    # global NODE_SEQ
    node_seq = [0]*len(rev_node_dict)
    start = 0
    for node in rev_edge_dict:
        if not rev_node_dict[node]:
            start = dfs_sequencing_iter(node, start, rev_node_dict, rev_edge_dict, node_seq)

    return node_seq


def dfs_sequencing_iter(node, start_idx, rev_node_dict, rev_edge_dict, node_seq):
    # global REV_NODE_DICT
    # global REV_EDGE_DICT
    # global NODE_SEQ

    rev_node_dict[node] = 1
    idx = start_idx
    stack = [node]

    while stack:
        active_node = stack[-1]
        # print('active node {}, index {}'.format(active_node, idx))
        # print(stack)
        is_sink = 1
        for neighbor in rev_edge_dict[active_node]:
            if not rev_node_dict[neighbor]:
                stack.append(neighbor)
                is_sink = 0
            rev_node_dict[neighbor] = 1
        if is_sink:
            node_seq[idx] = active_node
            idx += 1
            stack.pop()

    return idx


if __name__ == "__main__":
    # print('reverse edges', REV_EDGE_DICT)
    # print('reverse nodes', REV_NODE_DICT)
    edges, rev_edges, nodes, rev_nodes = get_graph('SCC.txt')
    ordering = get_sequence_iter(rev_nodes, rev_edges)
    print(ordering[:20])
