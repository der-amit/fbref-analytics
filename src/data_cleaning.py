import pandas as pd

def clean_table(file_path, new_columns, output_path = None):
    df = pd.read_csv(file_path)
    df = df.drop(df.columns[0], axis = 1)
    df = df.iloc[1:].reset_index(drop = True)
    
    if len(df.columns) == len(new_columns):
        df.columns = new_columns
    else:
        print(f"Column mismatch! Table has {len(df.columns)} but {len(new_columns)} names were provided")
        
    if output_path:
        df.to_csv(output_path, index = False)
        print(f"Cleaned data saved to {output_path}")
        
    return df

#Define new columns
    
def_cols = ['Squad', 'Players_used', '90s', 'Tkl_attempted', 'TklW', 'Tkl_Def', 'Tkl_Mid', 'Tkl_Att',
           'Drib_Tkl', 'Drib_chal', 'Drib_Tkl%', 'Chal_Lost', 'Blocks', 'Shots_blocked', 
           'Pass_blocked', 'Interceptions', 'Tkl+Int', 'Clr', 'Err_shot']

gca_cols = ["Squad", "Players_used", "90s", "SCA", "SCA90", "SCA_Passlive", "SCA_PassDead", 
           "SCA_TO", "SCA_Sh", "SCA_Fld", "SCA_Def", "GCA", "GCA90", "GCA_PassLive", 
           "GCA_PassDead", "GCA_TO", "GCA_Sh", "GCA_Fld", "GCA_Def"]

shooting_col = ['Squad','Players_used','90s','Goals','Shots',
                'SoT','SoT%','Sh/90','SoT/90',	'G/Sh',	'G/SoT', 
                'Shot_Dist','Shot_FK','PK_made','PKatt',
                'xG','npxG','npxG/Sh','Goals-xG', 'np:Goals-xG']

standard_col = ['Squad', 'Players_used','Age',	'Poss',	'Matches',	'Starts',	
                'Min',	'90s',	'Goals','Assists', 'G+A', 'G-PK', 'PK', 'PKatt', 'CrdY', 'CrdR', 
                'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC', 'PrgP', 'Goals_90', 
                'Assists_90', 'G+A_90', 'G-PK_90', 'G+A-PK_90', 
                'xG_90', 'xAG_90', 'xG+xAG_90', 'npxG_90', 'npxG+xAG_90']



mls_defense_25 = clean_table('data/mls2025_stats_squads_defense_for.csv', def_cols, 'data/mls2025_defense_cleaned.csv')

mls_gca_25 = clean_table('data/mls2025_stats_squads_gca_for.csv', gca_cols,'data/mls2025_gca_cleaned.csv')

mls_shooting_25 = clean_table('data/mls2025_stats_squads_shooting_for.csv',shooting_col, 'data/mls2025_shooting_cleaned.csv')

mls_standard_25 = clean_table('data/mls2025_stats_squads_standard_for.csv', standard_col, 'data/mls2025_standard_cleaned.csv')