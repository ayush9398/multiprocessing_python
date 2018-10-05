import csv
import pprint
import numpy as np

with open("lymphography.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)

a = np.array(data,dtype=int)
c = a[:,1]
b = np.bincount(c)
ii = np.nonzero(b)[0]
print(a[:,1])
print("break")
arr = list(zip(ii,b[ii]))
print(arr)
