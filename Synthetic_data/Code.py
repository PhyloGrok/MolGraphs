import pandas as pd
import numpy as np

df = pd.read_csv('1790Nanostring.csv')
df.drop(columns=['Accession', 'Analyte'], inplace=True)

df_numeric = df.set_index('ProbeID')

df2 = df_numeric.T

m = df2.mean(axis=1)
s = df2.std(axis=1)
df3 = np.zeros((6, 1000, 1045))

for i in range(6):
  df3[i] = np.random.normal(loc=m[i], scale=s[i], size=(1000,1045))
print('Total datapoints:', df3.size)
print(df3)
import pandas as pd

