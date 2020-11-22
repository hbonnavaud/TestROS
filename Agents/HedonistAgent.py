from Agents.Agent import Agent


class HedonistAgent(Agent):
    def __init__(self, _hedonist_table):
        super().__init__()
        self.hedonist_table = _hedonist_table
        self.available_actions = [x for x in range(len(self.hedonist_table))]

        self.best_known_action = None
        self.best_known_gain = None

    def memoriseOutcome(self, outcome):
        super().memoriseOutcome(outcome)
        if self.best_known_gain is None or outcome > self.best_known_gain:
            self.best_known_action = self.action
            self.best_known_gain = self.hedonist_table[self.action][outcome]

    def chooseAction(self, outcome):
        if outcome is not None:
            self.memoriseOutcome(outcome)

        """ Computing the next action to enact """
        self.action = self.best_known_action
        if self.action is None:
            self.action = 0

        return self.action

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self.action][new_outcome]
        return anticipation_satisfaction, hedonist_satisfaction