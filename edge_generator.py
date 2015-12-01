import random
import sys

print sys.argv[1]
print (int(sys.argv[1]) * int(sys.argv[2]))

for i in range(int(sys.argv[1]) - 1):
    edges = []

    for j in range(int(sys.argv[2])):
        edges.append(i + 1 + int((int(sys.argv[1]) - i - 1) * random.random()))

        for k in range(j):
            if edges[j] == edges[k]:
                j = j - 1
                break

    for j in range(int(sys.argv[2])):
        assert(i <> edges[j])
        assert(edges[j] < int(sys.argv[1]))
        print str(i) + ':' + str(edges[j])
