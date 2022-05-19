import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weights) in weights.items():
        for _ in range(weights):
            container_list.append(name)

    return np.random.choice(container_list)


other_weights = {
    'winning': 1,
    'breaking_even': 2,
    'lossing': 3
}

print(weighted_lottery(other_weights))