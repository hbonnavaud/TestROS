class Environment4:
    def __init__(self, nb_actions=3):
        self.nb_actions = nb_actions
        self.actions_undone_since = [0 for _ in range(nb_actions)]

    def outcome(self, action):
        if self.actions_undone_since[action] == max(self.actions_undone_since):
            outcome = 1
        else:
            outcome = 0
        self.actions_undone_since = [x+1 for x in self.actions_undone_since]
        self.actions_undone_since[action] = 0
        return outcome