# 2 Sum


FILE_PATH = "algo1-programming_prob-2sum.txt"


def get_nums(file_path):
    data = []
    with open(file_path, 'r') as f:
        for n in f:
            data.append(int(n.strip()))
    return data


def two_sum(l, t):
    # d = {t - n: n for n in l if t - n != n}
    d = {}
    for n in l:
        if n in d:
            return True
        else:
            if t - n != n:
                d[t - n] = n
            else:
                pass
    return False


def main():
    l = get_nums(FILE_PATH)
    count = 0
    for t in range(-10000, 10001):
        if two_sum(l, t):
            count += 1
            print(t)
        else:
            pass
    return count


if __name__ == '__main__':
    # print(get_nums(FILE_PATH))
    count = main()
    print(count)
