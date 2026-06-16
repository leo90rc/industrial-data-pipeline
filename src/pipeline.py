from pathlib import Path

from extract import extract_raw_data
from transform import transform_data
from load import load_to_postgresql


PROCESSED_DATA_PATH = Path("data/processed")


def save_processed_data(
    sensors_clean,
    measurements_clean,
    alerts,
) -> None:
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    sensors_clean.to_csv(PROCESSED_DATA_PATH / "sensors_clean.csv", index=False)
    measurements_clean.to_csv(
        PROCESSED_DATA_PATH / "measurements_clean.csv",
        index=False,
    )
    alerts.to_csv(PROCESSED_DATA_PATH / "alerts.csv", index=False)


def run_pipeline() -> None:
    sensors, measurements = extract_raw_data()

    sensors_clean, measurements_clean, alerts = transform_data(
        sensors,
        measurements,
    )

    save_processed_data(
        sensors_clean,
        measurements_clean,
        alerts,
    )

    load_to_postgresql(
        sensors_clean,
        measurements_clean,
        alerts,
    )

    print("Pipeline executed successfully.")
    print(f"Sensors processed: {len(sensors_clean)}")
    print(f"Measurements processed: {len(measurements_clean)}")
    print(f"Alerts generated: {len(alerts)}")


if __name__ == "__main__":
    run_pipeline()