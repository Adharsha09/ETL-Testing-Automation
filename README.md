 # ETL Testing Automation

## 📌 Project Overview
This project automates the ETL (Extract, Transform, Load) testing process to verify that data is correctly transformed and loaded into the target database. It reads a CSV file, calculates total sales per state, and validates the transformation against the MySQL database.

## 📂 Directory Structure
```
ETL_Tester_Files/
│-- etl_tester.py              # Main ETL Testing script
│-- sales.csv                  # Source data file
│-- etl_validation.log         # Log file (auto-generated)
│-- README.md                  # Project documentation
```

## 🔧 Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Database
- Required Python libraries

## 📥 Installation
1. Clone this repository or download the files.
2. Install dependencies:
   ```sh
   pip install pandas pymysql sqlalchemy
   ```
3. Configure MySQL with a database named `adharshdb`.
4. Update MySQL credentials in `ETL_Testing_with_logs.py`.

## 🚀 Running the ETL Test
Execute the script using:
```sh
python ETL_Testing_with_logs.py
```

## 📝 Logging
All logs are saved in `etl_validation.log`. The logs track:
- Database connection status
- Data extraction from `sales.csv`
- Data loading into MySQL
- Validation results

## 🛠 Troubleshooting
| Issue | Solution |
|--------|----------|
| `Connection failed` | Check MySQL is running and credentials are correct |
| `ETL Transformation process is not correctly performed` | Verify transformations in `sales.csv` and MySQL |
| `Permission Denied` | Run the script as an administrator |

## 📬 Support
For issues or suggestions, feel free to reach out!

---

✅ **ETL Testing Completed Successfully** 🚀


