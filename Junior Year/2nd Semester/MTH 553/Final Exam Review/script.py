import numpy as np

rng = np.random.default_rng()

random_numbers = rng.choice(np.arange(1, 41), size=30, replace=False)

print(random_numbers)