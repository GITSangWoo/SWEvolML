import pandas as pd 
import termplotlib as tpl
import numpy as np
import plotext as plt

df=pd.read_csv("~/data/GML/GML.csv")
x=df['length']
y=df['weight']

newx=df['length'].iloc[-1]
newy=df['weight'].iloc[-1]

plt.plotsize(35,10)
plt.xlabel("length")
plt.ylabel("weight")
plt.scatter(x,y)
plt.scatter([newx], [newy], marker='*', color='red')
plt.title("location of input data")
plt.show()
