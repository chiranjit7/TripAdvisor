from collections import defaultdict
from operator import itemgetter, attrgetter
import pandas as pd
import csv
import sys
import xlrd
import datetime as dt
import os
import numpy as np
word = 'MH1_SFB'
inputfile = '/home/amisha/Desktop/sourcedata/02_MH_ANALOG/'
path = '/home/amisha/Desktop/sourcedata/02_MH_ANALOG/'
files = os.listdir(path)

for idx, infile in enumerate(files):
   outputfile = path+"1_"+infile+".csv"
   saveout = sys.stdout
   SavedConcordance = open(outputfile, "w")   
   sys.stdout = SavedConcordance
   workbook = xlrd.open_workbook(path+infile)
   worksheet = workbook.sheet_by_index(0)
   for row in xrange(2, worksheet.nrows):
       if worksheet.cell_value(row,3) != '':
          #print row
          date= str(worksheet.cell_value(row,3))+","+ str(dt.datetime(*xlrd.xldate_as_tuple(worksheet.cell_value(row,2),workbook.datemode)))
          print date   

   sys.stdout = saveout                                     
   SavedConcordance.close() 

   with open(outputfile) as f:
         r = csv.reader(f)
         data = [line for line in r]
   with open(outputfile,'w') as f:
         w = csv.writer(f)
         w.writerow([word+'value','timestamp'])
         w.writerows(data)

#df = pd.DataFrame.from_csv(outputfile)

#lis=df['value'].groupby(df['timestamp']).describe()
#print list
#pd.pivot_table(df,index=["timestamp"])
#pd.pivot_table(df,index=[("value")])
#pd.pivot_table(df,index=["timestamp"])
#print pd.pivot_table(df,index=["timestamp"], values=[float("value")], aggfunc=[np.sum,np.mean],fill_value=0,margins=True)

   



