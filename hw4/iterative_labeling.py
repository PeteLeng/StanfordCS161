# Second DFS run to label all the SCCs, implemented iteratively
import time
from parse_data import get_graph
from iterative_ordering import get_sequence_iter
from collections import defaultdict


def get_labeling_iter(node_dict, edge_dict, node_seq):
    # global NODE_DICT
    # global EDGE_DICT

    scc_dict = defaultdict(list)
    scc_size_dict = defaultdict(int)
    for node in reversed(node_seq):
        if not node_dict[node]:
            dfs_labeling_iter(node, node_dict, edge_dict, scc_dict, scc_size_dict)

    return scc_dict, scc_size_dict


def dfs_labeling_iter(node, node_dict, edge_dict, scc_dict, scc_size_dict):
    # global NODE_DICT
    # global EDGE_DICT

    node_dict[node] = 1
    stack = [node]
    # scc_dict[node].append(node)

    while stack:
        active_node = stack[-1]
        is_sink = 1
        for neighbor in edge_dict[active_node]:
            if not node_dict[neighbor]:
                # Labeling should be done when popped from stack
                # rather than when added to stack
                # scc_dict[node].append(neighbor)
                stack.append(neighbor)
                node_dict[neighbor] = 1
                is_sink = 0

        if is_sink:
            scc_dict[node].append(active_node)
            scc_size_dict[node] += 1
            stack.pop()


if __name__ == '__main__':
    # Read data
    read_start_time = time.time()
    edges, rev_edges, nodes, rev_nodes = get_graph('SCC.txt')
    read_end_time = time.time()
    print('Time to read {} nodes and {} edges: '.format(len(rev_nodes), len(rev_edges)),
          read_end_time - read_start_time)

    # Get ordering
    ordering_start_time = time.time()
    ordering = get_sequence_iter(rev_nodes, rev_edges)
    ordering_end_time = time.time()
    print('Time to oder {} nodes and {} edges: '.format(len(rev_nodes), len(rev_edges)),
          ordering_end_time-ordering_start_time)

    # Get labeling
    labeling_start_time = time.time()
    sccs, scc_size = get_labeling_iter(nodes, edges, ordering)
    labeling_end_time = time.time()
    print('Time to label {} nodes and {} edges: '.format(len(nodes), len(edges)),
          labeling_end_time-labeling_start_time)

    # Sort
    sorting_start_time = time.time()
    sorted_scc_size = sorted(scc_size.values(), reverse=True)
    sorting_end_time = time.time()
    print('Time to sort scc: ', sorting_end_time - sorting_start_time)
    # print(sccs)
