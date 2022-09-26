import numpy as np
from utilities import plotArrayValues

TOTAL = 10000
MAX_MOVEMENTS = 12
coincidences = np.zeros(MAX_MOVEMENTS)

for i in range(TOTAL):
    randnums = np.random.randint(1,7,2)

    # Sum of elements
    coincidences[randnums[0] + randnums[1] - 1] += 1

    # Each individual element
    for index, n in enumerate(coincidences):
        if (randnums[0] - 1 == index) or (randnums[1] - 1 == index):
            coincidences[index] += 1

# Calculate the probabilities
probabilities = coincidences / TOTAL

for index, p in enumerate(probabilities):
    print(f"The probability of moving {index + 1} positions is {p}")

plotArrayValues(probabilities, showLabels=True)