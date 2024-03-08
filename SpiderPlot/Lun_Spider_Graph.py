"""
Lun Spider Graph
Roberto Herrera y del Valle
"""
#%%We import out packages first
#import plotly.express as pl
import plotly.graph_objects as go
import pandas as pd
#%%We create our data frame for testing out the function
threshold_df = pd.DataFrame(dict(
    value=[10, 3, 4, 30, 15],
    sample=['Roberto','Lun','Ryan','Ankita','Celina']))

target_df = pd.DataFrame(dict(
    value=[4, 1, 2, 6, 3],
    sample=['Roberto','Lun','Ryan','Ankita','Celina']))

target1_df = pd.DataFrame(dict(
    value=[8, 1, 4, 5, 8],
    sample=['Roberto','Lun','Ryan','Ankita','Celina']))
#%%
#We create a function 
#def spider_chart(threshold_df,target_df, values='val',theta='theta'):
#    fig = pl.line_polar(threshold_df,values,theta,line_close=True)
#    fig = pl.line_polar(target_df,values,theta,line_close=True)
#    fig.update_traces(fill='toself')
#    fig.show(renderer="png")
#%%
#We run the function
#spider_chart(threshold_df,target_df,"value","sample")
#%%
#We now use something that is not plotly express
#We go with the one example

fig = go.Figure(
  data=go.Scatterpolar(r=threshold_df["value"],theta=threshold_df["sample"],fill='toself')
                )

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False
)

fig.show(renderer="png")
#%%
#We now introduce two
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=threshold_df["value"],theta=threshold_df["sample"],
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=target_df["value"],theta=target_df["sample"],
      fill='toself',
      name='Product B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 7]
    )),
  showlegend=False
)

fig.show(renderer="png")
#%%
#We create a function for this
def spider_chart(threshold_df,*target_df,long=[0.5,0.75,1],
                 categories=["Underperfoming", "Satisfactory","Overperfoming"]):
    fig = go.Figure()
    threshold=threshold_df["value"]
    count=0
    for i in long:
        percent= [i]*len(threshold)
        fig.add_trace(go.Scatterpolar(
          r=percent,theta=threshold_df["sample"],
          fill='none',
          name=categories[count])
            )
        count +=1
    count=0
    for target in target_df:
        count +=1
        fig.add_trace(go.Scatterpolar(
              r=target["value"]/threshold[count],theta=target["sample"],
              fill='toself',
              name=f'Sample {count}'))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
        ))),
    fig.show(renderer="png")
#%%
#We test out the function 
spider_chart(threshold_df, target_df)

#%%
spider_chart(threshold_df, target_df,target1_df)
