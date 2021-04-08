#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def plain_dp(items, dp, K, cur_i):
    if K < 0:
        # This prevents from ending up with the negative weight
        dp[(K, cur_i)] = -100000000000000
        return -100000000000000
    if cur_i >= len(items):
        dp[(K, cur_i)] = 0
        return 0
    # memoization check
    if (K, cur_i) in dp:
        return dp[K, cur_i]
    # explore
    cand1 = plain_dp(items, dp, K, cur_i + 1)
    cand2 = plain_dp(items, dp, K - items[cur_i].weight, cur_i + 1) + items[cur_i].value

    dp[(K, cur_i)] = max(cand1, cand2)

    return dp[(K, cur_i)]

def reconstruct_path(items, dp, K):
    path = [0] * len(items)

    for i in range(len(items)):
        cand1 = dp[(K, i + 1)]
        cand2 = dp[(K - items[i].weight, i + 1)] + items[i].value

        if cand1 > cand2:
            pass
        else:
            path[i] = 1
            K = K - items[i].weight
    return path

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    '''
    Take best, sample algo
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    '''

    dp = {}
    path = {}
    value = plain_dp(items, dp, capacity, 0)
    taken = reconstruct_path(items, dp, capacity)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
