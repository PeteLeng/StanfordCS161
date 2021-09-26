import time

def get_data(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append(line.split())
    return data

def get_graph(filename):
    with open(filename, 'r') as f:
        edges = {}
        rev_edges = {}
        nodes = {}
        rev_nodes = {}
        count = 0
        for line in f:
            n1, n2 = line.strip('\n').split()

            # update nodes
            if n1 not in nodes:
                nodes[n1] = 0
                rev_nodes[n1] = 0
                edges[n1] = []
                rev_edges[n1] = []
            if n2 not in nodes:
                nodes[n2] = 0
                rev_nodes[n2] = 0
                edges[n2] = []
                rev_edges[n2] = []

            # update edges
            if n1 in edges:
                edges[n1].append(n2)

            # update reverse edges
            if n2 in rev_edges:
                rev_edges[n2].append(n1)

            count += 1
    print('number of lines:', count)
    return edges, rev_edges, nodes, rev_nodes

if __name__ == '__main__':
    # start = time.time()
    # data = get_data('SCC.txt')
    # end = time.time()
    # print(data[:10])
    # print('time to parse the data: {}'.format(end-start))

    start = time.time()
    edges, rev_edges, nodes, rev_nodes = get_graph('SCC.txt')
    end = time.time()
    print('number of nodes: ', len(nodes))
    print('number of edges', sum([len(edges[node]) for node in edges]))
    print('number of reversed edges', sum([len(rev_edges[node]) for node in rev_edges]))
    print('time to build the graph: ', end-start)

    # edges, rev_edges, nodes = get_graph('test2.txt')
    # print('number of nodes: ', len(nodes))
    # print('number of edges', sum([len(edges[node]) for node in edges]))
    # print('number of reversed edges', sum([len(rev_edges[node]) for node in rev_edges]))
