import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression


df_blore = pd.read_csv('Bangalore.csv')
df_global = pd.read_csv('global.csv')
df_blore = df_blore[['year', 'avg_temp']]
df_blore = df_blore.dropna()

#df_blore = df_blore.loc[(df_blore['year'] >= 1800) & (df_blore['year'] <= 1900)]
#df_global = df_global.loc[(df_global['year'] >= 1800) & (df_global['year'] <= 1900)]

# Calculate SMA - Simple Moving Average
df_blore['Bangalore'] = df_blore.iloc[:, 1].rolling(window=10).mean()
df_global['Global'] = df_global.iloc[:, 1].rolling(window=10).mean()

df = pd.concat([df_blore['avg_temp'], df_global['avg_temp_global']], axis=1)
# pcorr = df.corr(method='pearson')
# sb.heatmap(pcorr,
#         xticklabels=pcorr.columns,
#         yticklabels=pcorr.columns,
#         cmap='RdBu_r',
#         annot=True,
#         linewidth=0.5
#     )

df = df.dropna()
Y = df.iloc[:, 0].values.reshape(-1, 1)
X = df.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
y_pred = linear_regressor.predict(X)
X_test = pd.DataFrame([i for i in np.arange(9, 13, 0.5)]).iloc[:, 0].values.reshape(-1, 1)
pred = linear_regressor.predict(X_test)
v = [i for i in np.arange(9, 13, 0.5)]
for i in range(8):
    print(v[i], pred[i])
ax1 = df.plot.scatter(x='avg_temp_global', y='avg_temp', c='DarkBlue')
ax1.set_xlabel('Global Temperature')
ax1.set_ylabel('Bangalore Temperature')
ax1.set_title('Temperature Trend')
plt.plot(X, y_pred, color='red')

# plt.legend()
# plt.show()

