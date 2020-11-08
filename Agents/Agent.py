class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.outcomes_memory = {}
        self.hedonist_table = _hedonist_table
        self.action = None
        self.anticipated_outcome = None

    def getBestActionFromMemory(self):
        if not self.outcomes_memory:
            return None
        max = None
        best_action = None
        for action, outcome in self.outcomes_memory.items():
            gain = self.hedonist_table[action][outcome]
            if max is None or max < gain:
                max = gain
                best_action = action
        return best_action

    def memoriseOutcome(self, outcome):
        self.outcomes_memory[self.action] = outcome

    def chooseAction(self, outcome):
        if outcome is not None:
            self.memoriseOutcome(outcome)

        """ Computing the next action to enact """
        self.action = self.getBestActionFromMemory()
        if self.action is None:
            self.action = 0

        return self.action

    def anticipation(self):
        """ computing the anticipated outcome from the latest action """
        if self.action in self.outcomes_memory:
            self.anticipated_outcome = self.outcomes_memory[self.action]
        else:
            self.anticipated_outcome = 0
        return self.anticipated_outcome

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self.action][new_outcome]
        return anticipation_satisfaction, hedonist_satisfaction