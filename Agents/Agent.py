class Agent:
    def __init__(self):
        """ Creating our agent """
        self.memory = {}
        self.action = None
        self.anticipated_outcome = None

    def memoriseOutcome(self, outcome):
        self.memory[self.action] = outcome

    def chooseAction(self, outcome):
        if outcome is not None:
            self.memoriseOutcome(outcome)

        """ Computing the next action to enact """
        self.action = 0

        return self.action

    def anticipation(self):
        """ computing the anticipated outcome from the latest action """
        if self.action in self.memory:
            self.anticipated_outcome = self.memory[self.action]
        else:
            self.anticipated_outcome = 0
        return self.anticipated_outcome

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        return anticipation_satisfaction