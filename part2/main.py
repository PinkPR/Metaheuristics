import tabusearch
from functions import *
from matplotlib import pyplot
import numpy

def get_avg(func, test_n, list_size, step):
	avg = 0.0

	for i in range(test_n):
		ts = tabusearch.TabuSearch(50000, func, 2, list_size, step)
		best_params = ts.run()
		avg += func.compute(best_params)

	return avg / float(test_n)

def make_plot(func, test_n, size, step_list):
	res_list = []

	for i in step_list:
		print 'Testing : ' + str(i)
		res_list.append(get_avg(func, test_n, size, i))

	pyplot.plot(step_list, res_list)
	pyplot.savefig(func.name + '.png')

def test_funcs(funcs, test_n):
	for x in funcs:
		params_avg = [0, 0]
		avg = 0;
		for i in range(test_n):
			ts = tabusearch.TabuSearch(50000, x, 2, 10, 0.1)
			best_params = ts.run()
			params_avg[0] = params_avg[0] + best_params[0]
			params_avg[1] = params_avg[1] + best_params[1]
			avg += x.compute(best_params)
			#print x.name
			#print 'Test number : ' + str(i + 1)
			#print 'best params = ' + str(best_params)
			#print 'minimum = ' + str(x.compute(best_params))
			#print '-----------------------------------------'

		avg /= float(test_n)
		params_avg[0] = params_avg[0] / test_n
		params_avg[1] = params_avg[1] + test_n

		print
		print '----------------------------------------'
		print x.name
		print 'Average Params : ' + str(best_params)
		print 'Average Result : ' + str(avg)
		print '----------------------------------------'
		print

funcs = [DeJongF1(), DeJongF2(), DeJongF3(), GoldsteinPrice(), Rosenbrock(), Zakharov(), Schwefel1()]

#test_funcs(funcs, 10)
make_plot(Schwefel1(), 10, 50, numpy.linspace(0.01, 1, 5))
