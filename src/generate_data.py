import os

import numpy as np
import pandas as pd


RAW_DATA_PATH = "data/raw"

START_DATE = "2025-01-01 00:00:00"
END_DATE = "2025-12-31 23:00:00"
ANOMALY_RATE = 0.03
RANDOM_SEED = 42


def create_sensors() -> pd.DataFrame:
    sensors = [
        # Reactor A
        {
            "sensor_id": 1,
            "sensor_name": "TEMP_REACTOR_A",
            "production_unit": "Reactor A",
            "variable_type": "temperature",
            "engineering_unit": "°C",
            "min_limit": 70,
            "max_limit": 95,
        },
        {
            "sensor_id": 2,
            "sensor_name": "PRESS_REACTOR_A",
            "production_unit": "Reactor A",
            "variable_type": "pressure",
            "engineering_unit": "bar",
            "min_limit": 3,
            "max_limit": 7,
        },
        {
            "sensor_id": 3,
            "sensor_name": "FLOW_FEED_REACTOR_A",
            "production_unit": "Reactor A",
            "variable_type": "flow_rate",
            "engineering_unit": "m3/h",
            "min_limit": 45,
            "max_limit": 75,
        },
        {
            "sensor_id": 4,
            "sensor_name": "ENERGY_AGITATOR_REACTOR_A",
            "production_unit": "Reactor A",
            "variable_type": "energy_consumption",
            "engineering_unit": "kWh",
            "min_limit": 25,
            "max_limit": 55,
        },

        # Reactor B
        {
            "sensor_id": 5,
            "sensor_name": "TEMP_REACTOR_B",
            "production_unit": "Reactor B",
            "variable_type": "temperature",
            "engineering_unit": "°C",
            "min_limit": 75,
            "max_limit": 105,
        },
        {
            "sensor_id": 6,
            "sensor_name": "PRESS_REACTOR_B",
            "production_unit": "Reactor B",
            "variable_type": "pressure",
            "engineering_unit": "bar",
            "min_limit": 4,
            "max_limit": 9,
        },
        {
            "sensor_id": 7,
            "sensor_name": "FLOW_FEED_REACTOR_B",
            "production_unit": "Reactor B",
            "variable_type": "flow_rate",
            "engineering_unit": "m3/h",
            "min_limit": 40,
            "max_limit": 70,
        },
        {
            "sensor_id": 8,
            "sensor_name": "ENERGY_AGITATOR_REACTOR_B",
            "production_unit": "Reactor B",
            "variable_type": "energy_consumption",
            "engineering_unit": "kWh",
            "min_limit": 30,
            "max_limit": 65,
        },

        # Steam inlet to condenser
        {
            "sensor_id": 9,
            "sensor_name": "TEMP_STEAM_CONDENSER_IN",
            "production_unit": "Entrada de vapor al condensador",
            "variable_type": "temperature",
            "engineering_unit": "°C",
            "min_limit": 120,
            "max_limit": 160,
        },
        {
            "sensor_id": 10,
            "sensor_name": "PRESS_STEAM_CONDENSER_IN",
            "production_unit": "Entrada de vapor al condensador",
            "variable_type": "pressure",
            "engineering_unit": "bar",
            "min_limit": 1.5,
            "max_limit": 4.0,
        },
        {
            "sensor_id": 11,
            "sensor_name": "FLOW_STEAM_CONDENSER_IN",
            "production_unit": "Entrada de vapor al condensador",
            "variable_type": "flow_rate",
            "engineering_unit": "m3/h",
            "min_limit": 80,
            "max_limit": 140,
        },

        # Condensate outlet from condenser
        {
            "sensor_id": 12,
            "sensor_name": "TEMP_CONDENSATE_CONDENSER_OUT",
            "production_unit": "Salida de condensado del condensador",
            "variable_type": "temperature",
            "engineering_unit": "°C",
            "min_limit": 45,
            "max_limit": 85,
        },
        {
            "sensor_id": 13,
            "sensor_name": "PRESS_CONDENSATE_CONDENSER_OUT",
            "production_unit": "Salida de condensado del condensador",
            "variable_type": "pressure",
            "engineering_unit": "bar",
            "min_limit": 1.0,
            "max_limit": 3.5,
        },
        {
            "sensor_id": 14,
            "sensor_name": "FLOW_CONDENSATE_CONDENSER_OUT",
            "production_unit": "Salida de condensado del condensador",
            "variable_type": "flow_rate",
            "engineering_unit": "m3/h",
            "min_limit": 75,
            "max_limit": 135,
        },

        # Heat exchanger inlet
        {
            "sensor_id": 15,
            "sensor_name": "TEMP_HEAT_EXCHANGER_IN",
            "production_unit": "Entrada al intercambiador de calor",
            "variable_type": "temperature",
            "engineering_unit": "°C",
            "min_limit": 25,
            "max_limit": 45,
        },
        {
            "sensor_id": 16,
            "sensor_name": "PRESS_HEAT_EXCHANGER_IN",
            "production_unit": "Entrada al intercambiador de calor",
            "variable_type": "pressure",
            "engineering_unit": "bar",
            "min_limit": 2.0,
            "max_limit": 5.0,
        },
        {
            "sensor_id": 17,
            "sensor_name": "FLOW_HEAT_EXCHANGER_IN",
            "production_unit": "Entrada al intercambiador de calor",
            "variable_type": "flow_rate",
            "engineering_unit": "m3/h",
            "min_limit": 60,
            "max_limit": 110,
        },

        # Heat exchanger outlet
        {
            "sensor_id": 18,
            "sensor_name": "TEMP_HEAT_EXCHANGER_OUT",
            "production_unit": "Salida del intercambiador de calor",
            "variable_type": "temperature",
            "engineering_unit": "°C",
            "min_limit": 65,
            "max_limit": 95,
        },
        {
            "sensor_id": 19,
            "sensor_name": "PRESS_HEAT_EXCHANGER_OUT",
            "production_unit": "Salida del intercambiador de calor",
            "variable_type": "pressure",
            "engineering_unit": "bar",
            "min_limit": 1.5,
            "max_limit": 4.5,
        },
        {
            "sensor_id": 20,
            "sensor_name": "FLOW_HEAT_EXCHANGER_OUT",
            "production_unit": "Salida del intercambiador de calor",
            "variable_type": "flow_rate",
            "engineering_unit": "m3/h",
            "min_limit": 58,
            "max_limit": 108,
        },
    ]

    return pd.DataFrame(sensors)


