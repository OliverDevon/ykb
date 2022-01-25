import csv
import pandas as pd
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv("LOL.csv")
heightList=df['Height(Inches)'].to_list()
weightList=df['Weight(Pounds)'].to_list()

weightMean=statistics.mean(weightList)
heightMean=statistics.mean(heightList)

weightMedian=statistics.median(weightList)
heightMedian=statistics.median(heightList)

weightMode=statistics.mode(weightList)
heightMode=statistics.mode(heightList)

height_std_dev= statistics.stdev(heightList)
weight_std_dev= statistics.stdev(weightList)

height_first_std_dev_start, height_first_std_dev_end= heightMean-height_std_dev, heightMean+height_std_dev
height_second_std_dev_start, height_second_std_dev_end= heightMean-(2*height_std_dev), heightMean+(2*height_std_dev)
height_third_std_dev_start, height_third_std_dev_end= heightMean-(3*height_std_dev), heightMean+(3*height_std_dev)


fig = ff.create_distplot([heightList], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[heightMean, heightMean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[height_first_std_dev_start, height_first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[height_first_std_dev_end, height_first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[height_second_std_dev_start, height_second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[height_second_std_dev_end, height_second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[height_third_std_dev_start, height_third_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[height_third_std_dev_end, height_third_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()