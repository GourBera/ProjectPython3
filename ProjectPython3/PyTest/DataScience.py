'''
Created on May 21, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

import numpy as np
import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


b = np.array([1,5,8,9,4,7,5])
print(b)

df = pd.DataFrame(data = b)
print(df)

# matplotlib
t = np.array([1,5,8,9,4,7,5])
s = np.array([1,2,3,4,5,6,7])
plt.plot(t, s)

plt.xlabel('x - t array')
plt.ylabel('y - s array')
plt.title('Simple Plot')
plt.grid(True)
#plt.savefig("test.png")
plt.show()

# seaborn
sns.set_color_codes("dark")
_ = plt.plot([0, 1], color="g")
_ = plt.plot([0, 2], color="m")

plt.show()




















