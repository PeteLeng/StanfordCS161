# parse graph data from "dijkstraData.txt"
from collections import defaultdict


def get_data(file_path):
    node_dict = defaultdict(int)
    edge_dict = defaultdict(list)
    with open(file_path, 'r') as f:
        for line in f:
            data = line.split()
            node_dict[data[0]] = 0
            for pair in data[1:]:
                head, distance = pair.split(',')
                edge_dict[data[0]].append((head, int(distance)))
    return node_dict, edge_dict


def main():
    return get_data("dijkstraData.txt")


if __name__ == "__main__":
    nodes, edges = main()
    print('number of nodes:', len(nodes))
