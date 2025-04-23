import pandas as pd

def player_data_clean(filepath, new_cols, outputpath = None):
    df = pd.read_csv(filepath)
    df = df.drop(df.columns[0], axis = 1)
    df = df.iloc[1:].reset_index(drop = True)
    
    if len(df.columns) == len(new_cols):
        df.columns = new_cols
    else:
        print(f"Existing columns are: {len(df.columns)} but you passed: {len(new_cols)}")
        
    if outputpath:
        df.to_csv(outputpath, index = False)
        print(f"Cleaned data saved to: {outputpath}")
        
    return df

gca_cols = ['Rk','Player','Nation','Pos','Squad','Age','Born','90s',
            'SCA','SCA90', 'SCA_PassLive','SCA_PassDead','SCA_TO','SCA_Shot','SCA_Fld','SCA_DefAct',
            'GCA', 'GCA90', 'GCA_PassLive','GCA_PassDead','GCA_TO','GCA_Shot','GCA_Fld','GCA_DefAct', 'Matches']

gca_playerdata_2025 = player_data_clean('data/player_gca_2025.csv', gca_cols, 'data/mls2025_player_gca_cleaned.csv')