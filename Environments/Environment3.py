class Environment3:

    def __init__(self):
        self.previous_action = None

    def outcome(self, action):
        if action == self.previous_action:
            outcome = 0
        else:
            outcome = 1
        self.previous_action = action
        return outcome