import numpy as np
from helpers.utilities import plotArrayValues, powerset

# Edit this variable
MAX_ROWS = 5

TOTAL = 10000
MAX_MOVEMENTS = 12 * MAX_ROWS
coincidences = np.zeros(MAX_MOVEMENTS)

for i in range(TOTAL):
    randnums = np.random.randint(1,7,2*MAX_ROWS)
    alreadyCounted = np.zeros(MAX_MOVEMENTS)

    # First two elements
    for subset in powerset(randnums[:2]):
        partialSum = np.sum(subset)
        if alreadyCounted[partialSum - 1] == 0:
            coincidences[partialSum - 1] += 1
            alreadyCounted[partialSum - 1] = 1

    keepLooping = True
    j = 0
    while j < MAX_ROWS and keepLooping:
        if randnums[j] == randnums[j+1]:
            for subset in powerset(randnums[:2*j+4]):
                partialSum = np.sum(subset)
                if alreadyCounted[partialSum - 1] == 0:
                    coincidences[partialSum - 1] += 1
                    alreadyCounted[partialSum - 1] = 1
        else:
            keepLooping = False
        j += 2

# Calculate the probabilities
probabilities = coincidences / TOTAL

for index, p in enumerate(probabilities):
    print(f"The probability of moving {index + 1} positions is {p}")

plotArrayValues(probabilities, showLabels=False)