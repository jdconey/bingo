# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:03:32 2021

@author: never you mind
"""
#################################################
#usage python bingo.py item_file.xlsx output.txt#
#################################################

print('begin')

import pandas as pd
import random
import sys
print('packages imported')
input_file = sys.argv[1]
output_file = sys.argv[2]
print('arguments read')
df = pd.read_excel(input_file,header=None) # can also index sheet by name or fetch all sheets
clues = df[0].tolist()
ints = []

#change number of clues, bit of a faff tbf sorry
num_clues = 12
print('collecting random clues')
while len(ints)<num_clues:
    new = random.randint(0,len(clues)-1)
    if new not in ints:
        ints.append(new)

score_sheet = []
for item in ints:
    score_sheet.append(clues[item])
   
formatted = []
orders={'lhs':[0,3,6,9],'ctr':[1,4,7,10],'rhs':[2,5,8,11]}

lhs = max(len(score_sheet[0]),len(score_sheet[3]),len(score_sheet[6]),len(score_sheet[9]))
ctr = max(len(score_sheet[1]),len(score_sheet[4]),len(score_sheet[7]),len(score_sheet[10]))  
rhs = max(len(score_sheet[2]),len(score_sheet[5]),len(score_sheet[8]),len(score_sheet[11])) 

formatted = score_sheet.copy()

i=0
while i<len(formatted):
    string=''
    if i in orders['lhs']:
        lenty=lhs
    elif i in orders['ctr']:
        lenty=ctr
    elif i in orders['rhs']:
        lenty=rhs
    j=len(formatted[i])
    while j<lenty:
        string=string+' '
        j=j+1
    formatted[i] = formatted[i]+string
    i=i+1
    
top_border = lhs+ctr+rhs+2
k=0
border=''
while k<top_border:
    border=border+'-'
    k=k+1

layout=[]
layout.append(formatted[0]+'|'+formatted[1]+'|'+formatted[2])
layout.append(formatted[3]+'|'+formatted[4]+'|'+formatted[5])
layout.append(formatted[6]+'|'+formatted[7]+'|'+formatted[8])
layout.append(formatted[9]+'|'+formatted[10]+'|'+formatted[11])

print('making bingo card')
    
txt_file=['ICAS INTERNAL SEMINAR BINGO',border,layout[0],border,layout[1],border,layout[2],border,layout[3],border]
textfile = open(output_file, "w")
for n in txt_file:
    textfile.write(n + "\n")
textfile.close()

print('done')