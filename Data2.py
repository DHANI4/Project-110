import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("data1.csv")
data=df["average"].tolist()

def randomsetofMean(counter):
    dataSet=[] 
    for i in range(0,counter):
        rand_index=random.randint(0,len(data)-1)
        value=data[rand_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean 

def showGraph(meanList):
    df=meanList
    mean1=statistics.mean(df)
    fig=ff.create_distplot([df],["Temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,1],mode="lines",name="Mean"))
    fig.show()

def Setup():
    ml=[]
    for i in range(0,1000):
      r=randomsetofMean(200)
      ml.append(r)
    showGraph(ml)
    #sd
    sd=statistics.stdev(ml)
    print(sd)

Setup()