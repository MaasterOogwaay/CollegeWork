from scipy.stats import binom

n = 60  # number of trials
p = 1/6  # probability of success (rolling a six)

probability = 1 - binom.cdf(9, n, p)
print("Probability of rolling 10 or more sixes:", probability)
