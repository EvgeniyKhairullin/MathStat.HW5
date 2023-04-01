import numpy as np
from scipy import stats
z_h = (17.5 - 17)/(2 / np.sqrt(100))
print(z_h);
alpha = 0.05
stats.norm.ppf(1 - alpha)

x = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
x_mean = x.mean()
x_std = x.std(ddof = 1)
fact = (x_mean - 200) / x_std * np.sqrt(10)
print(fact)
crit = 3.25
crit
stats.t.ppf(1 - 0.01 / 2, df = len(x) - 1)
x_1 = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
x_2 = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

stats.ttest_rel(x_1, x_2)