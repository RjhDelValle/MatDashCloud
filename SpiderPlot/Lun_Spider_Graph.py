"""
Lun Spider Graph Version 2
Roberto J. Herrera
"""
#We import our libraries
#%%We import out packages first
#import plotly.graph_objects as go
import plotly.graph_objects as go
import pandas as pd

#%%
#We create a function for this
def spider_chart(threshold_df,target_dfs=[],performance_threshold=[],
                 categories=["Underperforming", "Satisfactory","Overperforming"]):
    threshold_df=threshold_df.append(threshold_df.iloc[0])
    #target_df=target_df.append(target_df.iloc[0])
    fig = go.Figure()
    count=0
    #This will be used to repeat the percentage threshold across the chart
    x=len(threshold_df)
    for i in performance_threshold:
        #We create a table where we have the percentage threshold value repeated x times
        percent= [i]*x
        fig.add_trace(go.Scatterpolar(
          r=percent,theta=threshold_df["sample"],
          fill='none',
          mode = 'lines',
          #line_color='black',
          name=categories[count])
            )
        count +=1
    threshold_df=threshold_df[:-1]
    threshold=threshold_df["value"]
    # We used the enumerate function to access the data frames
    # insider target_dfs and target for the actual values of the row
    for i,target in enumerate(target_dfs):
       count=0
       fig.add_trace(go.Scatterpolar(
           r=target.loc[:,"value"]/threshold[count],theta=target.loc[:,"sample"],
           fill='toself',
           name=f'Sample {count + 1}'))
       count +=1
    #This formats the chart itself, like font color and size
    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
        )),font=dict(
            size=17,
            color="black")),
    fig.show(renderer="jpg")
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
#We test out the function 
spider_chart(threshold_df,[target_df,target1_df],performance_threshold=[0.5,0.75,1])
