import plotly.express as px
import polars as pl

class BasePlot:
    def __init__(self):
        self.type = None 

    def basicLinesChart(self, df: pl.DataFrame, y):
        color_base = df.select('Color').to_series()[0]

        palette    = [color_base, "#FFFFFF", "#7B7B7B"]  
        palette    = palette[:len(y)]

        fig = px.line(
            df,
            x="Data",
            y=y,
            color_discrete_sequence=palette
        )

        fig.update_layout(
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
            plot_bgcolor="rgba(0,0,0,0)",   
            paper_bgcolor="rgba(0,0,0,0)"   
        )

        return fig

    def basicBarChart(self, df: pl.DataFrame, x, y):
        color = df.select('Color').to_series()[0]
        fig = px.bar(
            df,
            x=x,
            y=y,
            text=y,                       
            color_discrete_sequence=[color]
        )

        fig.update_traces(
            textposition="inside",        
            textfont=dict(size=18)        
        )

        return fig
