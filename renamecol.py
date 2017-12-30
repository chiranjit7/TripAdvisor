import pandas as pd
df = pd.read_csv('/home/amisha/Desktop/sourcedata/dump/output_dump.csv')
df.columns 
df.rename(columns={'Unnamed: 0': 'wordno','1st': 'word','2nd': 'count','filenum': 'filenum'}, inplace=True)
#df = df.rename(columns={'': 'wordno', '1st': 'word','2nd': 'count','filenum': 'filenum'},inplace=True)
#print df
df.to_csv('/home/amisha/Desktop/sourcedata/dump/example.csv')

df = pd.read_csv('/home/amisha/Desktop/sourcedata/dump/example.csv')
df.apply(pd.to_numeric, errors='ignore')
df['count'].groupby([df['wordno']]).mean().unstack()
