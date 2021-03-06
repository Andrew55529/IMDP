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

fig = mpl.figure()
ax = fig.add_subplot(111, projection = '3d')

i = np.arange(-1,1,0.01)
X, Y = np.meshgrid(i,i)
Z = X**2-Y**2

ax.plot_wireframe(X,Y,Z,rstride = 4, cstride = 4)

x = y = np.linspace(-3,3,74)
X, Y = np.meshgrid(x,y)

R = np.sqrt(X**2 + Y**2)
Z = np.sin(4 * R) / R

fig, ax = mpl.subplots(1,3,figsize = (14,4), subplot_kw=dict(projection = '3d'))

p = ax[0].plot_surface(X, Y, Z, rstride = 1,cstride = 1)
ax[0].set_xlabel("$x$",fontsize = 16)
ax[0].set_xlabel("$y$",fontsize = 16)
ax[0].set_xlabel("$z$",fontsize = 16)

ax[1].plot_wireframe(X,Y,Z, rstride = 3, cstride = 3, color = "darkgrey")
ax[1].set_title("plot_wireframe")



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