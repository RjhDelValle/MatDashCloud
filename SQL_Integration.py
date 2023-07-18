import pyodbc
import pandas as pd
import numpy as np
import sqlalchemy
def create_connection():
    db = ("Driver={ODBC Driver 17 for SQL Server};"
          "Server=dash-database-cloud.cqg8xstfjlip.us-east-1.rds.amazonaws.com;"
          "Database=MatDashTest;"
          "uid=****;pwd=***;"
          "port=1433;"
          "timeout=30;")
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % db)
    connection = pyodbc.connect(db)
    return connection, engine
def fetch_data(connection):
    query = "SELECT TOP(100) * FROM AM_LPBF_Seebeck_Bismuth_Telluride_06_09_2023 WHERE Seebeck >85"
    data = pd.read_sql(query, connection)
    return data
def create_random_data():
    df = pd.DataFrame(np.random.rand(100, 5), columns=list('ABCDE'))
    df.to_csv('random.csv', index=False)
    return df
def import_to_database(df, engine):
    #this will overwrite the file if it exists change to to_sql for different behaviour
    df.to_sql('random_data', con=engine, if_exists='replace')
def main():
    try:
        connection, engine = create_connection()
        data = fetch_data(connection)
        print(data)
        df = create_random_data()
        import_to_database(df, engine)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.close()
if _name_ == "_main_":
    main()
df = pd.DataFrame(data)
print(df)

#We send it to the SQLServer
df.to_sql('MoltenSalt', con = myeng)
