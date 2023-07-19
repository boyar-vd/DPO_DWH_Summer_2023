"""
Update table "DDS".merchants
"""

'''Import libs'''
# from sqlalchemy import text
import pandas as pd

'''Import connections and common functions'''
from dags.python_scripts.config import engine


def update():
    sql = f'''
    SELECT DISTINCT merchant
     FROM "RAW".test_table_sl
    '''

    select_df = pd.read_sql(sql=sql, con=engine)

    if not select_df.empty:
        # select_df.apply(lambda row: function(row), axis=1)

        select_df.to_sql(name='merchants_test'
                        ,con=engine
                        ,schema='DDS'
                        ,if_exists='replace'
                        ,index=True)
# update()
