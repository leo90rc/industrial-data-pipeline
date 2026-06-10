from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw")

SENSORS_FILE = RAW_DATA_PATH / "sensors.csv"
MEASUREMENTS_FILE = RAW_DATA_PATH / "measurements.csv"


def extract_sensors() -> pd.DataFrame:
    return pd.read_csv(SENSORS_FILE)


def extract_measurements() -> pd.DataFrame:
    return pd.read_csv(MEASUREMENTS_FILE)


def extract_raw_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    sensors = extract_sensors()
    measurements = extract_measurements()

    return sensors, measurements


if __name__ == "__main__":
    sensors_df, measurements_df = extract_raw_data()

    print("Raw data extracted successfully.")
    print(f"Sensors: {len(sensors_df)}")
    print(f"Measurements: {len(measurements_df)}")