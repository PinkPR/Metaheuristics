import sys

class Graph:
    def __init__(self, file_path):
        self.vertices = []
        self.edges = []
        self.vpl = 5
        self.vertices_cnt = 0

        f = open(file_path, 'r')
        self.vertices_cnt = int(f.readline())
        edges_cnt = int(f.readline())

        for i in range(edges_cnt):
            edg = map(int, f.readline()[:-1].split(':'))

            if edg[0] < 0 or edg[0] >= self.vertices_cnt:
                print "Bad edge id : " + str(edg[0])
                sys.exit(1)
            if edg[1] < 0 or edg[1] >= self.vertices_cnt:
                print "Bad edge id : " + str(edg[1])
                sys.exit(1)

            self.edges.append(edg)

        f.close()

    def DrawLines(self, window_size, func):
        sz = (window_size[0] - 40 * 2 - 40 * self.vpl) / self.vpl

        for e in self.edges:
            x1 = 40 + (sz + 40) * (e[0] % self.vpl) + sz / 2
            y1 = 40 + (sz + 40) * (e[0] / self.vpl) + sz / 2
            x2 = 40 + (sz + 40) * (e[1] % self.vpl) + sz / 2
            y2 = 40 + (sz + 40) * (e[1] / self.vpl) + sz / 2

            func(x1, y1, x2, y2)

    def DrawSquares(self, window_size, func):
        sz = (window_size[0] - 40 * 2 - 40 * self.vpl) / self.vpl

        for i in range(self.vertices_cnt):
            x = 40 + (sz + 40) * (i % self.vpl)
            y = 40 + (sz + 40) * (i / self.vpl)

            func(x, y, sz, sz, roundness=0.2)

    def Export(self, filename):
        f = open(filename, 'w')
        f.write(str(self.vertices_cnt) + '\n')
        f.write(str(len(self.edges)) + '\n')

        for i in self.edges:
            f.write(str(i[0]) + ':' + str(i[1]) + '\n')

        f.close()
