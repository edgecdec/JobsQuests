import os

from TemplateClasses.Job import Job
from TemplateClasses.Quest import Quest


class JobYAMLTemplate:
    def __init__(self, job: Job, quests: list[Quest]):
        self.job = job
        self.quests = quests
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"  Quests:")
        for i in range(len(quests)):
            self.single_quest_string(quests[i], i+1)

    def single_quest_string(self, quest: Quest, number: int):
        print(f"    '{number}':")
        print(f"      Name: {self.job.name} (lvl {quest.quest_difficulty.difficulty_level})")
        print(f"      Objectives:")
        for objective in quest.objectives_selected:
            print(f"      - {objective.type};{objective.block};{objective.count}")
        print(f"      RewardCommands:")
        print(f"      - jobs promote [playerName] {self.job.name} {quest.quest_difficulty.levels}")
        print(f"      - crates give physical {self.job.key_type}Crate 1 [playerName]")
        print(f"      - scoreboard players add [playerName] questpoints {quest.quest_difficulty.quest_points}")
        print(f"      - msg [playerName] Completed {self.job.name} {quest.quest_difficulty.difficulty_level} quest!")
        print(f"      RewardDesc:")
        print(f"      - Earn {quest.quest_difficulty.quest_points} quest point(s)!")
        print(f"      - Earn {quest.quest_difficulty.levels} job level(s)!")
        print(f"      - Earn {quest.quest_difficulty.keys} {self.job.key_type} key(s)!")

