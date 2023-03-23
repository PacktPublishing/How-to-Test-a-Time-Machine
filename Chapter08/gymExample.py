'''
 Example of gym library
'''
# from math import gamma
import numpy as np
import gym

env = gym.make('FrozenLake-v0') ## render our env
env.reset()
env.render()

observation_size = env.observation_space.n
action_size = env.action_space.n
bug_table = np.zeros((observation_size, action_size))
print(bug_table)

MAX_ITERATIONS = 3000
MAX_MOVES = 400

# Change the following values to improve the algorithm
EXPLORATION_PROBABILITY = 0.5
EXPLORATION_DECREASING_DECAY = 0.001
MINIMUM_EXPLORATION_PROBABILITY = 0.01
DISCOUNTED_FACTOR = 0.1 # gamma
LEARNING_RATE = 0.99

total_rewards = []

for j in range(MAX_ITERATIONS):
    current_state = env.reset()
    DONE = False
    CURRENT_TOTAL_REWARD = 0
    for i in range(MAX_MOVES):
        # We iterate through the number of redirections allowed from this step
        # we can set this as a constant or as part of the table
        # Next step is to decide if we want to exploit or explore the system
        if np.random.uniform(0,1) > EXPLORATION_PROBABILITY:
            # Exploit the system - take the best action
            action = np.argmax(bug_table[current_state, :])
        else:
            # Explore the system - take a random action
            action = env.action_space.sample()
        # update the system
        observation, reward, done, degub_info = env.step(action)
        # calculate the estimation of next step – this is done
        # from the formula of the q-algorithm
        discounted_estimated_next_step = LEARNING_RATE * (reward +\
             DISCOUNTED_FACTOR*np.max(bug_table[observation] - bug_table[current_state, action]))
        # update the bug table with the new values (based on the q-algorithm
        # formula as well
        bug_table[current_state, action] = bug_table[current_state, action ] +\
             discounted_estimated_next_step
         #(1-LEARNING_RATE) * bug_table[current_state, action] + discounted_estimated_next_step
        # update the total reward
        CURRENT_TOTAL_REWARD = CURRENT_TOTAL_REWARD + reward
        # go to next step
        current_state = observation
	    # stop if done
        if DONE:
            break
    if not DONE:
        # add the new reward
        total_rewards.append(CURRENT_TOTAL_REWARD)
        # We should now fix the probability of exploration, based on the
        # algorithm as well, but we could have always the same one
    EXPLORATION_PROBABILITY = np.max([MINIMUM_EXPLORATION_PROBABILITY,\
         np.exp(-EXPLORATION_DECREASING_DECAY*2.0)])
    # print(bug_table)
    # Finally we render the environment that we got
    env.render()
print(bug_table)

sucess_rate = 0
for i in range(MAX_ITERATIONS):
    current_state = env.reset()
    DONE = False
    for j in range(MAX_MOVES):
        if np.random.uniform(0,1) > EXPLORATION_PROBABILITY:
            # Exploit the system - take the best action
            action = np.argmax(bug_table[current_state, :])
        current_state, reward, done, degub_info = env.step(action)
        sucess_rate = sucess_rate + reward

print(sucess_rate)
env.render()
