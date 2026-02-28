import pandas as pd
from sqlalchemy import create_engine, text

# --- MySQL Config ---
USER = "root"
PASSWORD = "rishit123"
HOST = "localhost"
PORT = 3306
DATABASE = "demand_db"

def create_database():
    """
    Creates the database if it doesn't already exist.
    """
    engine = create_engine(
        f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}"
    )

    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE}"))
        print(f"[OK] Database '{DATABASE}' is ready.")

def upload_csv_to_mysql(csv_path):
    """
    Reads a CSV file and uploads it to MySQL.
    """
    print("Reading CSV file...")
    df = pd.read_csv(csv_path)

    print(f"Loaded {len(df)} rows.")

    engine = create_engine(
        f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )

    print("Uploading data to MySQL (table: raw_sales)...")
    df.to_sql("raw_sales", con=engine, if_exists="replace", index=False)

    print("Upload complete ✔")

if __name__ == "__main__":
    try:
        create_database()
        upload_csv_to_mysql("train.csv")
        print("All done.")

    except Exception as err:
        print("Something went wrong:")
        print(err)