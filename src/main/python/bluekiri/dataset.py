import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
from pyspark.sql.window import Window

class trips_dataset:
    spark = SparkSession\
        .builder\
        .appName("GenerateDataset")\
        .getOrCreate()

    trips = pd.DataFrame({
        "origin": [
            "PMI",
            "ATH",
            "JFK",
            "HND"
        ],
        "destination": [
            "OPO",
            "BCN",
            "MAD",
            "LAX"
        ],
        "internal_flight_ids": [
            [2, 1],
            [3],
            [5, 4, 6],
            [8, 9, 7, 0]
        ]
    })

    flights = pd.DataFrame({
        "internal_flight_id": [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        ],
        "public_flight_number": [
            "FR5763", "UT9586", "B4325", "RW35675", "LP656",
            "NB4321", "CX4599", "AZ8844", "KH8851", "OP8777"
        ]
    })

    trips = spark.createDataFrame(trips)
    flights = spark.createDataFrame(flights)


    trips.show
    spark.stop

if __name__ == '__main__':
    pass
