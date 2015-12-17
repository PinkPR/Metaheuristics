import random
import copy

def print_out(vert_cnt, edges, filename):
    LF = '\n'
    f = open(filename, 'w')
    f.write(str(vert_cnt) + LF)
    f.write(str(len(edges)) + LF)

    for couple in edges:
        f.write(str(couple[0]) + ':' + str(couple[1]) + LF)

    f.close()

def shake_once(vert_cnt, edges):
    edge1 = int(vert_cnt * random.random())
    edge2 = int(vert_cnt * random.random())

    for i in range(len(edges)):
            for j in range(2):
                if edges[i][j] == edge1:
                    edges[i][j] = edge2
                elif edges[i][j] == edge2:
                    edges[i][j] = edge1

    return edges

def shake(vert_cnt, edges, iters):
    for i in range(iters):
        edges = shake_once(vert_cnt, edges)

    return edges

def generate_25(iters):
    edges = []
    vert_cnt = 25
    width = 5

    for i in range(vert_cnt):
        if i < vert_cnt - width:
            edges.append([i, i + width])
        if(i + 1) % width:
            edges.append([i, i + 1])

    return shake(25, edges, iters)

edges = generate_25(250)
print_out(25, edges, 'perfect_graph')
