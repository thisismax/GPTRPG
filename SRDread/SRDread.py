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

FILE = Path('.')/'SRDread'/'SRDmonsters.csv'

fullData = pd.read_csv(FILE)
fullData.rename(columns={"intel":"int","strength":"str"},inplace=True)
#print(fullData.columns)

testData = fullData[['name','size','type','cr','ac','hp','str','dex','con','int','wis','cha']].copy()

### reformat for testing
# this is not quite right - I'm losing the column names doing it this way
#testData = testData.assign(prompt=testData[['name','size','type','cr']].astype(str).apply("\n".join,axis=1)+"\n\n###\n\n")
#testData = testData.assign(completion=testData[['ac','hp','str','dex','con','int','wis','cha']].astype(str).apply("\n".join,axis=1))

#print(testData['completion'].head(5))

promptJSON = pd.DataFrame.to_json(testData[['name','size','type','cr']],orient="records",lines=True)
completionJSON = pd.DataFrame.to_json(testData[['ac','hp','str','dex','con','int','wis','cha']],orient="records",lines=True)

print(promptJSON)
print(completionJSON)

# Ha I have to figure out how to format this properly so that it's convenient to read later also...
# Also - apparently openAI has already read the SRD and knows the stats.

# tasks
# determine proper final format
# likely need to split up some columns:
# senses, attributes, actions, legendary_actions