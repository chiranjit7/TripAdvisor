import os
os.chdir("/home/amisha/anaconda2/lib/python2.7")

#Top sites visited by users aged 18 to 25

#read the users file
#lines = open()
fileHandle = open("/home/amisha/Desktop/join/Table3.txt", 'r')

for line in fileHandle:
    fields = line.split('|')
    print fields
    #print(fields[0]) # prints the first fields value
    #print(fields[1]) # prints the second fields value

fileHandle.close()

#users = [line.split('|') for line in lines]      #user name, age (eg - john, 22)
#userlist = [ (u[2]) for u in users]     #split the user name and age
#print len(users), users[0]
#read the page visit file
#pages = open("/home/amisha/Desktop/join/Table1.txt")
#page = [p.split("|") for p in pages]              #user name, website visited (eg - john,google.com)
#pagelist  = [ (p[0],p[1]) for p in page]

#map user and page visits & filter age group between 18 and 25
#usrpage = [[p[1],u[0]] for u in userlist for p in pagelist  if (u[0] == p[0] and u[1]>=18 and u[1]<=25) ]

#for z in usrpage:
#    print(z[0].strip('\r\n')+",1")
