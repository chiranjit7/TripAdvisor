import glob
import pandas as pd
import numpy as np

listall = glob.glob("/home/amisha/Desktop/sourcedata/dump/dump*.csv")
all_data = pd.DataFrame()
for f in listall:
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
	
all_data.to_csv('/home/amisha/Desktop/sourcedata/example.csv', encoding='utf-8')
