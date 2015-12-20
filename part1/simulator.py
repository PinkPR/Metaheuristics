import StatisticalCooling
import graph
import numpy
import sys
import copy

def runTest(gg, temp, factor, optimum, max_iter):
	print 'Running : T = ' + str(temp) + ' factor = ' + str(factor)
	g = copy.deepcopy(gg)
	sc = StatisticalCooling.Algo(temp, factor, g, optimum, max_iter)

	while True:
		g2 = sc.Run()

		if not g2:
			return (False, sc.iter_cnt)

		g = g2

	return (True, sc.iter_cnt)

def runAllTest(g, temp_list, factor_list, optimum, max_iter, test_cnt):
	results = []
	test_nb = len(temp_list) * len(factor_list) * test_cnt

	for t in temp_list:
		print "Test count left : " + str(test_nb * test_cnt)
		factor_results = []

		for f in factor_list:
			result_set = []

			for i in range(test_cnt):
				result_set[i] = factor_results.append(runTest(g, t, f, optimum, max_iter))

			factor_results.append(result_set)

		results.append(factor_results)
		test_nb -= 1

	return factor_results

temp_min = 100
temp_max = 1000
temp_step = 50

factor_min = 0.8
factor_max = 0.99
factor_step = 0.05

temp_list = list(numpy.linspace(temp_min, temp_max, int((temp_max - temp_min) / float(temp_step)) + 1))
factor_list = list(numpy.linspace(factor_min, factor_max, int((factor_max - factor_min) / float(factor_step)) + 1))

print 'Temp list = ' + str(temp_list)
print 'Fact list = ' + str(factor_list)

g = graph.Graph(sys.argv[1])

res = runAllTest(g, temp_list, factor_list, 200, 10000, 20)
