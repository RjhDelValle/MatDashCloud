# -*- coding: utf-8 -*-
"""
Lun Spider Graph Version 2
Roberto J. Herrera
"""
#We import our libraries
#%%We import out packages first
#import plotly.graph_objects as go
import plotly.graph_objects as go
import pandas as pd
#%%We create our data frame for testing out the function
threshold_df = pd.DataFrame(dict(
    value=[10, 3, 4, 30, 15],
    sample=['Roberto','Lun','Ryan','Ankita','Celina']))

target_df = pd.DataFrame(dict(
    value=[10, 1, 2, 6, 3],
    sample=['Roberto','Lun','Ryan','Ankita','Celina']))

target1_df = pd.DataFrame(dict(
    value=[8, 1, 4, 5, 8],
    sample=['Roberto','Lun','Ryan','Ankita','Celina']))

#%%
#We create a function for this
def spider_chart(threshold_df,*target_df,long=[0.5,0.8,1],
                 categories=["Underperfoming", "Satisfactory","Overperfoming"]):
    threshold_df=threshold_df.append(threshold_df.iloc[0])
    #target_df=target_df.append(target_df.iloc[0])
    fig = go.Figure()
    count=0
    for i in long:
        percent= [i]*len(threshold_df)
        fig.add_trace(go.Scatterpolar(
          r=percent,theta=threshold_df["sample"],
          fill='none',
          mode = 'lines',
          #line_color=['black','aqua','honeydew'],
          name=categories[count])
            )
        count +=1
    threshold_df=threshold_df[:-1]
    threshold=threshold_df["value"]
    for target in target_df:
        count=0
        fig.add_trace(go.Scatterpolar(
              r=target["value"]/threshold[count],theta=target["sample"],
              fill='toself',
              name=f'Sample {count+1}'))
        count +=1
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
        )),font=dict(
            size=15,
            color="black")),
    fig.show(renderer="png")
#%%
#We test out the function 
spider_chart(threshold_df,target_df,target1_df)
