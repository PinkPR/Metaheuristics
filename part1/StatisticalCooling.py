import graph
import random
import math
import copy

class Algo:
    def __init__(self, t, coeff, gr, optimum, max_iter):
        self.iter_cnt = 0
        self.t = t
        self.coeff = coeff
        self.gr = gr
        self.optimum = optimum
        self.max_iter = max_iter

    def ManhattanDistance(self, g):
        s = 0

        for i in g.edges:
            x1 = i[0] % g.vpl
            y1 = i[0] / g.vpl
            x2 = i[1] % g.vpl
            y2 = i[1] / g.vpl
            s = s + abs(x2 - x1) + abs(y2 - y1)

        return 5 * s

    def MetropolisCrit(self, delta, t):
        if delta <= 0:
            return True
        if random.random() <= math.exp(float(-delta) / t):
            return True
        return False

    def GetNewGraph(self, g):
        edge1 = int(g.vertices_cnt * random.random())
        edge2 = int(g.vertices_cnt * random.random())
        g2 = copy.deepcopy(g)


        for i in range(len(g.edges)):
            for j in range(2):
                if g.edges[i][j] == edge1:
                    g2.edges[i][j] = edge2
                if g.edges[i][j] == edge2:
                    g2.edges[i][j] = edge1

        return g2

    def Run(self):
        if True:
            # break case
            if self.t == 0 or self.iter_cnt >= self.max_iter:
                return (None, 0)

            g2 = self.GetNewGraph(self.gr)
            m1 = self.ManhattanDistance(g2)
            m2 = self.ManhattanDistance(self.gr)

            # optimum reached
            if m2 == self.optimum:
                return (None, m2)

            delta = m1 - m2

            metro = self.MetropolisCrit(delta, self.t)
            if metro:
                self.gr = g2
                #print 'T = ' + str(self.t) + '\t' + 'Iter : ' + str(self.iter_cnt)

            self.iter_cnt = self.iter_cnt + 1
            self.t = self.t * self.coeff

        return (self.gr, m2)
