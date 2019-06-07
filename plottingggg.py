import pandas as pd
from matplotlib import pyplot as plt

x = [1,2,3]
y = [2,5,8]


plt.plot(x,y)
#plt.show()

import time as t

seconds = int(input('How many seconds to wait?'))

for i in range(seconds):
   countdown = (str(seconds - i) + ' seconds remain')
   print (countdown)
   t.sleep(1)
   if countdown = '' :
      exit()