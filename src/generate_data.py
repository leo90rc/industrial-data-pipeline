import os
import numpy as np
import pandas as pd


RAW_DATA_PATH = "data/raw"
N_SENSORS = 20
START_DATE = "2025-01-01 00:00:00"
END_DATE = "2025-12-31 23:00:00"


def create_sensors() -> pd.DataFrame:
    production_units = [
        "Reactor A",
        "Reactor B",
        "Distillation Unit",
        "Heat Exchanger",
        "Storage Area",
    ]

    sensor_config = {
        "temperature": {"prefix": "TEMP", "min": 60, "max": 90},
        "pressure": {"prefix": "PRESS", "min": 2, "max": 8},
        "flow_rate": {"prefix": "FLOW", "min": 100, "max": 250},
        "energy_consumption": {"prefix": "ENERGY", "min": 20, "max": 80},
    }

    sensors = []
    sensor_id = 1

    for variable_type, config in sensor_config.items():
        for i in range(5):
            sensors.append(
                {
                    "sensor_id": sensor_id,
                    "sensor_name": f"{config['prefix']}_{sensor_id:03d}",
                    "production_unit": production_units[i % len(production_units)],
                    "variable_type": variable_type,
                    "min_limit": config["min"],
                    "max_limit": config["max"],
                }
            )
            sensor_id += 1

    return pd.DataFrame(sensors)


def generate_measurements(sensors: pd.DataFrame) -> pd.DataFrame:
    timestamps = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq="h",
    )

    records = []

    for _, sensor in sensors.iterrows():
        min_limit = sensor["min_limit"]
        max_limit = sensor["max_limit"]
        normal_mean = (min_limit + max_limit) / 2
        normal_std = (max_limit - min_limit) / 8

        values = np.random.normal(
            loc=normal_mean,
            scale=normal_std,
            size=len(timestamps),
        )

        anomaly_mask = np.random.random(size=len(timestamps)) < 0.03
        anomaly_direction = np.random.choice([-1, 1], size=len(timestamps))

        values[anomaly_mask] = np.where(
            anomaly_direction[anomaly_mask] > 0,
            max_limit * np.random.uniform(1.01, 1.20, size=anomaly_mask.sum()),
            min_limit * np.random.uniform(0.80, 0.99, size=anomaly_mask.sum()),
        )

        sensor_records = pd.DataFrame(
            {
                "sensor_id": sensor["sensor_id"],
                "timestamp": timestamps,
                "value": values.round(2),
            }
        )

        records.append(sensor_records)

    return pd.concat(records, ignore_index=True)


def main() -> None:
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    sensors = create_sensors()
    measurements = generate_measurements(sensors)

    sensors.to_csv(f"{RAW_DATA_PATH}/sensors.csv", index=False)
    measurements.to_csv(f"{RAW_DATA_PATH}/measurements.csv", index=False)

    print("Raw data generated successfully.")
    print(f"Sensors: {len(sensors)}")
    print(f"Measurements: {len(measurements)}")


if __name__ == "__main__":
    main()