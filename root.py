import numpy as np
import math
class Root:
	def __init__(self, game, belief, visited):
		self.type = "root"
		self.game = game
		self.actions = self.game.getAllActions()
		self.children = self.make_children()
		self.belief = belief
		self.visited = visited

	def make_children(self):
		children = []
		for action in self.actions:
			children.append("empty")

		return children

	def optimal_action(self, c):
		for i in range(0, len(self.children)):
			if self.children[i] == "empty":
				return self.actions[i]

		values = []
		for i in range(0, len(self.children)):
			values.append(self.children[i].augmented_value(c))

		return self.actions[values.index(max(values))]

	def sample_belief(self):
		random_index = np.random.choice(range(0, len(self.belief)))
		return self.belief[random_index]

	def update_visited(self, theta):
		count = self.visited
		count = count + 1
		self.visited = count

	def update_value(self, reward, theta):
		return