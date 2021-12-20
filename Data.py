import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("Data.csv")
data=df["temp"].tolist()

fig=ff.create_distplot([data],["TEMP"],show_hist=False)
fig.show()