import pandas as pd
import logging
from pymysql import connect
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Setup Logging
logging.basicConfig(
    filename="etl_validation.log",  # Log file name
    level=logging.INFO,             # Log level: INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S"  # Date format
)

logging.info("🚀 ETL Testing Script Started")

# Database Connection
try:
    conn = connect(
        host="localhost",
        user="root",
        password="Adhi@8722",
        database="adharshdb"
    )
    logging.info("✅ Connected to MySQL Database!")
except Exception as e:
    logging.error(f"❌ Connection failed: {e}")
    exit()  # Stop execution if connection fails

def total_sales_per_state_table_Validation():
    try:
        logging.info("📥 Reading source data from 'sales.csv'")
        src = pd.read_csv("sales.csv")
        
        query = "SELECT * FROM total_sales_per_state"
        logging.info("📤 Fetching target data from MySQL")

        tgt = pd.read_sql(query, conn)

        # Compute Total Sales
        src["Total_sales"] = src["Quantity"] * src["Price"]
        trns_src = src.groupby("Country")["Total_sales"].sum().reset_index()

        logging.info("🔄 Comparing transformed source data with target data")

        # Validate ETL process
        assert trns_src.equals(tgt), "❌ ETL Transformation process is not correctly performed"
        
        logging.info("✅ ETL Transformation on 'total_sales_per_state' table **PASSED**")
        print("✅ ELT Transformation on 'total_sales_per_state' table PASSED")

    except AssertionError as ae:
        logging.error(f"❌ Assertion Error: {ae}")
        print("❌ ETL Transformation validation **FAILED**:", ae)
    except Exception as e:
        logging.error(f"❌ Error occurred: {e}")
        print("❌ An unexpected error occurred:", e)

# Run validation
total_sales_per_state_table_Validation()

logging.info("🚀 ETL Testing Script Completed")
