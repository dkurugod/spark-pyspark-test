from src.spark_session import get_spark
from src.transformations import transform_data

def main():
    spark = get_spark("local-run")

    customers = spark.read.csv(
        "data/customers.csv",
        header=True,
        inferSchema=True
    )

    orders = spark.read.csv(
        "data/orders.csv",
        header=True,
        inferSchema=True
    )

    result = transform_data(customers, orders)

    result.show(truncate=False)

    spark.stop()

if __name__ == "__main__":
    main()
