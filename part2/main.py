import tabusearch
from functions import *

def test_funcs(funcs):
	for x in funcs:
		ts = tabusearch.TabuSearch(50000, x, 2, 10, 1)
		best_params = ts.run()
		print x.name
		print 'best params = ' + str(best_params)
		print 'minimum = ' + str(x.compute(best_params))
		print '-----------------------------------------'

funcs = [DeJongF1(), DeJongF2(), DeJongF3(), GoldsteinPrice(), Rosenbrock(), Zakharov(), Schwefel1()]

test_funcs(funcs)
