# Some are the Examples of the Random Number Generation:

import numpy as np

# # Simulate 100k coin flips
# rng = np.random.default_rng()
# flips = rng.integers(0, 2, size=100000)  # 0 = tails, 1 = heads
# prob_heads = np.mean(flips)
# print("Estimated probability of heads:", prob_heads)


# import time

# # Python Loop
# start = time.time()
# squares = [i**2 for i in range(1000000)]
# end = time.time()
# print("Loop time:", end - start)

# # NumPy vectorized
# start = time.time()
# arr = np.arange(1000000)
# squares_np = arr**2
# end = time.time()
# print("Vectorized time:", end - start)


