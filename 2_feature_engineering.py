import pandas as pd
from sqlalchemy import create_engine, text

# --- DB config ---
USER = "root"
PASSWORD = "rishit123"
HOST = "localhost"
PORT = 3306
DATABASE = "demand_db"

engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# SQL for feature creation (lags + rolling average)
FEATURE_SQL = """
CREATE TABLE processed_sales AS
SELECT 
    `date`,
    store,
    item,
    sales,
    LAG(sales, 1) OVER (
        PARTITION BY store, item 
        ORDER BY `date`
    ) AS lag_1,
    LAG(sales, 7) OVER (
        PARTITION BY store, item 
        ORDER BY `date`
    ) AS lag_7,
    AVG(sales) OVER (
        PARTITION BY store, item
        ORDER BY `date`
        ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING
    ) AS rolling_avg_7d
FROM raw_sales;
"""

def create_features():
    """
    Creates lag and rolling features directly inside MySQL.
    """
    with engine.connect() as conn:
        print("Dropping old processed table (if any)...")
        conn.execute(text("DROP TABLE IF EXISTS processed_sales"))

        print("Running feature engineering query...")
        conn.execute(text(FEATURE_SQL))
        conn.commit()

    print("Feature table created successfully.")


def export_features(output_path="engineered_data.csv"):
    """
    Pulls processed data into pandas and saves it locally.
    """
    print("Loading processed data into pandas...")
    df = pd.read_sql(
        "SELECT * FROM processed_sales WHERE lag_7 IS NOT NULL",
        engine
    )

    print(f"Rows available for training: {len(df)}")

    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    try:
        create_features()
        export_features()
        print("Done.")
    except Exception as err:
        print("Error during processing:")
        print(err)