from random import randint

from TemplateClasses.Job import Job
from TemplateClasses.QuestDifficulty import QuestDifficulty


class Quest:
    def __init__(self, quest_difficulty: QuestDifficulty, job: Job):
        self.quest_difficulty = quest_difficulty
        self.job = job
        self.num_objectives = quest_difficulty.difficulties_count
        self.objectives_selected = self.get_selected_objectives()

    def get_selected_objectives(self):
        objectives = []
        for difficulty in self.quest_difficulty.difficulties.keys():
            cur_objectives = self.job.objectives[difficulty]
            for i in range(self.quest_difficulty.difficulties[difficulty]):
                objectives.append(cur_objectives[randint(0, len(cur_objectives) - 1)])
        return objectives

    def display(self):
        print(f"Quest Difficulty: {self.quest_difficulty.difficulty_level}")
        print(f"Job: {self.job.name}")
        print("Selected objectives:")
        print(self.objectives_selected)
