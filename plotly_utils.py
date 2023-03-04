import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd

def create_multiple_plot(df, variable_names, time='Time', verbose=False):        
    fig = go.Figure(layout=go.Layout(xaxis={'spikemode': 'across'}))
    colors = ['#727272', '#56b4e9', "#009E73", "#000000"]
    last = len(variable_names) - 1
    

    for i in range(0, len(variable_names)):
        var = variable_names[i]
        
        if i <= (len(colors)):
            color = colors[i]
        else:
            color = ''
        

        if i != last:
            fig.add_trace(go.Scatter(x=df[time], y=df[var], name=var, marker={'color': color}, yaxis="y1"))
        else:
            fig.add_trace(go.Scatter(x=df[time], y=df[var], name=var, marker={'color': color}, yaxis="y2"))
    


    fig.update_layout(
            yaxis=dict(
                titlefont=dict(
                    color="#000000"
                ),
                tickfont=dict(
                    color="#000000"
                )
            ),
            yaxis2=dict(
                tickfont=dict(
                    color=color
                ),
                anchor="free",
                overlaying="y",
                side="left",
                position=1
            ))
            
    fig.update_layout(
        xaxis=go.layout.XAxis(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True,
            ),
            type="date",
        )
    )
    
    fig = fig.update_xaxes(spikemode='across+marker')
    fig = fig.update_layout(hovermode="x")

    return fig
