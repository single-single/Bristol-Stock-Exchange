import pandas as pd
import string
import matplotlib.pyplot as plt

print(list(string.ascii_uppercase)[0:22])

avgBalance = pd.read_csv("avg_balance.csv",header=None,\
                         names=list(string.ascii_uppercase)[0:22],\
                         index_col=False)

newNames = { "H":"GVWY", "L":"SHVR", "P":"ZIC", "T":"ZIP"}
avgBalance.rename(columns=newNames,inplace=True)
avgBalance.plot(x="B",y=["GVWY","SHVR","ZIC","ZIP"], kind="line")
plt.show(block=True)
