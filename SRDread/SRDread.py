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

fullData = pd.read_csv(FILE)
fullData.rename(columns={"intel":"int","strength":"str"},inplace=True)
#print(fullData.columns)

testData = fullData[['name','size','type','cr','ac','hp','str','dex','con','int','wis','cha']].copy()

### reformat for testing
testData = testData.assign(prompt=testData[['name','size','type','cr']].astype(str).apply(" ".join,axis=1)+"\n\n###\n\n")

print(testData['prompt'].head(5))

#testJSON = pd.DataFrame.to_json(testData,orient="records",lines=True)

#print(testJSON)

# tasks
# determine proper final format
# likely need to split up some columns:
# senses, attributes, actions, legendary_actions