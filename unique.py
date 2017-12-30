
with open('input_file.txt','r') as f:                                                                                                                                                                                                                                                 
    distinct_content=set(f.readlines())                                                                                                                                                                                                                                                   

to_file=""                                                                                                                                                                                                                                                                       
for element in distinct_content:                                                                                                                                                                                                                                                               
    to_file=to_file+element                                                                                                                                                                                                                                                           
with open('output_file.txt','w') as w:                                                                                                                                                                                                                                                  
    w.write(to_file) 
		
		
#-90505483 - Alim