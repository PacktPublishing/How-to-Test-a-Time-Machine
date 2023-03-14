from yaml import load, safe_load, Loader
import os
from git import Repo
with open('instructions.yml') as stream:
    data = safe_load(stream)
    for step in data['Steps']:
        print(step['name'])
        print(step['log'])
        os.system(step['instruction'])
