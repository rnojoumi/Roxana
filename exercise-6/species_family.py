from collections import Counter
import csv
import sys
name = sys.argv[1]

file_object=("name")

reader = csv.reader(file_object)

mylist=[]

next(reader, None)
next(reader, None)
next(reader, None)


#counter will make a dictionary of the families and the number of them repeated. 
for row in reader:
    
    mylist.append(row[7])
    
counted = Counter(mylist)    

for keys, values in counted.items():
        print(str(values)+" total species in Family "+ keys)
     


file_object.close()

