import streamlit as st
import polars as pl

from utils.player import PlayerFeats
from plots.basePlot import BasePlot

# Configurações da página
plots  = BasePlot()
player = PlayerFeats()

st.set_page_config(
    page_title="NBA Project",
    page_icon="🏀",
    layout="wide",
)

def player_page():
    df = pl.read_parquet('data/nba_database.parquet')

    players = df.select("Player").unique().to_series().sort().to_list()
    player_name = st.selectbox("Choose a player", players, index=None)


    if player_name is not None:
        df_player = df.filter(pl.col('Player') == player_name).sort('Data')
        
        plot = plots.basicLinesChart(df_player, ["PTS", "AST", "3PA"])
        perc = plots.basicLinesChart(df_player, ["FG%", "TOV", "3P%"])
        
        try:
            file_name = player_name.replace(" ", "_") + ".png"
            st.image(f"imagens_jogadores/{file_name}")
        except Exception as e:
            print(e)

        st.header(f'{player_name} Stats over the time')
        with st.expander(label="Table Stats Game", expanded=False):
            st.dataframe(df_player)

        with st.container(border=True):
            c1, c2 = st.columns([1, 1])
            with c1:
                st.plotly_chart(plots.basicBarChart(player.top_teams_against('PTS', df_player), 'Oponent', 'Avarage PTS'))
            with c2:    
                st.plotly_chart(plots.basicBarChart(player.top_teams_against('FG%', df_player), 'Oponent', 'Avarage FG%'))

            c3, c4 = st.columns([1, 1])
            with c3:
                st.plotly_chart(plots.basicBarChart(player.top_teams_against('3P', df_player), 'Oponent', 'Avarage 3P'))
            with c4:
                st.plotly_chart(plots.basicBarChart(player.top_teams_against('3P%', df_player), 'Oponent', 'Avarage 3P%'))
        
        st.plotly_chart(plot, use_container_width=True)
        st.plotly_chart(perc, use_container_width=True)

if __name__ == '__main__':
    player_page()
