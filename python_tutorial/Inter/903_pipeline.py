import pandas as pd
from sqlalchemy import (
    create_engine,
    inspect,
    text,
    select,
    MetaData,
    Table,
)

from utils import (
    clean_903_table,
    group_calculation,
    calculate_age_buckets,
    time_difference,
    multiples_same_event,group_calculation_year,appears_on_both
)

from datetime import datetime

from dateutil.relativedelta import relativedelta

#from utils import multiples_same_event, group_calculation_year, appears_on_both

filepath = (
    "/workspaces/python-learning-repo/python_tutorial/Intermediate/Data/903_database.db"
)

collection_year = 2014

collection_end = datetime(collection_year, 3, 31)


# read the data from SQL db
engine_903 = create_engine(f"sqlite:///{filepath}")

connection = engine_903.connect()

insection = inspect(engine_903)

# get the table names
table_names = insection.get_table_names()

# uncomment to check database connection
# print(table_names)


metadata_903 = MetaData()

dfs = {}
for table in table_names:
    current_table = Table(table, metadata_903, autoload_with=engine_903)
    with engine_903.connect() as con:
        stmt = select(current_table)
        result = con.execute(stmt).fetchall()
    dfs[table] = pd.DataFrame(result)

# uncomment to check the dataframes
# print(dfs.keys())
# print(dfs.values())

# clean all tables in 903

# for key, df in dfs.items():
# dfs[key] = clean_903_table(df)
for key in dfs.keys():
    dfs[key] = clean_903_table(dfs[key], collection_end)

# Ucomment to check the cleaned dataframes
# print(dfs['header'])


grouped = dfs["header"].groupby("ETHNICITY").count()

grouped = dfs["header"].groupby("ETHNICITY").size()

# grouped =grouped.to_frame(name='count').reset_index()
# grouped =grouped.to_frame('count')

# grouped =grouped.to_frame('count').reset_index()

# grouped =grouped.to_frame('Header - Ethnicities- count').reset_index()

# grouped = grouped.rename(columns={'ETHNICITY': 'Ethnicity'})

# grouped =grouped.to_frame(name='count').reset_index()

# print(grouped)


# def group_calcuation(df,colunm):
# grouped = dfs['header'].groupby('ETHNICITY').size()
# grouped = grouped.to_frame('Header - Ethncities - Count').reset_index()
# grouped = grouped.rename(columns={'ETHNICITY':'Ethnicity'})

# grouped['Header - Ethnicities - Percentage'] = (grouped['Header - Ethncities - Count'] /
# grouped['Header - Ethncities - Count'].sum()) * 100

# print(grouped['H'])


# def group_calculation(df, column, measure_name):
# grouped = df.groupby(column).size()
#   grouped = grouped.to_frame(f'{measure_name} - Count').reset_index()
#  grouped = grouped.rename(columns={column:'Ethnicity'})

#  grouped[f'{measure_name} - Percentage'] = (grouped[f'{measure_name} - Count'] /
#                                                grouped[f'{measure_name} - Count'].sum()) * 100
# return grouped

output = group_calculation(dfs["header"], "ETHNICITY", "Header - Ethncities")

print(output)


# def group_calculation(df, column, measure_name):
#     '''
#     A function to group as df by input column, outputs with count
#    and percentage to a dataframe with renamed columns.
#    '''
#     grouped = df.groupby(column).size()
#     grouped = grouped.to_frame(f'{measure_name} - Count').reset_index()
#    grouped = grouped.rename(columns={column:'Value'})

#    grouped[f'{measure_name} - Percentage'] = (grouped[f'{measure_name} - Count'] /
#                                                    grouped[f'{measure_name} - Count'].sum()) * 100

#    return grouped

output = group_calculation(dfs["header"], "ETHNICITY", "Header - Ethncities")

print(output)

measures = {}

measures["Header by ethnicity"] = group_calculation(
    dfs["header"], "ETHNICITY", "Header - Ethncities"
)

measures["Header by age"] = group_calculation(dfs["header"], "AGE", "Header - Ages")

dfs["missing"]["MISSING_DURATION"] = dfs["missing"].apply(
    lambda x: relativedelta(x["MIS_END_dt"], x["MIS_START_dt"]).normalized().days,
    axis=1,
)

dfs["missing"]

print(dfs["missing"])



output = multiples_same_event(dfs['episodes'], col_name='Number of Episodes')
 
print(output)


measures['Multiple  episodes'] = multiples_same_event(dfs['episodes'], col_name='Number of Episodes')

dfs['episodes']["DECOM_YEAR"] = dfs['episodes']['DECOM_dt'].dt.year

measures['Episodes starting per year'] = group_calculation(dfs['episodes'], "DECOM_YEAR", "Measures starting per year")

output = group_calculation_year(dfs['episodes'], "DECOM_YEAR", "Measures starting per year")

measures['Episodes starting per year'] = group_calculation_year(dfs['episodes'], "DECOM_YEAR", "Measures starting per year")

print(output)

# output = appears_on_both(dfs['episodes'], dfs['missing'], 'CYP with episode and missing event')

# print(output)

output = appears_on_both(dfs['episodes'], dfs['missing'], "CYP with episodes who have been missing")
print(output)