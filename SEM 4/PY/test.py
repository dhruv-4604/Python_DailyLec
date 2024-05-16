import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
dat=np.random.randint(1,100,(10,10))
print(dat)

sns.heatmap(data=dat,cmap='tab20')
plt.show()
