import pyodbc
import pandas as pd
from twitter_transform import run_twitter_transform

server = 'fastserver.database.windows.net'
database = 'fast_database'
username = 'serveradminlogin'
password = '{Rangga12!}'
driver = '{ODBC Driver 17 for SQL Server}'


def run_twitter_load():
    cleaned = pd.read_json(run_twitter_transform())
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:' +
                        server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            # Query to be executed
            for i in range(cleaned.shape[0]):
                cursor.execute("INSERT INTO [dbo].[tabletext](text) VALUES ('{0}')".format(
                    cleaned.iloc[i]['text']))


run_twitter_load()
