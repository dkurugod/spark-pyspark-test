import pytest
from spark_pyspark_test.transformations import transform_data

@pytest.mark.spark
def test_transform_data(customers_df, orders_df):
    result = transform_data(customers_df, orders_df)

    data = {row["city"]: row["total_amount"] for row in result.collect()}

    assert data["Toronto"] == 500
    assert data["Mississauga"] == 700
    assert "Brampton" not in data
