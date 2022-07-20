# Script to reformat SRD Monster data for inclusion in fitted model
# Input data: CSV, 1 row per monster
# Output data: jsonl
# Data source:
    # Data scraped from aidedd.org by Travis Tyler
    # (https://www.kaggle.com/datasets/travistyler/dnd-5e-monster-manual-stats)
    # Stats collected here ("SRDmonsters.csv") are all from the D&D SRD and covered by
    # the OGL (https://media.wizards.com/2016/downloads/SRD-OGL_V1.1.pdf)

import pandas as pd
from pathlib import Path

FILE = Path('.')/'GPTRPG'/'SRDread'/'SRDmonsters.csv'

df = pd.read_csv(FILE)

print(df.columns)

# tasks
# determine proper final format
# likely need to split up some columns:
# senses, attributes, actions, legendary_actions