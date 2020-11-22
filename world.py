#!/usr/bin/env python3

# Olivier Georgeon, 2020.
# This code is used to teach Develpmental AI.
from Agents.ContextAgent import ContextAgent
from Agents.HedonistAgent import HedonistAgent
from Agents.BoredAgent import BoredAgent
from Agents.BoredHedonistAgent import BoredHedonistAgent
from Agents.PaternDetectionAgent import PaternDetectionAgent
from Agents.LowInterestAgent import LowInterestAgent
from Environments.Environment1 import Environment1
from Environments.Environment2 import Environment2
from Environments.Environment3 import Environment3
from Environments.Environment4 import Environment4


# Choose an agent
agent_id = 6  # we will use bored agent otherwise
context_deep = 2  # if agent_id == 7
available_actions = context_deep
hedonist_table = [[-1, 1] for _ in range(available_actions)]
# 1 : HedonistAgent                 # Agent 0 du sujet : L'agent rudimentaire
# 2 : BoredAgent                    # Agent 1 du sujet : L'agent qui n'aimait pas s'ennuyer
# 3 : BoredHedonistAgent with greedy=False  # Agent 2 du sujet : L'agent qui préférait les interactions positives
# 4 : BoredHedonistAgent with greedy=True   <# Agent 2 du sujet : L'agent qui préférait les interactions positives>
                                            # Mais en version greedy (Cf. compte rendu ou readme)
# 5 : ContextAgent                  # Agent 3 du sujet : L'agent qui agissait selon son contexte
# 6 : RandomExplorerHedonistAgent
# 7 : LongMemoryAgent

# Choose an environment
environment_id = 3      # id of the environment to use
# 1 : Environment1
# 2 : Environment2
# 3 : Environment3
# 4 : Environment4

def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = None
    for i in range(15):
        action = agent.chooseAction(outcome)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))

if environment_id == 1:
    environment = Environment1()
elif environment_id == 2:
    environment = Environment2()
elif environment_id == 3:
    environment = Environment3()
elif environment_id == 4:
    environment = Environment4(nb_actions=context_deep)
else:
    environment = Environment3()

if agent_id == 1:
    agent = HedonistAgent(hedonist_table)
elif agent_id == 2:
    agent = BoredAgent(hedonist_table)
elif agent_id == 3:
    agent = BoredHedonistAgent(hedonist_table, greedy=False)
elif agent_id == 4:
    agent = BoredHedonistAgent(hedonist_table, greedy=True)
elif agent_id == 5:
    agent = ContextAgent(hedonist_table)
elif agent_id == 6:
    agent = PaternDetectionAgent(hedonist_table)
elif agent_id == 7:
    agent = LowInterestAgent(hedonist_table, actions_range=available_actions)

world(agent, environment)
