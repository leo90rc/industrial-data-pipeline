import pandas as pd


def validate_columns(
    dataframe: pd.DataFrame,
    required_columns: list[str],
    dataframe_name: str,
) -> None:
    missing_columns = [
        column for column in required_columns if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"{dataframe_name} is missing required columns: {missing_columns}"
        )


def clean_sensors(sensors: pd.DataFrame) -> pd.DataFrame:
    required_columns = [
        "sensor_id",
        "sensor_name",
        "production_unit",
        "variable_type",
        "engineering_unit",
        "min_limit",
        "max_limit",
    ]

    validate_columns(sensors, required_columns, "sensors")

    sensors = sensors.copy()
    sensors = sensors.drop_duplicates(subset=["sensor_id"])

    sensors["sensor_id"] = sensors["sensor_id"].astype(int)
    sensors["min_limit"] = sensors["min_limit"].astype(float)
    sensors["max_limit"] = sensors["max_limit"].astype(float)

    return sensors


def clean_measurements(measurements: pd.DataFrame) -> pd.DataFrame:
    required_columns = [
        "sensor_id",
        "timestamp",
        "value",
    ]

    validate_columns(measurements, required_columns, "measurements")

    measurements = measurements.copy()
    measurements = measurements.drop_duplicates(subset=["sensor_id", "timestamp"])

    measurements["sensor_id"] = measurements["sensor_id"].astype(int)
    measurements["timestamp"] = pd.to_datetime(measurements["timestamp"])
    measurements["value"] = measurements["value"].astype(float)

    measurements = measurements.sort_values(["sensor_id", "timestamp"])
    measurements = measurements.reset_index(drop=True)
    measurements["measurement_id"] = measurements.index + 1

    return measurements[
        [
            "measurement_id",
            "sensor_id",
            "timestamp",
            "value",
        ]
    ]


def generate_alerts(
    measurements: pd.DataFrame,
    sensors: pd.DataFrame,
) -> pd.DataFrame:
    measurements_with_limits = measurements.merge(
        sensors[
            [
                "sensor_id",
                "variable_type",
                "min_limit",
                "max_limit",
            ]
        ],
        on="sensor_id",
        how="left",
    )

    alerts = measurements_with_limits[
        (measurements_with_limits["value"] < measurements_with_limits["min_limit"])
        | (measurements_with_limits["value"] > measurements_with_limits["max_limit"])
    ].copy()

    alerts["alert_type"] = alerts.apply(
        lambda row: (
            f"LOW_{row['variable_type'].upper()}"
            if row["value"] < row["min_limit"]
            else f"HIGH_{row['variable_type'].upper()}"
        ),
        axis=1,
    )

    alerts["severity"] = alerts.apply(
        lambda row: classify_severity(
            value=row["value"],
            min_limit=row["min_limit"],
            max_limit=row["max_limit"],
        ),
        axis=1,
    )

    alerts["created_at"] = alerts["timestamp"]

    alerts = alerts.reset_index(drop=True)
    alerts["alert_id"] = alerts.index + 1

    return alerts[
        [
            "alert_id",
            "measurement_id",
            "alert_type",
            "severity",
            "created_at",
        ]
    ]


def classify_severity(
    value: float,
    min_limit: float,
    max_limit: float,
) -> str:
    operating_range = max_limit - min_limit

    if value > max_limit:
        deviation_ratio = (value - max_limit) / operating_range
    else:
        deviation_ratio = (min_limit - value) / operating_range

    if deviation_ratio >= 0.10:
        return "HIGH"

    return "MEDIUM"


def transform_data(
    sensors: pd.DataFrame,
    measurements: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    sensors_clean = clean_sensors(sensors)
    measurements_clean = clean_measurements(measurements)
    alerts = generate_alerts(measurements_clean, sensors_clean)

    return sensors_clean, measurements_clean, alerts