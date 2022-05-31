import numpy as np
import pandas as pd
normal_sample = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
random_sample = np.random.random(size = 10000)
gamma_sample = np.random.gamma(2, size = 10000)
df = pd.DataFrame({'normal': normal_sample, 'random': random_sample, 'gamma': gamma_sample})
df.head()
df.describe()
print(df.describe())
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis = [10, 90])
plt.show()

dff = pd.DataFrame(data = df, columns = ["normal", "random", "gamma"])
sns.boxplot(x = None, y = None, data = dff)
bp = sns.boxplot(x = "variable", y = 'value', data = pd.melt(dff), whis = [0, 100])

plt.show()

import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import axes3d

import seaborn as sns
np.random.seed(1234)

v1 = pd.Series(np.random.normal(0,10,5000), name = 'v1')
v2 = pd.Series(2*v1+np.random.normal(60,15,5000),name = 'v2')

mpl.hist(v1,alpha = 0.7, bins = np.arange(-50,150,5), label = 'v1')
mpl.hist(v2,alpha = 0.7, bins = np.arange(-50,150,5), label = 'v1')

from locale import normalize
mpl.figure()
mpl.hist([v1,v2], histtype="barstacked", density = True)
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3)

mpl.figure()
sns.distplot(v3,hist_kws = {'color':'Teal'}, kde_kws ={'color':'Navy'})

mpl.figure()
sns.jointplot(v1,v2,alpha = 0.5, kind = "hex")
mpl.show()