def generate_measurements(
    sensors: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    timestamps = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq="h",
    )

    measurement_records = []

    for _, sensor in sensors.iterrows():
        min_limit = sensor["min_limit"]
        max_limit = sensor["max_limit"]

        mean_value = (min_limit + max_limit) / 2
        standard_deviation = (max_limit - min_limit) / 8

        values = rng.normal(
            loc=mean_value,
            scale=standard_deviation,
            size=len(timestamps),
        )

        anomaly_mask = rng.random(size=len(timestamps)) < ANOMALY_RATE
        anomaly_direction = rng.choice([-1, 1], size=len(timestamps))

        values[anomaly_mask] = np.where(
            anomaly_direction[anomaly_mask] > 0,
            max_limit * rng.uniform(1.01, 1.20, size=anomaly_mask.sum()),
            min_limit * rng.uniform(0.80, 0.99, size=anomaly_mask.sum()),
        )

        sensor_measurements = pd.DataFrame(
            {
                "sensor_id": sensor["sensor_id"],
                "timestamp": timestamps,
                "value": values.round(2),
            }
        )

        measurement_records.append(sensor_measurements)

    return pd.concat(measurement_records, ignore_index=True)


def main() -> None:
    rng = np.random.default_rng(seed=RANDOM_SEED)

    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    sensors = create_sensors()
    measurements = generate_measurements(sensors, rng)

    sensors.to_csv(f"{RAW_DATA_PATH}/sensors.csv", index=False)
    measurements.to_csv(f"{RAW_DATA_PATH}/measurements.csv", index=False)

    print("Raw data generated successfully.")
    print(f"Sensors: {len(sensors)}")
    print(f"Measurements: {len(measurements)}")


if __name__ == "__main__":
    main()