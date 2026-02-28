import pandas as pd
from sqlalchemy import create_engine, text

# Basic DB settings (local MySQL running in Docker)
USER = "root"
PASSWORD = "rishit123"
HOST = "localhost"
PORT = 3306
DATABASE = "demand_db"

engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

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


def create_processed_table():
    print("Resetting processed_sales table...")

    with engine.begin() as conn:   # auto-commit block
        conn.execute(text("DROP TABLE IF EXISTS processed_sales"))
        conn.execute(text(FEATURE_SQL))

    print("processed_sales table created.")


def fetch_training_data():
    print("Fetching data for model training...")

    query = """
    SELECT *
    FROM processed_sales
    WHERE lag_7 IS NOT NULL
    """

    df = pd.read_sql(query, engine)

    # Drop any remaining NaNs just to be safe
    df = df.dropna()

    print(f"Final dataset shape: {df.shape}")
    return df


if __name__ == "__main__":
    try:
        create_processed_table()
        df = fetch_training_data()

        output_file = "engineered_data.csv"
        df.to_csv(output_file, index=False)

        print(f"Saved training data to {output_file}")

    except Exception as e:
        print("Something failed:")
        print(e)