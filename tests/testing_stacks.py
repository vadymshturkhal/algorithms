from data_structures.stack import Stack
from data_structures.stack_resizing_array import StackResizingArray
from time import time

STACK_LEN = 100000

stacks = {
    "stack         ": Stack,
    "stack resizing": StackResizingArray,
}

for name, stack in stacks.items():
    start_time = time()
    s = stack()

    for i in range(STACK_LEN):
        s.push(i)

    for i in range(STACK_LEN):
        s.pop()

    elapsed_time = time() - start_time
    print(name, elapsed_time)
