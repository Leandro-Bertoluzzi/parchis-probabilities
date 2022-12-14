import matplotlib.pyplot as plt
from itertools import chain, combinations

def plotArrayValues(values, showLabels=False):
    x = range(1, len(values) + 1)

    plt.xlabel('Movements')
    plt.ylabel('Probability')
    plt.title('Probability of moving x places')
    plt.xlim(0, len(values) + 1)
    plt.ylim(0.0, 1.0)
    plt.grid(True)
    plt.plot(x, values, '-o')

    if showLabels:
        axes = plt.gca()
        for i, v in enumerate(values):
            axes.text(i+1, v+0.03, "%.2f" %v, ha="center")

    plt.show()

def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))