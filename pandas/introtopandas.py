#note to self: run >>> jupyter notebook
#before attempting to run
#stuff to check out later https://ipython.org

import pandas as pd
import matplotlib.pyplot as plt
import jupyter
%pylab inline

data = pd.read_csv("hubble_data.csv")
data.set_index("distance", inplace= True) #replacing index
data.head()

data.plot()
plt.show()

"""
headers = ["dist", "rec_vel"]
data_no_headers = pd.read_csv("hubble_data_no_headers.csv", names = headers)
data_no_headers.head()

data_nt_header["dist"]
"""
