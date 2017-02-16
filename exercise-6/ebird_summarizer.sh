#! /bin/bash
#import sys
#name = sys.argv[1]
#my_file = open(name)
cat $1| tr "\r" "\n" | sed 's/,\s/ /g' > formatted_$1
#name2 = formatted_$1 
python species_family.py formatted_$1

