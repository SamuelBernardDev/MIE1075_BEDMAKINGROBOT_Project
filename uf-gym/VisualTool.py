import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../panda-gym')) # the directory of 'panda-gym'
import gymnasium as gym
from sb3_contrib.tqc import TQC
import panda_gym
import uf_gym
from collections import OrderedDict
from stable_baselines3 import HerReplayBuffer
import time

# Initialize the environment with rendering enabled
env = gym.make('XArm7PickAndPlace-v3', render_mode="human")

# Reset the environment to obtain the initial observation
observation, info = env.reset()

# Define the delay duration (in seconds) between steps
delay_duration = 0.05  # Adjust this value as needed

# Run a few steps to visualize the environment
for _ in range(1000):
    action = env.action_space.sample()  # Replace with your action selection logic
    observation, reward, done, truncated, info = env.step(action)
    if done or truncated:
        observation, info = env.reset()
    time.sleep(delay_duration)  # Introduce a delay to slow down the simulation

# Close the environment
env.close()
