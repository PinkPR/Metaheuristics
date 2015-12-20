import graph
import StatisticalCooling

g = graph.Graph('test_file')
sc = StatisticalCooling.Algo(1.0, 1 - 1e-5, g, 200)
g = sc.Run()

while True:
    g2 = sc.Run()
    if not g2:
        break
    g = g2

g.Export('result')
