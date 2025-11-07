import polars as pl

class PlayerFeats:
    def __init__(self):
        pass

    def top_teams_against(self, colum, df: pl.DataFrame):
        final_df = df.unique(subset=f"Avarage {colum}")
        return final_df.top_k(3, by=f"Avarage {colum}").select(['Oponent', f'Avarage {colum}', 'Color'])

    def top_teams_against(self, colum, df: pl.DataFrame):
        final_df = df.unique(subset=f"Avarage {colum}")
        return final_df.top_k(3, by=f"Avarage {colum}").select(['Oponent', f'Avarage {colum}', 'Color'])