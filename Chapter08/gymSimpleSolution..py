'''
Simple solution for frozen lake using gym library
'''
import gym

env = gym.make('FrozenLake-v0') ## render our env
env.reset()
env.render()

# Print below values to learn more about the space
# observation_size = env.observation_space.n
# print(observation_size)
# action_size = env.action_space.n
# print(action_size)
MAX_MOVES =20
MAX_ITERATIONS = 200

for j in range(MAX_ITERATIONS):
    for i in range(MAX_MOVES):
        action = env.action_space.sample()
        observation, reward, done, degub_info = env.step(action)
        env.render()
        if done:
            break
    if observation == 15:
        break
    env.reset()
print(j)
