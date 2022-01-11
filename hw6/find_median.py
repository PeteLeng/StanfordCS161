# Use heap to maintain the median of a sequence of integers
import numpy as np


FILE_PATH = 'Median.txt'


def get_numbers(file):
    d = []
    with open(file, 'r') as f:
        for line in f:
            d.append(int(line.strip()))
    return d


class Heap(object):
    def __init__(self, minOrMax=1):
        self.tree = []
        self.min = minOrMax

    def is_leaf(self, i):
        end = len(self.tree) - 1
        return True if 2 * i + 1 > end else False

    def _swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def bubble_down(self, i):
        while True:
            if self.is_leaf(i):
                break
            end = len(self.tree) - 1
            left_child_pos = 2 * i + 1
            right_child_pos = 2 * i + 2 if left_child_pos < end else left_child_pos
            swap_child_pos = left_child_pos \
                if (self.tree[left_child_pos] <= self.tree[right_child_pos]) == self.min \
                else right_child_pos
            if (self.tree[i] > self.tree[swap_child_pos]) == self.min:
                self._swap(i, swap_child_pos)
                i = swap_child_pos
            else:
                break

    def bubble_up(self, i):
        while True:
            if i == 0:
                break
            parent_pos = int((i - 1) / 2)
            if (self.tree[i] < self.tree[parent_pos]) == self.min:
                self._swap(i, parent_pos)
                i = parent_pos
            else:
                break

    def insert(self, k):
        self.tree.append(k)
        end = len(self.tree) - 1
        self.bubble_up(end)

    def delete(self, i):
        end = len(self.tree) - 1
        if i == end:
            k = self.tree.pop()
        else:
            self._swap(i, end)
            k = self.tree.pop()
            self.bubble_up(i)
            self.bubble_down(i)
        return k

    def extract_extrema(self):
        return self.delete(0)

    def get_extrema(self):
        return self.tree[0]

    def __len__(self):
        return len(self.tree)

    def print_tree(self):
        l = len(self.tree)
        d = int(np.log2(l)) + 1
        n_row = 2 * d - 1
        n_col = 2 ** (d - 1) + 1
        t = np.empty([n_row, n_col]).astype(str)
        t.fill('')
        center = int((n_col - 1) / 2)
        for i in range(d):
            if i == 0:
                t[0, center] = str(self.tree[i])
                t[1, center - 1] = '/'
                t[1, center + 1] = '\\'
            elif i == d - 1:
                left = 2 ** i - 1
                end = l - 1
                length = end - left + 1
                half = 2 ** (i - 1)
                if length <= half:
                    t[2 * i, 0: length] = self.tree[left:]
                else:
                    t[2 * i, 0: half] = self.tree[left: left + half]
                    t[2 * i, center + 1: center + 1 + length - half] = self.tree[left + half:]
            else:
                left = 2 ** i - 1
                mid = left + 2 ** (i - 1)
                right = 2 ** (i + 1) - 1
                half = 2 ** (i - 1)
                t[2 * i, center - half: center] = self.tree[left: mid]
                t[2 * i, center + 1: center + 1 + half] = self.tree[mid: right]
                t[2 * i + 1, center - 2 * half: center] = ['/', '|'] * half
                t[2 * i + 1, center + 1: center + 1 + 2 * half] = ['|', '\\'] * half
        print(t)


class MedianHeap(object):
    def __init__(self):
        self.h_low = Heap(0)
        self.h_high = Heap()

    def insert(self, n):
        if not len(self.h_low) or n <= self.h_low.get_extrema():
            self.h_low.insert(n)
        else:
            self.h_high.insert(n)

        if len(self.h_low) - len(self.h_high) > 1:
            k = self.h_low.extract_extrema()
            self.h_high.insert(k)
        elif len(self.h_low) - len(self.h_high) < -1:
            k = self.h_high.extract_extrema()
            self.h_low.insert(k)

    def get_median(self):
        if len(self.h_low) < len(self.h_high):
            return self.h_high.get_extrema()
        elif len(self.h_low) == len(self.h_high):
            # return (self.h_low.get_extrema() + self.h_high.get_extrema()) / 2
            return self.h_low.get_extrema()
        else:
            return self.h_low.get_extrema()

    def print_tree(self):
        self.h_high.print_tree()
        self.h_low.print_tree()


def main():
    # h = Heap(0)
    # l = [4, 5, 6, 8, 9, 10, 11, 3, 22]
    # # l = [1]
    # for n in l:
    #     h.insert(n)
    # # h.print_tree()
    # print(h.get_extrema())

    h = MedianHeap()
    l = [4, 4, 8, 9, 4, 12, 9, 11, 13, 15, 10, 8, 13, 19, 25, 11, 3, 22]
    # h.print_tree()

    l = get_numbers(FILE_PATH)
    # print(len(l))
    print(l[:10])
    res = []
    for i in range(10000):
        h.insert(l[i])
        m = h.get_median()
        res.append(m)
        # print(m)
    print(f'Final Result: {sum(res) % 10000}')


if __name__ == '__main__':
    main()
