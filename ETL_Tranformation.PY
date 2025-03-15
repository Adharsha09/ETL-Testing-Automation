import pandas as pd
from pymysql import connect
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings("ignore")
engine = create_engine("mysql+pymysql://root:Adhi%408722@localhost/adharshdb")

src = pd.read_csv("sales.csv")
src["Total_sales"] = src["Quantity"]*src["Price"]
Total_sales_state = src.groupby("Country")['Total_sales'].sum().reset_index()
Total_sales_state.to_sql('total_sales_per_state',con =engine,if_exists='replace',index=False)
print("✅ Data successfully inserted into MySQL!")
