# MAke a graph to check how many allocations have happened in each block group.
# Input is a file which ultiple lines with each line having one BG number of the allocation.

import sys
import math
import matplotlib.pyplot as plt

file = sys.argv[1]

fd = open(file, "r")
bgs = fd.readlines()

bg_dict=dict()
for bg in bgs:
    bg = bg.strip()
    if bg in bg_dict:
        bg_dict[bg]+=1
    else:
        bg_dict[bg]=1


print(bg_dict)
bg_keys = list(bg_dict.keys())
bg_vals = list(bg_dict.values())

plt.bar(bg_keys, bg_vals, width = 0.4)
 
plt.xlabel("Block group")
plt.ylabel("No. of allocations in group")
plt.title("Allocation spread with mb_optimize_scan=0")
plt.show()
