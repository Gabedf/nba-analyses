import polars as pl

class DataFeatures:
    def __init__(self, df: pl.DataFrame):
        self.df = df

    def rename_columns(self):
        self.df = self.df.rename(
            {
                "Tm": "Team",
                "Opp": "Oponent",
                "Res": "Result"
            }
        )

    def avarage(self, colum):
        self.df = self.df.with_columns(pl.col(colum)
                    .mean()
                    .over(["Player", "Oponent"])
                    .alias(f"Avarage {colum}"))
  
if __name__ == "__main__":
    try:
        caminho = "data/database_24_25.csv"

        df = pl.read_csv(caminho)
        feats = DataFeatures(df)

        feats.rename_columns()
        feats.avarage('PTS')
        feats.avarage('3P')

        feats.avarage('FG%')
        feats.avarage('3P%')

        feats.df.write_parquet('data/nba_database.parquet')
    except Exception as e:
        print(e)

    try:
        team_colors = {
            "DET": "#1D428A",
            "ATL": "#E03A3E",
            "NYK": "#F58426",
            "UTA": "#00471B",
            "OKC": "#007AC1",
            "TOR": "#CE1141",
            "WAS": "#E31837",
            "SAS": "#C4CED4",
            "CHO": "#00788C",
            "MIA": "#98002E",
            "HOU": "#CE1141",
            "BOS": "#007A33",
            "PHO": "#1D1160",
            "LAC": "#1D428A",
            "MIN": "#0C2340",
            "NOP": "#0C2340",
            "PHI": "#006BB6",
            "CHI": "#CE1141",
            "GSW": "#1D428A",
            "DEN": "#0E2240",
            "POR": "#E03A3E",
            "DAL": "#00538C",
            "SAC": "#5A2D81",
            "BRK": "#000000",
            "CLE": "#6F263D",
            "ORL": "#0077C0",
            "MEM": "#5D76A9",
            "LAL": "#FDB927",
            "IND": "#002D62",
            "MIL": "#00471B",
        }

        team_colors_df = (
            pl.DataFrame(list(team_colors.items()), schema=["Team", "Color"])
        )

        # Faz o join com seu DataFrame
        feats.df = feats.df.join(team_colors_df, on="Team", how="left")
        feats.df.write_parquet('data/nba_database.parquet')
    except Exception as e:
        print(e)