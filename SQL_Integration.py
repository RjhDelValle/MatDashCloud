# -*- coding: utf-8 -*-
"""
SQL Calling file
Roberto J. Herrera y del Valle
"""
#%% We import our library for connecting Python to SQL
import pyodbc
import pandas as pd
import sqlalchemy
import pyodbc
#%%Local Driver Condition
cnxn_str = ("Driver={SQL Server};"
            "Server=DESKTOP-64QH8U8;"
            "Database=Thermo;"
            "Trusted_Connection=yes;")
#%% Actual connection
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
#%%We select some test data
cursor.execute("SELECT TOP(100) * FROM data")
cursor.close()
"We actually place it in our enviroment"
data = pd.read_sql("SELECT TOP(100) * FROM data WHERE ZT >0.5", cnxn)

#%%AWS SQL Server Calling

#%%We create our connection conditions
#These are the strings that can be used to authenticate access to the AWS RDS instance

db = ("Driver={SQL Server};"
      "Server=dash-database.cqg8xstfjlip.us-east-1.rds.amazonaws.com;"
      "Database=******;"
      "uid=*****;pwd=*****;"
      "port = 1433;"
                      )
#The engine is used to create an intermediary betweeb the python and SQL server for import
myeng = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % db)
#%%Actual Connection
#CNXN Activeates a connection with the SQL Server "Dash Database"
cnxn = pyodbc.connect(db)
#Creates a cursor on the SQL to perform specific action and queries within the SQL server
cursor = cnxn.cursor()

#%% We extract a specific data amount for testing
cursor.execute("SELECT TOP(10) * FROM AM_BismuthTelluride_Data")
cursor.close()
#We actually place it in our enviroment
data = pd.read_sql("SELECT TOP(100) * FROM AM_BismuthTelluride_Data WHERE Seebeck >85", cnxn)

#%%We send data into the SQL server
#We import it from my desktop
data = pd.read_excel ('C:\\Users\\adfig\\Desktop\\MoltenSalt.xlsx')   
df = pd.DataFrame(data)
print(df)

#We send it to the SQLServer
df.to_sql('MotelSalt', con = myeng)
