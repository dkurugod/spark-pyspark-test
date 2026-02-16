from pyspark.sql import DataFrame
from pyspark.sql.functions import col, sum as _sum

def transform_data(customers: DataFrame, orders: DataFrame) -> DataFrame:
    """
    - Filter orders > 300
    - Join with customers
    - Aggregate total amount per city
    """
    filtered_orders = orders.filter(col("amount") > 300)

    joined_df = filtered_orders.join(
        customers,
        on="customer_id",
        how="inner"
    )

    result_df = (
        joined_df
        .groupBy("city")
        .agg(_sum("amount").alias("total_amount"))
    )

    return result_df
