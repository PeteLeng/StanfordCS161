from get_data import *
from heap import *


def build_heap(node_dict):
    heap = Heap()
    for key in node_dict.keys():
        heap.insert(key, 1000000)
    return heap


def update_heap(key, score, edge_dict, dijkstra_heap):
    # min_key, min_value = dijkstra_heap.get_key(0), dijkstra_heap.get_val(0)
    # dijkstra_heap.delete(min_key)
    for arc in edge_dict[key]:
        head_key, distance = arc[0], arc[1]
        if dijkstra_heap.has_key(head_key):
            arc_score = score + distance
            if arc_score < dijkstra_heap.vals[head_key]:
                # print('- delete node {}; distance {}'.format(head_key, dijkstra_heap.vals[head_key]))
                dijkstra_heap.delete(head_key)
                # print('- insert node {}; distance {}'.format(head_key, arc_score))
                dijkstra_heap.insert(head_key, arc_score)


def get_shortest_path(node_dict, edge_dict, src_key):
    heap = build_heap(node_dict)
    heap.delete(src_key)
    update_heap(src_key, 0, edge_dict, heap)
    # k = 0
    while heap.tree:
    # for i in range(91):
        key, min_score = heap.extract_min()
        # k += 1
        # print('\nExtract Node {}; Distance {}; left {}'.format(key, min_score, len(heap.tree)))
        node_dict[key] = min_score
        update_heap(key, min_score, edge_dict, heap)
    # return heap


if __name__ == '__main__':
    nodes, edges = get_data("dijkstraData.txt")

    # Test build graph
    # h1 = build_heap(nodes)
    # h1.delete('1')

    # Test update heap
    # update_heap('1', 0, edges, h1)

    get_shortest_path(nodes, edges, '1')
    for node in [7,37,59,82,99,115,133,165,188,197]:
        print('Node {}: shortest distance {}'.format(node, nodes[str(node)]))
