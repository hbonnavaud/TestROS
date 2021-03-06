from random import choice

from Agents.HedonistAgent import HedonistAgent

""" Agent qui n'aimait pas s'ennuyer : https://github.com/OlivierGeorgeon/TestROS/wiki/Agent-1 """
class BoredAgent(HedonistAgent):
    def __init__(self, _hedonist_table, patience=4):
        super().__init__(_hedonist_table)
        self.good_predictions_before_get_bored = 0
        self.patience = patience  # Combiens d'itérations avant que l'agent s'ennuie

    """ True if the agent is bored, false otherwise. """

    def isBored(self):
        if self.good_predictions_before_get_bored >= self.patience:
            return True
        return False

    """ Computing a tuple representing the agent's satisfaction after the last interaction """

    def satisfaction(self, new_outcome):
        if new_outcome is not None:
            self.memoriseOutcome(new_outcome)

        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        if anticipation_satisfaction:
            self.good_predictions_before_get_bored += 1
        else:
            self.good_predictions_before_get_bored = 0

        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self.action][new_outcome]

        return anticipation_satisfaction, hedonist_satisfaction, self.isBored()

    def chooseAction(self, outcome):
        if self.action is None:
            self.action = 0
            return self.action

        # If our agent get bored
        if self.isBored():
            # In this case, we should choose a random action from the range of available actions except the one
            # we choosed before.
            other_actions = self.available_actions.copy()
            other_actions.remove(self.action)
            self.action = choice(other_actions)

            # Now our agent change it's choice, he's not bored anymore.
            self.good_predictions_before_get_bored = 0
        # Otherwise, we just keep the same action.
        return self.action