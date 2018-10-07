import csv
from collections import defaultdict
import numpy as np

def fcount(a, b):
    b = np.bincount(a)
    ii = np.nonzero(b)[0]
    arr = str(list(zip(ii,b[ii])))
    print(arr)


if __name__ == '__main__':

    columns = defaultdict(list) # each value in each column is appended to a list

    with open('lymphography.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                columns[k].append(v) # append the value into the appropriate list
                                     # based on column name k


    fcount(columns['B'],'B')
    fcount(columns['C'],'C')
    fcount(columns['D'],'D')
    fcount(columns['E'],'E')
    fcount(columns['F'],'F')
    fcount(columns['G'],'G')
    fcount(columns['H'],'H')
    fcount(columns['I'],'I')
    fcount(columns['J'],'J')
    fcount(columns['K'],'K')
    fcount(columns['L'],'L')
    fcount(columns['M'],'M')
    fcount(columns['N'],'N')
    fcount(columns['O'],'O')
    fcount(columns['P'],'P')
    fcount(columns['Q'],'Q')
    fcount(columns['R'],'R')
    fcount(columns['S'],'S')
