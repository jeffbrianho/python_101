# debug.py

import pdb

counter = 1

pdb.set_trace() 

while counter <= 5:
    print(counter)
    pdb.set_trace()  # Add breakpoint
    counter += 1