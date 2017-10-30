#!/usr/local/bin/python

import numpy as np


def similarity(f1, f2):
    sim_mat = []
    node_mat = []
    for i in f1:
        temp = []
        temp_c = []
        for j in f2:
            temp_mat,c = sim_distance(i, j)
            temp.append(temp_mat)
            temp_c.append(c)
        sim_mat.append(temp)
        node_mat.append(temp_c)
    for i in sim_mat:
        print i

    for i in node_mat:
        print i


def sim_distance(h1, h2):
    c = 0
    n = max(len(h1), len(h2))
    s_d = 0.0
    for i in range(0, n):
        s_d_node = 0.0
        if h1[i] is not None and h2[i] is not None:
            m = len(h1[i])
            for j in range(0,m):
                s_d_node += pow(h1[i][j] - h2[i][j], 2.0)
            s_d += np.sqrt(s_d_node)
            c += 1
    return s_d, c

if __name__ == '__main__':
    f1 = [[[3, 4], [5, 8], [7, 1]], [[6, 14], [21, 12], [3, 15]], [[13, 12], [11, 14],None]]
    f2 = [[[13, 11], [12, 5], None], [[8, 17], [16, 24], [2,3]]]
    print f1
    similarity(f1, f1)
