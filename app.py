import streamlit as st
import polars as pl
import plotly.express as px
import plotly.graph_objects as go

# Configurações da página
st.set_page_config(
    page_title="NBA Project",
    page_icon="🏀",
    layout="wide",
)

def main():
    df = pl.read_csv('database_24_25.csv').with_columns([
        pl.col("Player").str.strip_chars(),   
        pl.col("Data").str.strptime(pl.Date, "%Y-%m-%d"),
    ])

    players = df.select("Player").unique().to_series().sort().to_list()
    player_name = st.selectbox("Choose a player", players, index=None)


    if player_name is not None:
        df_player = df.filter(pl.col('Player') == player_name).sort('Data')

        qt = px.line(
            df_player,
            x="Data",
            y=["PTS", "AST", "3PA"], 
        )

        perc = px.line(
            df_player,
            x="Data",
            y=["FG%", "TOV", "3P%"], 
        )

        qt.update_layout(
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
        )
        perc.update_layout(
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
        )


        with st.container(border=True):
            st.dataframe(df_player)
            
            st.header(f'{player_name} Stats over the time')
            c1, c2 = st.columns([1, 1])
            with c1:
                st.plotly_chart(qt, use_container_width=True)
            with c2:
                st.plotly_chart(perc, use_container_width=True)

if __name__ == '__main__':
    main()
