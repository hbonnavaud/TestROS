

""" Use actions_memory to update self.patternsDetected. """
from Agents.PaternDetectionAgent import PaternDetectionError

def updateDetectedPatterns():
    global patterns_detected
    global actions_memory
    global ennuis
    # Pour chaque pattern dans notre mémoire de pattern:
    patterns_to_remove = [] # keep a memory because we can't remove patterns while iterate on them.
    for pattern in patterns_detected:
        # We search the index of the action that arrived just after the last detection of this pattern.
        regenerated = False
        for regenerated_pattern_length in range(1, len(pattern) + 1):
            # If the 'regenerated_pattern_length' first patterns actions has been regenerated
            # to know if it's true, iterate into the end of our memory, we should find the
            # pattern folowed by it's "regenerated_pattern_length" first actions
            memory_end = list(pattern)
            memory_end += memory_end[:regenerated_pattern_length]
            if memory_end == actions_memory[-len(memory_end):]:
                regenerated = True
        if not regenerated:
            patterns_to_remove.append(pattern)
    for pattern in patterns_to_remove:
        patterns_detected.pop(pattern, None)

    # Detection of new patterns from the new action :
    for n in range(len(actions_memory) // 2):
        pattern_length = n + 1
        new_pattern = []
        for i in range(pattern_length):
            new_pattern.append(actions_memory[-(i+1)])
        new_pattern.reverse()

        # On regarde si il est reproduit avant
        same = True
        for i in range(pattern_length):
            if actions_memory[-(pattern_length + i + 1)] != new_pattern[-(i + 1)]:
                same = False
        if same:
            if tuple(new_pattern) in patterns_to_remove:
                raise PaternDetectionError("Pattern removed before a reproduction has been found, pattern = " + str(new_pattern))
            pattern = tuple(new_pattern)
            if pattern in patterns_detected:
                patterns_detected[pattern] += 1
                if patterns_detected[pattern] >= 4:
                    patterns_detected = {}
                    actions_memory = []
                    print("Ennuis pour : " + str(new_pattern))
                    ennuis = True
                    return
            else:
                patterns_detected[pattern] = 2

def append_action(action):
    global actions_memory
    global max_memory_length
    actions_memory.append(action)
    while len(actions_memory) > max_memory_length:
        actions_memory.pop(0)

sequences = []
sequences.append([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,])
sequences.append([0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0])
sequences.append([0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2])
sequences.append([0, 1, 0, 2, 3, 0, 1, 0, 2, 3, 0, 1, 0, 2, 3, 0, 1, 0, 2, 3])

patterns_detected = {}
actions_memory = []
max_memory_length = 8
ennuis = False

index = 0
for sequence in sequences:
    print("")
    print("===================================================================================")
    print("sequence n°" + str(index) + " = " + str(sequence))
    ennuis = False
    for action in sequence:
        # print("=======================================================================================")
        append_action(action)
        # print("actions_memory = " + str(actions_memory))
        updateDetectedPatterns()
        # print("patterns_detected = " + str(patterns_detected))
        # print("=======================================================================================")
    if not ennuis :
        print("Pas d'ennuis pour cette séquence")
    index += 1
