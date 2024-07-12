from collections import defaultdict

from Constants.JobKeyMap import JOB_KEY_MAP
from TemplateClasses import Objective


class Job:
    def __init__(self, name: str):
        self.name = name
        self.key_type = JOB_KEY_MAP[self.name]
        self.objectives = defaultdict(list)

    def add_objective(self, objective: Objective):
        self.objectives[objective.difficulty].append(objective)

    def display(self):
        print(f"Job Name: {self.name}")
        print("Objectives:")
        for difficulty, objs in self.objectives.items():
            print(f"Difficulty: {difficulty}")
            for obj in objs:
                obj.display()
                print()
