import pytest
from spark_pyspark_test.spark_session import get_spark

@pytest.fixture(scope="session")
def spark():
    spark = get_spark("pytest-session")
    yield spark
    spark.stop()

@pytest.fixture
def customers_df(spark):
    return spark.read.csv(
        "data/customers.csv",
        header=True,
        inferSchema=True
    )

@pytest.fixture
def orders_df(spark):
    return spark.read.csv(
        "data/orders.csv",
        header=True,
        inferSchema=True
    )
