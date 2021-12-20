import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data1.csv")
data=df["average"].tolist()

fig=ff.create_distplot([data],["Average"],show_hist=False)
fig.show()