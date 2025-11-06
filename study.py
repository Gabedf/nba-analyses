# %% 
import sqlite3
import duckdb
import polars as pl
from itables import show
import plotly.express as px

# %%
df = pl.read_csv('database_24_25.csv', separator=',', ignore_errors=True)
df = df.with_columns(
    pl.col("Data").str.strptime(pl.Date, "%Y-%m-%d")
)

# %%
show(df)

# %%
fig = px.line(df.filter(pl.col('Player') == 'Jayson Tatum'), 
              x='Data', 
              y='PTS',
              )
fig.show()

# %%
df = df.sort(by='Player')
# %%
df.write_parquet('last_season.parquet')
# %%
media_pts = (
    df.filter(pl.col("Player") == "Anthony Davis")
      .group_by("Opp")
      .agg(pl.col("PTS").mean().alias("Media_PTS"))
      .sort("Media_PTS", descending=True)
)

# %%
show(media_pts)
# %%
