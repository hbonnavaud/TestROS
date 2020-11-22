from random import choice

from Agents.ContextAgent import ContextAgent

class PaternDetectionError(Exception):
    pass

class PaternDetectionAgent(ContextAgent):
    def __init__(self, _hedonist_table):
        super().__init__(_hedonist_table)
        self.patterns_detected = {}
        # self.patterns_detected = {
        #   patternA: X,
        #   patternB: y,
        #   ...
        # }
        # Avec PatternA et patternB des pattern, et X et Y le nombre de fois qu'on les a détectés jusque là.
        # We consider that a pattern is a list of action, and an action is an int.

        self.actions_memory = []
        self.actions_memory_length = 8  # permet de détecter des patterns de taille 1 à actions_memory_length/2
        self.bored = False

    def setBored(self, bored):
        self.bored = bored

    def isBored(self):
        return self.bored

    def memoriseAction(self, action):
        self.actions_memory.append(action)
        while len(self.actions_memory) > self.actions_memory_length:
            self.actions_memory.pop(0)

    """ Use actions_memory to update self.patternsDetected. """
    def updateDetectedPatterns(self):
        patterns_to_remove = []  # keep a memory because we can't remove patterns while iterate on them.
        # For each pattern in our patterns memory
        for pattern in self.patterns_detected:
            # We search the index of the action that arrived just after the last detection of this pattern.
            regenerated = False
            for regenerated_pattern_length in range(1, len(pattern) + 1):
                # If the 'regenerated_pattern_length' first patterns actions has been regenerated
                # to know if it's true, iterate into the end of our memory, we should find the
                # pattern folowed by it's "regenerated_pattern_length" first actions
                memory_end = list(pattern)
                memory_end += memory_end[:regenerated_pattern_length]
                if memory_end == self.actions_memory[-len(memory_end):]:
                    regenerated = True
            if not regenerated:
                patterns_to_remove.append(pattern)
        for pattern in patterns_to_remove:
            self.patterns_detected.pop(pattern, None)

        # Detection of new patterns from the new action :
        for n in range(len(self.actions_memory) // 2):
            pattern_length = n + 1
            new_pattern = []
            for i in range(pattern_length):
                new_pattern.append(self.actions_memory[-(i + 1)])
            new_pattern.reverse()

            # On regarde si il est reproduit avant
            same = True
            for i in range(pattern_length):
                if self.actions_memory[-(pattern_length + i + 1)] != new_pattern[-(i + 1)]:
                    same = False
            if same:
                if tuple(new_pattern) in patterns_to_remove:
                    raise PaternDetectionError(
                        "Pattern removed before a reproduction has been found, pattern = " + str(new_pattern))
                pattern = tuple(new_pattern)
                if pattern in self.patterns_detected:
                    self.patterns_detected[pattern] += 1
                    if self.patterns_detected[pattern] >= 4:
                        self.patterns_detected = {}
                        self.actions_memory = []
                        self.setBored(True)
                        return
                else:
                    self.patterns_detected[pattern] = 2

    def chooseAction(self, outcome):

        # print(str(self.context_memory))
        print(str(self.patterns_detected))

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

                """ RESET BORED BOOLEAN """
                self.setBored(False)

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

        """ BEFORE WE RETURN AN ACTION """
        """ We should store it inside our memory. """
        self.memoriseAction(self.action)
        self.updateDetectedPatterns()
        return self.action






