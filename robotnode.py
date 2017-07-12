class ActionNode:
	def __init__(self, game, value, visited):
		"""
		Initializes the ActionNode class, which stores the coordinator action taken.
		:param game: the game to be solved.
		:param value: the value that was achieved after this coordinator action was taken.
		:param visited: the number of times this coordinator action was taken (should be initialized to 1).
		"""
		self.type = "action"
		self.game = game
		self.human_actions = self.game.getAllHumanActions()
		self.children = self.make_children()
		self.value = value
		self.visited = visited

	def make_children(self):
		"""
		Makes the children (human actions) of the ActionNode.
		"""
		children = []
		for action in self.human_actions:
			children.append("empty")

		return children

	def augmented_value(self, c):
		"""
		Returns the augmented value (value + exploration) of taking this robot action.
		"""
		#test to make sure this division isnt just 0
		return self.value + c/self.visited

	def update_value(self, reward):
		"""
		Averages the new reward with the current value to update it.
		:param reward: the reward just received
		"""
		val = self.value
		val = val + ((reward - val)/self.visited)
		self.value = val

	def update_visited(self):
		"""
		Increments the number of times this robot action has been taken.
		"""
		count = self.visited
		count = count + 1
		self.visited = count