from re import X
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.environ['CDF_LIB'] = '~/CDF/lib'
from spacepy import pycdf
import cdflib

plt.style.use('_mpl-gallery')

cdf_pycdf = pycdf.CDF('dscovr_h0_mag_20220101_v01.cdf')

cdf_pycdf2 = pycdf.CDF('wi_h2_mfi_20220101_v04.cdf')
cdf_data  = cdf_pycdf.copy()
cdf_data2 = cdf_pycdf2.copy()
# print('These are the variables within this file:\n')
arr = cdf_pycdf2['BGSE'][...]
arr[arr > 999] = np.NaN
arr[arr < -999] = np.NaN
# print(cdf_pycdf2['BGSE'][...])


# print(cdf_pycdf.attrs)

# print(cdf_pycdf['SENS'])
# print(cdf_pycdf2)
# print(cdf_data.keys())

# wind_cdf_data = cdflib.cdf_to_xarray('wi_h2_mfi_20220101_v04.cdf', fillval_to_nan=True)

# df = pd.DataFrame(wind_cdf_data)
# print(df)

# print(cdf_data['B1GSE'][...])
# print(cdf_data['B1GSE'].attrs)
# arr = np.array(cdf_data['B1GSE'][:, 2])

x = cdf_data['Epoch1']

# y = cdf_data['B1GSE'][:, 2]

fig, ax = plt.subplots()

ax.plot(x, arr, linewidth=2.0)






# print(arr)

# print(cdf_data['B1GSE'].attrs)

# print(cdf_data2.keys())

# plt.plot(cdf_data['Epoch1'][...])


cdf_pycdf.close()
cdf_pycdf2.close()

plt.show()