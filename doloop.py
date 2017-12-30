from collections import defaultdict
from operator import itemgetter, attrgetter
import pandas as pd
import numpy as np 
import csv
import sys
import openpyxl

outpufile = '/home/amisha/Desktop/sourcedata/02_MH_ANALOG/'+ '520 MH 01 FEB 2016 03 to 09.xls'
wb = openpyxl.load_workbook('example.xlsx')

# Create dataframe
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])

#print df

groupby_regiment = df['preTestScore'].groupby(df['company'])
groupby_regiment

list(df['preTestScore'].groupby(df['company']))

lis=df['preTestScore'].groupby(df['company']).describe()

#b =np.array([a])

#import transposer

#print b.T

#print groupby_regiment.mean()
#df['postTestScore'].groupby(df['categories']).apply(get_stats).unstack()


#df['preTestScore'].groupby([df['regiment'], df['company']]).mean()

#df['preTestScore'].groupby([df['regiment'], df['company']]).mean().unstack()

#df.groupby(['regiment', 'company']).mean()

#df.groupby(['regiment', 'company']).size()


# Group the dataframe by regiment, and for each regiment,
#for name, group in df.groupby('regiment'): 
#    # print the name of the regiment
#    print(name)
#    # print the data of that regiment
#    print(group)

#list(df.groupby(df.dtypes, axis=1))

#df.groupby('regiment').mean().add_prefix('mean_')

#def get_stats(group):
#    return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}

#bins = [0, 25, 50, 75, 100]
#group_names = ['Low', 'Okay', 'Good', 'Great']
#df['categories'] = pd.cut(df['postTestScore'], bins, labels=group_names)

#df['postTestScore'].groupby(df['categories']).apply(get_stats).unstack()



