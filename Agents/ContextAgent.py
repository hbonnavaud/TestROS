from random import choice

from Agents.BoredHedonistAgent import BoredHedonistAgent


class ContextAgent(BoredHedonistAgent):
    def __init__(self, _hedonist_table):
        super().__init__(_hedonist_table, greedy=True)

        # This agent will have the exactly same behaviour than its parent,
        # except that it's memory will not work the same way.
        self.context_memory = {}
        self.context = None

        # self.context_memory = {
        #   A: [(0, 1), (1, 0)],
        #   B: [(1, 0), (0, 1)]
        #   ...
        # }
        # With, A, B, somme t-1 interactions (contexts), and 0:1, 1:0 somme interactions at time=t.
        # A context is a tuple (action, outcome) that is the interaction at time t-1.

    """ Computing a tuple representing the agent's satisfaction after the last interaction """
    def memoriseOutcome(self, outcome):
        # Memorise the passed interaction
        if self.context is not None:
            if self.context in self.context_memory:
                if (self.action, outcome) not in self.context_memory[self.context]:
                    self.context_memory[self.context].append((self.action, outcome))
            else:
                self.context_memory[self.context] = [(self.action, outcome)]
        # register the passed interaction as the new context
        self.context = (self.action, outcome)

    """
        Return a tuple (Action, Outcome) where outcome is the best outcome you can get according to hedonist table
        from the given context 'currentContext', ans Action is the action to chose in order to get the returned outcome.
    """
    def getBestActionFromContext(self, currentContext):
        for context, memory in self.context_memory.items():
            if context == currentContext:
                # Find the best action in this memory
                # Note that from this point, we will not continue the for loop and return something in every case.
                best_outcome = None
                best_action = None
                for action, outcome in memory:
                    if best_outcome is None or outcome > best_outcome:
                        best_outcome = outcome
                        best_action = action
                return None if best_action is None else (best_action, best_outcome)
        # If nothing have been returned, then we don't know anything about the current context
        return None

    def chooseAction(self, outcome):
        print(str(self.context_memory))

        # On garde en mémoire notre dernière action
        old_action = self.action

        # On commence par choisir une action
        if self.context is None:
            self.action = 0
        else:
            bestActionContext = self.getBestActionFromContext(self.context)
            if bestActionContext is None:
                self.action = 0
            else:
                self.action = bestActionContext[0]

            if self.isBored():
                # If our agent is bored, we are going to randomly choose an action that is taken
                other_actions = self.available_actions.copy()
                other_actions.remove(self.action)
                self.action = choice(other_actions)

            # If our agent is greedy, it will try to explore it's environment if it's not satisfied by the last outcome.
            # Then, if our best_known gain so far is set and negative, and if we still have actions left to explore,
            # then we are going to explore.
            elif self.greedy and bestActionContext is not None \
                    and self.hedonist_table[bestActionContext[0]][bestActionContext[1]] < 0 \
                    and len(self.context_memory[self.context]) < len(self.available_actions):
                actions = [interaction[0] for interaction in self.context_memory[self.context]]
                unexplored_actions = [x for x in self.available_actions if x not in actions]
                self.action = choice(unexplored_actions)
        # End of "if self.context is not None"

        # If we chose a new action, then we can restart the boring counter.
        if self.action != old_action:
            self.good_predictions_before_get_bored = 0
        return self.action




