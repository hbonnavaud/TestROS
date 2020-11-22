from random import choice

from Agents.HedonistAgent import HedonistAgent

""" Agent qui n'aimait pas s'ennuyer : https://github.com/OlivierGeorgeon/TestROS/wiki/Agent-1 """
class BoredHedonistAgent(HedonistAgent):
    def __init__(self, _hedonist_table, patience=4, greedy=True):
        super().__init__(_hedonist_table)
        self.good_predictions_before_get_bored = 0
        self.patience = patience  # Combiens d'itérations avant que l'agent s'ennuie
        self.greedy = greedy

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

        # On garde en mémoire notre dernière action
        old_action = self.action

        # On commence par choisir une action
        self.action = self.best_known_action
        if self.action is None:
            self.action = 0

        if self.isBored():
            # If our agent is bored, we are going to randomly choose an action that is taken
            other_actions = self.available_actions.copy()
            other_actions.remove(self.action)
            self.action = choice(other_actions)

        # If our agent is greedy, it will try to explore it's environment if it's not satisfied by the last outcome.
        # Then, if our best_known gain so far is set and negative, and if we still have actions left to explore,
        # then we are going to explore.
        elif self.greedy and self.best_known_gain is not None and self.best_known_gain < 0 \
                and len(self.memory) < len(self.available_actions):
            actions = [action for action in self.memory.keys()]
            unexplored_actions = [x for x in self.available_actions if x not in actions]
            self.action = choice(unexplored_actions)

        # If we chose a new action, then we can restart the boring counter.
        if self.action != old_action:
            self.good_predictions_before_get_bored = 0
        return self.action