from collections import deque
import functions
import copy

class TabuFifo:
	def __init__(self, max_size):
		self.fifo = deque([])
		self.max_size = max_size

	def push(self, elt):
		if len(self.fifo) < self.max_size:
			self.fifo.append(elt)

	def pop(self):
		if len(self.fifo) == 0:
			return None
		return self.fifo.popleft()

class TabuSearch:
	def __init__(self, max_iter, func, params_n, max_fifo_size, step):
		self.max_iter = max_iter
		self.func = func
		self.params_n = params_n
		self.fifo = TabuFifo(max_fifo_size)
		self.max_fifo_size = max_fifo_size
		self.step = step

	def run(self):
		params = self.func.get_random_params(self.params_n)
		best_params = copy.deepcopy(params)
		iter_count = 0

		while iter_count < self.max_iter:
			neighbours = self.func.get_neighbours(params, self.step)
			best_neighbour = None

			for n in neighbours:
				if not best_neighbour:
					best_neighbour = n
					continue

				if not (n in self.fifo.fifo):
					if self.func.compute(best_neighbour) > self.func.compute(n):
						best_neighbour = copy.deepcopy(n)

			params = copy.deepcopy(best_neighbour)

			if self.func.compute(best_neighbour) < self.func.compute(best_params):
				best_params = best_neighbour

			self.fifo.push(best_neighbour)

			if len(self.fifo.fifo) == self.max_fifo_size:
				pop_elt = self.fifo.pop()

			iter_count += 1

		return best_params
