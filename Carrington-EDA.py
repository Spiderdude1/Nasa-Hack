from cProfile import label
from email import header
from time import tzname
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.environ['CDF_LIB'] = '~/CDF/lib'
from spacepy import pycdf
import cdflib
from dtw import *
import datetime
dscovr_cdf = pycdf.CDF('dscovr_h0_mag_20220101_v01.cdf')
# print(dscovr_cdf['Epoch1'][...])
wind_cdf = pycdf.CDF('wi_h2_mfi_20220101_v04.cdf')
dscovr_cpy  = dscovr_cdf.copy()
wind_cpy = wind_cdf.copy()

discover2_df = pd.DataFrame(dscovr_cdf['B1GSE'], columns= ['x', 'y', 'z'])
# pick only every 100 rows
discover2_df = discover2_df[0::50]
discover2_df['amp'] = np.sqrt(discover2_df['x'] ** 2 + discover2_df['y'] ** 2 + discover2_df['z'] ** 2)
discover2_df['time'] = datetime.datetime(2022, 1, 1, 0, 0, 0).timestamp() + (discover2_df.index-1)
# pd.to_datetime(dscovr_cdf['Epoch1'].tolist()._type('int64')) // 10**9
pd.options.display.float_format = '{:.5f}'.format
discover2_df['date'] = pd.to_datetime(discover2_df['time'],unit='s', utc=True)
discover2_df = discover2_df.drop(discover2_df[discover2_df.amp >=999].index)

print(discover2_df.head(5))
print(discover2_df.tail(5))

# wind_df = pd.DataFrame(wind_cdf['BGSE'][:100], columns= ['x', 'y', 'z'])
wind_df = pd.DataFrame(wind_cdf['BGSE'], columns= ['x', 'y', 'z'])
wind_df = wind_df[0::50]
wind_df['amp'] = np.sqrt(wind_df['x'] ** 2 + wind_df['y'] ** 2 + wind_df['z'] ** 2)
wind_df['time'] = datetime.datetime(2022, 1, 1, 0, 0, 0).timestamp() + (wind_df.index-1) / 10.715
wind_df['time'] = wind_df['time']
wind_df['date'] = pd.to_datetime(wind_df['time'],unit='s', utc=True)
wind_df = wind_df.drop(wind_df[wind_df.amp >=999].index)
print(wind_df.head(5))
print(wind_df.tail(5))
print(wind_df.count)

plt.style.use('ggplot')
plt.plot(discover2_df.date, discover2_df.amp, label="DSCOVR Satellite (L1)")
plt.plot(wind_df.date, wind_df.amp, label='Wind Satellite (L2)')
plt.xlabel('Time (Datetime format: PST)')
plt.ylabel('Amplitude of magnetic flux (in nanotesla)')
plt.legend()
plt.show()

dscovr_cdf.close()
wind_cdf.close()