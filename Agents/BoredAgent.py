from random import choice

from Agents.Agent import Agent


""" Agent qui n'aimait pas s'ennuyer : https://github.com/OlivierGeorgeon/TestROS/wiki/Agent-1 """
class BoredAgent(Agent):
    def __init__(self, _hedonist_table):
        super().__init__(_hedonist_table)
        self.good_predictions_before_get_bored = 0
        self.patience = 4  # Combiens d'itérations avant que l'agent s'ennuie

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

        """ Computing the next action to enact """
        old_action = self.action

        self.action = self.getBestActionFromMemory()
        if self.action is None:
            self.action = 0

        if self.isBored():
            # Dans ce cas on choisit une action au hasard parmis les actions différentes de celle qu'on aurait choisis.
            # 1 - On construit la liste des actions possibles
            available_actions = [x for x in range(0, len(self.hedonist_table))]  # [0, ..., n], n = len(hedonist) - 1
            # 2 - On y retire l'action que nous avions prévu de choisir
            available_actions.remove(self.action)
            self.action = choice(available_actions)

            # Maintenant que l'agent a changé de décision, il n'est plus ennuyé.
            self.good_predictions_before_get_bored = 0

        # Si on a changé d'action, on éinitialise le compteur avant ennuis.
        if self.action != old_action:
            self.good_predictions_before_get_bored = 0
        return self.action