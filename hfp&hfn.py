import pandas as pd

df = pd.read_csv("cps project.csv")

for i in range(1,7):
    df = df.replace("s"+str(i),i)

sum=[]

for i in range(1,10):
    s=[]
    for j in range(0,7):
        a=(((df["CA"+str(i)+"xp"][j])*(df["CA"+str(i)+"yp"][j]))+((df["CA"+str(i)+"xn"][j])*(df["CA"+str(i)+"yn"][j])))
        s.append(a)
    sum.append(s)

print(sum)

positive = []

for i in range(0,9):
    if(i<7):
        positive.append(sum[i].index(max(sum[i])))
    else:
        positive.append(sum[i].index(min(sum[i])))

print(positive)

negative = []

for i in range(0,9):
    if(i<7):
        negative.append(sum[i].index(min(sum[i])))
    else:
        negative.append(sum[i].index(max(sum[i])))

print(negative)

for i in range(1,7):
    df = df.replace(i,"s"+str(i))

pv = []

b=1
for i in positive:
    a = df["CA" + str(b) + "xp"][i] + "(" +str( df["CA" + str(b) + "yp"][i]) + ") ," + df["CA" + str(b) + "xn"][i] + "(" + str(df["CA" + str(b) + "yn"][i]) + ")"
    pv.append(a)
    b=b+1


print(pv)

nv = []

b = 1
for i in negative:
    a = df["CA" + str(b) + "xp"][i] + "(" +str( df["CA" + str(b) + "yp"][i]) + ") ," + df["CA" + str(b) + "xn"][i] + "(" + str(df["CA" + str(b) + "yn"][i]) + ")"
    nv.append(a)
    b=b+1


print(nv)

