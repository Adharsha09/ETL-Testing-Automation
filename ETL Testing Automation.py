import pandas as pd
from pymysql import connect
import warnings
warnings.filterwarnings("ignore")
try:
    conn = connect(
        host = "localhost",
        user = 'root',
        password='Adhi@8722',
        database='adharshdb'
    )
    print("Connected to MySQL Database!")
except Exception as e:
    print("Connection failed:", e)
def total_sales_per_state_table_Validation():
    src = pd.read_csv("sales.csv")
    query = ("select * from total_sales_per_state")
    tgt = pd.read_sql(query,conn)
    src["Total_sales"] = src["Quantity"]*src["Price"]
    trns_src = src.groupby("Country")["Total_sales"].sum().reset_index()
    assert trns_src.equals(tgt),"ETL Transformation process is not correctly performed"
    print("ELT Transformation on total_sales_per_state table is passed")

total_sales_per_state_table_Validation()