# -*- coding: utf-8 -*-
"""
SQL Integration Function
Roberto J. Herrera y del Valle
"""
#%% Function for calling specific databases from our AWS SQL server
def SQLCall(x):
    import pyodbc
    import pandas as pd
    if type(x)!= str :
        return "Incorrect Input"
    else :
        db = ("Driver={SQL Server};"
              "Server=******;"
              "Database=*****;"
              "uid=****;pwd=*****;"
              "port = 1433;")
        cnxn = pyodbc.connect(db)
        df = pd.read_sql("SELECT * FROM " + x, cnxn)
        return df

x=SQLCall("AM_BismuthTelluride_Data")

#%% Function for calling importinh databases from our AWS SQL server
def SQLSend(df,name):
    import sqlalchemy
    db = ("Driver={SQL Server};"
          "Server=******;"
          "Database=******;"
          "uid=******;pwd=******;"
          "port = 1433;")
    myeng = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % db)
    df.to_sql(str(name), con = myeng)   
       
SQLSend(data, "MoltenSalt")
