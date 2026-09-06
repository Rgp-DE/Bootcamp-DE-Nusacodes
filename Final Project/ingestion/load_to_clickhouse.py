import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text


DATA_DIR = Path(
    os.getenv(
        "DATA_DIR",
        "/opt/airflow/project/data"
    )
)

CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "clickhouse")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_NATIVE_PORT", "9000")
CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER", "default")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "")
CLICKHOUSE_DATABASE = os.getenv("CLICKHOUSE_DATABASE", "default")


CSV_FILES = [
    "customers_dataset.csv",
    "geolocation_dataset.csv",
    "order_items_dataset.csv",
    "order_payments_dataset.csv",
    "order_reviews_dataset.csv",
    "orders_dataset.csv",
    "product_category_name_translation.csv",
    "products_dataset.csv",
    "sellers_dataset.csv",
]


def get_engine():
    connection_url = (
        f"clickhouse+native://"
        f"{CLICKHOUSE_USER}:{CLICKHOUSE_PASSWORD}"
        f"@{CLICKHOUSE_HOST}:{CLICKHOUSE_PORT}/"
        f"{CLICKHOUSE_DATABASE}"
    )

    return create_engine(connection_url)


def load_all_csv_to_clickhouse():
    print("Starting Olist ingestion pipeline...")

    engine = get_engine()

    for filename in CSV_FILES:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        print("=" * 60)
        print(f"Extracting {filename}")

        df = pd.read_csv(file_path)

        # Normalize column names
        df.columns = [
            col.lower().strip()
            for col in df.columns
        ]

        table_name = filename.replace(".csv", "")

        columns_db = []

        for column_name in df.columns:
            dtype = str(df[column_name].dtype)

            if "int" in dtype:
                df[column_name] = (
                    df[column_name]
                    .fillna(0)
                    .astype("int64")
                )
                columns_db.append(
                    f"`{column_name}` Int64"
                )

            elif "float" in dtype:
                df[column_name] = (
                    df[column_name]
                    .fillna(0.0)
                    .astype("float64")
                )
                columns_db.append(
                    f"`{column_name}` Float64"
                )

            else:
                df[column_name] = (
                    df[column_name]
                    .fillna("")
                    .astype(str)
                )
                columns_db.append(
                    f"`{column_name}` String"
                )

        create_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {", ".join(columns_db)}
        )
        ENGINE = MergeTree()
        ORDER BY tuple()
        """

        with engine.begin() as connection:
            connection.execute(
                text(
                    f"DROP TABLE IF EXISTS {table_name}"
                )
            )

            connection.execute(text(create_query))

        print(
            f"Loading {len(df):,} rows "
            f"into {table_name}"
        )

        df.to_sql(
            table_name,
            con=engine,
            if_exists="append",
            index=False,
        )

        print(f"Successfully loaded {table_name}")

    print("=" * 60)
    print("Olist ingestion completed.")


if __name__ == "__main__":
    load_all_csv_to_clickhouse()