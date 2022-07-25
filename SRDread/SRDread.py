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

INPUTFILE = Path('.')/'SRDread'/'SRDmonsters.csv'
OUTPUTFILE = Path('.')/'SRDread'/'testModel.jsonl'

fullData = pd.read_csv(INPUTFILE)
fullData.rename(columns={"intel":"int","strength":"str"},inplace=True)
#print(fullData.columns)

testData = fullData[['name','size','type','cr','ac','hp','str','dex','con','int','wis','cha']].copy()

### reformat for testing

promptJSON = pd.DataFrame.to_json(testData[['name','size','type','cr']],orient="records",lines=True)
completionJSON = pd.DataFrame.to_json(testData[['name','ac','hp','str','dex','con','int','wis','cha']],orient="records",lines=True)

promptMark = ''
promptList = promptJSON.split('\n')[:-1]
completionList = completionJSON.split('\n')[:-1]

testJSON = ''
for p,c in zip(promptList,completionList):
    testJSON += "{"+f"\"prompt\":{p+promptMark},\"completion\":{c}"+"}\n"

with open(OUTPUTFILE,"w") as f:
    f.write(testJSON)


## Notes - 2022.07.24
# I should probably do the mathematical elements using python directly.
# And generate the action list using OA?
# It is possible that the basic usage is entirely calculated and does not require a model at all.
# Hurray for learning!