import pandas as pd

def clean_903_table():
    print('Function works')

def clean_903_table(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Takes tables from the 903 as dataframes and outputs cleaned tables.
    '''  
    clean_df = df.copy()

    # TODO remove index

if 'index' in clean_df.columns:
        clean_df = clean_df.drop(columns=['index'])
    # TODO convert date columns

    # TODO make ethnic main group column

    # TODO make age column

    # TODO add age buckets column

    return clean_df