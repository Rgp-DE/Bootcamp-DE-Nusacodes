import os
from sqlalchemy import create_engine, text

host = os.getenv("CLICKHOUSE_HOST", "clickhouse")
port = os.getenv("CLICKHOUSE_NATIVE_PORT", "9000")
user = os.getenv("CLICKHOUSE_USER", "default")
password = os.getenv("CLICKHOUSE_PASSWORD", "")
database = os.getenv("CLICKHOUSE_DATABASE", "default")

engine = create_engine(
    f"clickhouse+native://{user}:{password}@{host}:{port}/{database}"
)

TABLES = [
    "customers_dataset",
    "orders_dataset",
    "silver_dim_customers",
    "silver_fact_orders",
    "gold_dim_customers",
    "gold_fct_orders",
]

def validate():
    with engine.connect() as connection:
        for table in TABLES:
            row_count = connection.execute(
                text(f"SELECT count(*) FROM {table}")
            ).scalar()

            print(f"{table}: {row_count:,} rows")

            if row_count == 0:
                raise ValueError(
                    f"Validation failed: {table} is empty"
                )

    print("All validation checks passed.")

if __name__ == "__main__":
    validate()
