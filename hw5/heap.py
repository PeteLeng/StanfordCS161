# implement the heap data structure
from collections import defaultdict


class Heap(object):
    def __init__(self):
        self.tree = []
        self.vals = defaultdict(int)
        self.idxs = defaultdict(int)

    def swap(self, idx1, idx2):
        key1, key2 = self.tree[idx1], self.tree[idx2]
        self.tree[idx1], self.tree[idx2] = self.tree[idx2], self.tree[idx1]
        self.idxs[key1] = idx2
        self.idxs[key2] = idx1

    def get_key(self, idx):
        return self.tree[idx]

    def get_val(self, idx):
        key = self.get_key(idx)
        return self.vals[key]

    def get_idx(self, key):
        return self.idxs[key]

    def get_min_idx(self, idx1, idx2):
        if self.get_val(idx1) > self.get_val(idx2):
            return idx2
        return idx1

    def _add(self, key, val):
        self.tree.append(key)
        self.idxs[key] = len(self.tree)-1
        self.vals[key] = val

    def _pop(self):
        key = self.tree.pop()
        del self.vals[key]
        del self.idxs[key]

    def bubble_up(self, node_idx):
        while True:
            if node_idx == 0:
                break
            parent_idx = int((node_idx-1)/2)
            if self.get_val(parent_idx) > self.get_val(node_idx):
                self.swap(node_idx, parent_idx)
                node_idx = parent_idx
            else:
                break

    def bubble_down(self, node_idx):
        while True:
            left_child_idx = 2 * (node_idx + 1) - 1
            right_child_idx = 2 * (node_idx + 1)
            restored = False
            if left_child_idx == len(self.tree)-1:
                if self.get_val(node_idx) > self.get_val(left_child_idx):
                    self.swap(node_idx, left_child_idx)
                    node_idx = left_child_idx
                else:
                    restored = True
            elif left_child_idx < len(self.tree)-1:
                min_idx = self.get_min_idx(left_child_idx, right_child_idx)
                if self.get_val(node_idx) > self.get_val(min_idx):
                    self.swap(node_idx, min_idx)
                    node_idx = min_idx
                else:
                    restored = True
            else:
                break

            if restored:
                break

    def insert(self, leaf_key, leaf_val):
        self.tree.append(leaf_key)
        self.idxs[leaf_key] = len(self.tree) - 1
        self.vals[leaf_key] = leaf_val
        self.bubble_up(self.idxs[leaf_key])

    def delete(self, node_key):
        node_idx = self.idxs[node_key]
        last_idx = len(self.tree) - 1
        self.swap(node_idx, last_idx)
        self._pop()
        self.bubble_up(node_idx)
        self.bubble_down(node_idx)

    def get_tree(self):
        return [self.vals[k] for k in self.tree]

    def print_tree(self):
        depth = 0
        k = 0
        while k < len(self.tree):
            i = min(k+2**depth, len(self.tree))
            print([self.vals[key] for key in self.tree[k:i]])
            k = i
            depth += 1
        print('\n')


if __name__ == '__main__':
    h1 = Heap()
    list = [4, 4, 8, 9, 4, 12, 9, 11, 13]
    for i,v in enumerate(list):
        h1.insert(i, v)
    print(h1.get_tree())
    print(h1.vals)
    h1.print_tree()

    # Test insert
    h1.insert(9, 2)
    print('Insert 2')
    h1.print_tree()

    print('Insert 3, 6')
    h1.insert(10, 3)
    h1.insert(11, 6)
    h1.print_tree()

    # Test delete
    print('Delete 2')
    h1.delete(9)
    h1.print_tree()
