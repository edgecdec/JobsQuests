import pandas as pd

class Objective:
    def __init__(self, data: dict):
        self.type = data.get('Type', '')
        self.block = data.get('Block', '')
        self.count = data.get('Count', 0)
        self.difficulty = data.get('Difficulty', '')

    def __repr__(self):
        return f"Objective(type='{self.type}', block='{self.block}', count={self.count}, difficulty='{self.difficulty}')"

    def display(self):
        print(f"Type: {self.type}")
        print(f"Block: {self.block}")
        print(f"Count: {self.count}")
        print(f"Difficulty: {self.difficulty}")
