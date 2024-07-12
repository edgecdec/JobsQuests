from collections import defaultdict


class QuestDifficulty:
    def __init__(self, data: dict):
        self.difficulty_level = data.get('Difficulty Level', '')
        self.difficulties_count = 0
        self.difficulties = self.parse_difficulty_string(data.get('Difficulties', ''))
        self.levels = data.get('Levels', 0)
        self.keys = data.get('Keys', 0)
        self.quest_points = data.get('QuestPoints', 0)

    def parse_difficulty_string(self, difficulty_string):
        # Split the string on the "/" delimiter
        difficulties = difficulty_string.split('/')
        self.difficulties_count = len(difficulties)

        # Create a defaultdict to count occurrences
        difficulty_counts = defaultdict(int)

        # Count each difficulty
        for difficulty in difficulties:
            if difficulty:  # Ensure that the difficulty is not an empty string
                difficulty_counts[difficulty] += 1

        return dict(difficulty_counts)

    def __repr__(self):
        return (f"QuestDifficulty(difficulty_level='{self.difficulty_level}', "
                f"difficulties='{self.difficulties}', levels={self.levels}, "
                f"keys={self.keys}, quest_points={self.quest_points})")

    def display(self):
        print(f"Difficulty Level: {self.difficulty_level}")
        print(f"Difficulties: {self.difficulties}")
        print(f"Levels: {self.levels}")
        print(f"Keys: {self.keys}")
        print(f"Quest Points: {self.quest_points}")
