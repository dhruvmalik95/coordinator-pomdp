class RobotNode:
	def __init__(self, game, value, visited):
		self.type = "robot"
		self.game = game
		self.observations = self.game.getAllObservations()
		self.children = self.make_children()
		self.value = value
		self.visited = visited

	def make_children(self):
		children = []
		for action in self.observations:
			children.append("empty")

		return children

	def augmented_value(self, c):
		#test to make sure this division isnt just 0
		return self.value + c/self.visited

	def update_value(self, reward):
		val = self.value
		val = val + ((reward - val)/self.visited)
		self.value = val

	def update_visited(self):
		count = self.visited
		count = count + 1
		self.visited = count