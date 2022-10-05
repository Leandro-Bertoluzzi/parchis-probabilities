import numpy as np
from helpers.utilities import plotArrayValues, powerset

TOTAL = 10000
MAX_MOVEMENTS = 36
coincidences = np.zeros(MAX_MOVEMENTS)

for i in range(TOTAL):
    randnums = np.random.randint(1,7,6)
    alreadyCounted = np.zeros(MAX_MOVEMENTS)

    # Sum of elements
    sumFirstRow = randnums[0] + randnums[1]
    if alreadyCounted[sumFirstRow - 1] == 0:
        coincidences[sumFirstRow - 1] += 1
        alreadyCounted[sumFirstRow - 1] = 1

    if randnums[0] == randnums[1]:
        for subset in powerset(randnums[:4]):
            partialSum = np.sum(subset)
            if alreadyCounted[partialSum - 1] == 0:
                coincidences[partialSum - 1] += 1
                alreadyCounted[partialSum - 1] = 1
        if randnums[2] == randnums[3]:
            for subset in powerset(randnums):
                partialSum = np.sum(subset)
                if alreadyCounted[partialSum - 1] == 0:
                    coincidences[partialSum - 1] += 1
                    alreadyCounted[partialSum - 1] = 1

    # Each individual element
    for index, n in enumerate(coincidences):
        if alreadyCounted[index] == 1:
            continue

        if randnums[0] - 1 == index or randnums[1] - 1 == index:
            coincidences[index] += 1
            alreadyCounted[index] = 1

# Calculate the probabilities
probabilities = coincidences / TOTAL

for index, p in enumerate(probabilities):
    print(f"The probability of moving {index + 1} positions is {p}")

plotArrayValues(probabilities, showLabels=True)