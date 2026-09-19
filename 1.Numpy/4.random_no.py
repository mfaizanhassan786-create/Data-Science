import numpy as np

# Simulate 100k coin flips
rng = np.random.default_rng()
flips = rng.integers(0, 2, size=100000)  # 0 = tails, 1 = heads
prob_heads = np.mean(flips)
print("Estimated probability of heads:", prob_heads)


# import time

# # Python loop
# start = time.time()
# squares = [i**2 for i in range(1000000)]
