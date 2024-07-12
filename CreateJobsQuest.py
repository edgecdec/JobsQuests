import os
import glob

import pandas as pd

from TemplateClasses.Job import Job
from TemplateClasses.JobYAMLTemplate import JobYAMLTemplate
from TemplateClasses.Objective import Objective
from TemplateClasses.Quest import Quest
from TemplateClasses.QuestDifficulty import QuestDifficulty

# Folder containing the CSV files
folder_path = 'JobsCSVs'

jobs = []

# Loop over each CSV file in the folder
for csv_file in glob.glob(os.path.join(folder_path, '*.csv')):
    # Extract job name from the file name
    file_name = os.path.basename(csv_file)
    job_name = file_name.replace('Jobs Quests - ', '').replace('.csv', '')

    # Create a Job instance
    job = Job(job_name)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Create and add Objective instances to the Job
    for index, row in df.iterrows():
        objective = Objective(row)
        job.add_objective(objective)

    # Display the Job and its objectives
    job.display()
    print('Completed job:', job_name)
    print()

    jobs.append(job)

# Read the CSV file into a DataFrame
file_path = 'Jobs Quests - Difficulty.csv'
df = pd.read_csv(file_path)

# Create a list of QuestDifficulty instances from the DataFrame
quest_difficulties = [QuestDifficulty(row) for index, row in df.iterrows()]

# Display the quest difficulties
for quest in quest_difficulties:
    quest.display()
    print()

for job in jobs:
    quests = []
    for quest_difficulty in quest_difficulties:
        for i in range(20):
            quests.append(Quest(quest_difficulty, job))
    for quest in quests:
        quest.display()
        print()
    JobYAMLTemplate(job, quests)
