import pandas as pd
import numpy as np

df = pd.read_csv("cps project.csv")

wt =[0.061, 0.0915, 0.0577, 0.2228, 0.0839, 0.1194, 0.154, 0.1785, 0.0312]
print(df)


for j in range(1,10):
    for i in range(1, 7):
        df['CA' + str(j) + 'xp'] = df['CA' + str(j) + 'xp'].replace("s" + str(i),i*wt[j-1])
        df['CA' + str(j) + 'xn'] = df['CA' + str(j) + 'xn'].replace("s" + str(i), i * wt[j - 1])


for j in range(1,10):
    for i in range(0, 7):
        df['CA' + str(j) + 'yp'] = df['CA' + str(j) + 'yp'].replace(df['CA' + str(j) + 'yp'][i],(1-(1-(df['CA' + str(j) + 'yp'][i])**wt[j-1])))
        df['CA' + str(j) + 'yn'] = df['CA' + str(j) + 'yn'].replace(df['CA' + str(j) + 'yn'][i], (1 - (1 - (df['CA' + str(j) + 'yn'][i]) ** wt[j - 1])))





print(df)
df.to_csv("hf.csv")
