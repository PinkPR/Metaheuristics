import math
import copy
import random

def f(n, backs):
	if n == 0:
		return backs

	result_sets = []

	if backs == None:
		for i in range(-1, 2):
			result_sets.append([i])
	else:
		for x in backs:
			for i in range(-1, 2):
				new_back = copy.deepcopy(x)
				new_back.append(i)
				result_sets.append(new_back)

	return f(n - 1, result_sets)

class BasicFunc:
	def __init__(self):
		self.param_range = [0, 1]
		#self.param_range = [0, math.pi]

	def compute(self, params):
		#s = 0.0
		for i in range(len(params)):
			#s += math.sin(params[i]) * pow(math.sin((i + 1) * pow(params[i], 2) / math.pi), 20)
			s += params[i]

		return s

	def get_random_params(self, n):
		params = []
		for i in range(n):
			params.append(self.param_range[0] + random.random() * (self.param_range[1] - self.param_range[0]))

		return params

	def accept_params(self, params):
		for x in params:
			if x > self.param_range[1] or x < self.param_range[0]:
				return False
		return True

	def get_neighbours(self, params, step):
		sets = f(len(params), None)
		neighbours = []

		for n in sets:
			new_params = copy.deepcopy(params)

			if n == ([0] * len(n)):
				continue

			for i in range(len(new_params)):
				new_params[i] = new_params[i] + (n[i] * step)
			if self.accept_params(new_params):
				neighbours.append(new_params)

		return neighbours

class Michalewicz(BasicFunc):
	def __init__(self):
		self.param_range = [0, math.pi]

	def compute(self, params):
		s = 0.0
		for i in range(len(params)):
			s += math.sin(params[i]) * pow(math.sin((i + 1) * pow(params[i], 2) / math.pi), 20)

		return s

class DeJongF1(BasicFunc):
	def __init__(self):
		self.param_range = [-5.12, 5.12]
		self.name = 'De Jong F1'

	def compute(self, params):
		s = 0.0
		for x in params:
			s += pow(x, 2)

		return s

class DeJongF2(BasicFunc):
	def __init__(self):
		self.param_range = [-2.048, 2.048]
		self.name = 'De Jong F2'

	def compute(self, params):
		x1 = params[0]
		x2 = params[1]

		return 100 * (pow(x2, 2) - x1) + (1 - x1)

class DeJongF3(BasicFunc):
	def __init__(self):
		self.param_range = [-5.12, 5.12]
		self.name = 'De Jong F3'

	def compute(self, params):
		s = 0.0

		for x in params:
			s += int(x)

		return s

class GoldsteinPrice(BasicFunc):
	def __init__(self):
		self.param_range = [-2, 2]
		self.name = "Goldstein And Price"

	def compute(self, params):
		x1 = params[0]
		x2 = params[1]

		return (1 + pow(x1 + x2 + 1, 2) * (19 - 14 * x1 + 3 * pow(x1, 2) - 14 * x2 + 6 * x1 * x2
				+ 3 * pow(x2, 2))) * (30 + pow(2 * x1 - 3 * x2, 2) * (18 - 32 * x1 + 12 * pow(x1, 2)
				+ 48 * x2 - 36 * x1 * x2 + 27 * pow(x2, 2)))

class Rosenbrock(BasicFunc):
	def __init__(self):
		self.param_range = [-2.048, 2.048]
		self.name = 'Rosenbrock'

	def compute(self, params):
		s = 0.0
		for i in range(len(params) - 1):
			s += 100 * pow(pow(params[i], 2) - params[i + 1], 2) + (params[i] - 1)

		return s

class Zakharov(BasicFunc):
	def __init__(self):
		self.param_range = [-2.048, 2.048]
		self.name = 'Zakharov'

	def compute(self, params):
		s1 = 0.0
		s2 = 0.0

		for x in params:
			s1 += pow(x, 2)

		for i in range(len(params)):
			s2 += 0.5 * i * params[i]

		return s1 + pow(s2, 2) + pow(s2, 4)

class Schwefel1(BasicFunc):
	def __init__(self):
		self.param_range = [-500, 500]
		self.name = 'Schwefel 1'

	def compute(self, params):
		s = 0.0

		for x in params:
			s += -x * math.sin(math.sqrt(abs(x)))

		return s
