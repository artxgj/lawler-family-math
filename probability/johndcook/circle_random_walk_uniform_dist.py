"""
Convergence rate of random walk on integers mod p
https://www.johndcook.com/blog/2019/12/17/random-walk-on-circle/

Source code from John D. Cook
"""

from numpy import zeros
from numpy.random import binomial
import matplotlib.pyplot as plt

p = 25
N = p*p//2
reps = 100000

count = zeros(p)

for _ in range(reps):
    n = 2*binomial(N, 0.5) - N
    count[n%p] += 1

plt.bar(range(p), count/reps)
plt.show()
