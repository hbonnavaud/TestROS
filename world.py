#!/usr/bin/env python3

# Olivier Georgeon, 2020.
# This code is used to teach Develpmental AI.

from Agents.Agent import Agent
from Agents.BoredAgent import BoredAgent
from Agents.RandomExplorerAgent import RandomExplorerAgent
from Environments.Environment1 import Environment1
from Environments.Environment2 import Environment2

# Define the hedonist values of interactions (action, outcome)
from Environments.Environment3 import Environment3

hedonist_table = [[-1, 1], [-1, 1]]

# Choose an agent
use_basic_agent = 3  # we will use bored agent otherwise
# 1 : Agent
# 2 : BoredAgent
# 3 : RandomExplorerAgent

# Choose an environment
environment_id = 3      # id of the environment to use
# 1 : Environment1
# 2 : Environment2
# 3 : Environment3 with hedonist_table = [[-1, 1], [-0.5, 0.5], [0, 0], [-0.5, 0.5], [-1, 1], [-1.5, 1.5]]

def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    print("hedonist table = " + str(agent.hedonist_table))
    outcome = None
    for i in range(15):
        action = agent.chooseAction(outcome)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))

environment = None
if environment_id == 1:
    environment = Environment1()
elif environment_id == 2:
    environment = Environment2()
else:
    environment = Environment3()
    hedonist_table = [[-1, 1], [-0.5, 0.5], [0, 0], [-0.5, 0.5], [-1, 1], [-1.5, 1.5]]

agent = None
if use_basic_agent == 1:
    agent = Agent(hedonist_table)
elif use_basic_agent == 2:
    agent = BoredAgent(hedonist_table)
else:
    agent = RandomExplorerAgent(hedonist_table)


world(agent, environment)
