from random import choice, random

from Agents.Agent import Agent


""" Agent qui n'aimait pas s'ennuyer : https://github.com/OlivierGeorgeon/TestROS/wiki/Agent-1 """
class RandomExplorerAgent(Agent):
    def __init__(self, _hedonist_table):
        super().__init__(_hedonist_table)

        # List of action that haven't been explored yet
        self.actions_to_explore = [x for x in range(0, len(self.hedonist_table))]

        # Probabilité que l'agent explore à chaque itération
        self.exploration_probability = 0.1

    """ Computing a tuple representing the agent's satisfaction after the last interaction """
    def satisfaction(self, new_outcome):
        if new_outcome is not None:
            # Maintenant qu'on fait le bilan de l'action passé et que nous en avons un retour,
            # Nous pouvons noter l'action passée comme étant explorée.
            if self.action in self.actions_to_explore:
                self.actions_to_explore.remove(self.action)
            self.memoriseOutcome(new_outcome)

        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self.action][new_outcome]

        return anticipation_satisfaction, hedonist_satisfaction

    """ Computing the next action to enact """
    def chooseAction(self, outcome):
        if self.actions_to_explore and self.exploration_probability <= random():
            self.action = choice(self.actions_to_explore)
        else:
            self.action = self.getBestActionFromMemory()
            if self.action is None:
                self.action = 0
        return self.action