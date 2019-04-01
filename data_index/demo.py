import pandas as pd

l_a=range(0,5000)
a=pd.Series(l_a)
print (a)


f=pd.read_csv('../notebook/acc.csv')

f.insert(0,'AA',a)
print(f)