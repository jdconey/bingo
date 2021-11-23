# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:03:32 2021

@author: never you mind
"""
#####################################################################
##usage python bingo.py num_rows num_cols item_file.xlsx output.txt##
#####################################################################

print('begin')

import pandas as pd
import random
import sys
print('packages imported')
input_file = sys.argv[3]#'bingo.xlsx'#
output_file = sys.argv[4]#'test.txt'#
print('arguments read')
df = pd.read_excel(input_file,header=None) # can also index sheet by name or fetch all sheets
clues = df[0].tolist()
ints = []

#change number of clues
num_rows = sys.argv[1]#4 works well
num_cols = sys.argv[2]#3 works well

if num_rows*num_cols>len(clues):
    raise Exception("you melon, you need more clues in the spreadsheet.\n You asked for "+str(num_rows*num_cols)+" items in your bingo card, and only gave me a list of "+str(len(clues))+" to choose from, you wally.")
    
if num_rows*num_cols<1:
    raise Exception("negative bingo cards are a no-no.")

if len(clues)<1:
    raise Exception("put some clues in your spreadsheet")

print('collecting random clues')
while len(ints)<num_rows*num_cols:
    new = random.randint(0,len(clues)-1)
    if new not in ints:
        ints.append(new)

score_sheet = []
for item in ints:
    score_sheet.append(clues[item])
   
formatted = []

orders=[]
i=0
while i<num_rows*num_cols:
   j=0
   row=[]
   while j<num_cols:
       row.append(i)
       i=i+1
       j=j+1
   orders.append(row)

cols=[]
j=0
while j<len(orders[0]):
    cols.append([])
    j=j+1
j=0
while j<len(orders):
    k=0
    while k<len(orders[j]):
        cols[k].append(orders[j][k])
        k=k+1
    j=j+1

maxes=[]
for k in cols:
    lens=[]
    for l in k:
        lens.append(len(score_sheet[l]))
    maxes.append(max(lens))
    

formatted = score_sheet.copy()
i=0
while i<len(formatted):
    string=''
    k=0
    while k<len(cols):
        if i in cols[k]:
            oo=k
        k=k+1
    lenty = maxes[oo]
    j=len(formatted[i])
    print(j,lenty)
    while j<lenty:
        string=string+' '
        j=j+1
    formatted[i] = formatted[i]+string
    i=i+1

top_border = sum(maxes)+num_cols
k=0
border=''
while k<top_border:
    border=border+'-'
    k=k+1

layout=[]
x=0
inc=0
while x<num_rows:
    y=0
    row='|'
    while y<num_cols:
        row = row + formatted[inc] + '|'
        inc=inc+1
        y=y+1
    layout.append(row)
    x=x+1


print('making bingo card')

txt_file = ['BINGO']
for k in layout:
    txt_file.append(border)
    txt_file.append(k)
txt_file.append(border)

textfile = open(output_file, "w")
for n in txt_file:
    textfile.write(n + "\n")
textfile.close()

print('done')