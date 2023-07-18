#%%We send data into the SQL server
#We import it from my desktop
data = pd.read_excel ('C:\\Users\\adfig\\Desktop\\MoltenSalt.xlsx')
df = pd.DataFrame(data)
print(df)
#We send it to the SQLServer
df.to_sql('MoltenSalt', con = myeng)





12:48
Replace Molten Salt with any excel that you have


Shan Akiraj
  12:49 PM
okay great the first portion of the code worked I was able to fetch the file and print it out locally


Shan Akiraj
  1:01 PM
cool everything is working perfectly
1:01
I was able to fetch and send to the server


Roberto Herrera del Valle
  9:06 PM
Pardon the delay, I am currently travelling
9:06
Awesome, is there any way that you could improve the code, with good practices or advice?


Shan Akiraj
  9:07 PM
For sure, I think it would be good to implement some exception handling.
9:09
also I can organize the code into methods to make it more modular


Roberto Herrera del Valle
  9:23 PM
Got it! We can work on that to optimize it before handing it to Ryan


Roberto Herrera del Valle
  11:15 AM
Hey Shan, let me know when you want to work on making it more modular. I can start today too and make it modular.


Shan Akiraj
  11:25 AM
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
