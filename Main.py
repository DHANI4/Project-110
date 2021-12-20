import plotly.figure_factory as ff
import statistics
import pandas as pd
import plotly.graph_objects as go
import random 

df=pd.read_csv("Data.csv")
data=df["temp"].tolist()

#function to plot the mean of the data
def randomsetofMean(counter):
    dataSet=[]
    for i in range(0,counter):
        rand_index=random.randint(0,len(data)-1)
        value=data[rand_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean 
#function to plot the mean of graph
def showGraph(meanList):
    df=meanList
    mean1=statistics.mean(df)
    fig=ff.create_distplot([df],["Temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,1],mode="lines",name="Mean"))
    fig.show()
# function to call function call
def Setup():
    ml=[]
    for i in range(0,1000):
      r=randomsetofMean(100)
      ml.append(r)
    showGraph(ml)
    #sd
    sd=statistics.stdev(ml)
    print(sd)

#calling main function Setup
Setup()
