import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


PROCESSED_DATA_PATH = "data/processed"


def get_database_engine():
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    required_variables = {
        "DB_HOST": db_host,
        "DB_PORT": db_port,
        "DB_NAME": db_name,
        "DB_USER": db_user,
        "DB_PASSWORD": db_password,
    }

    missing_variables = [
        name for name, value in required_variables.items() if value is None
    ]

    if missing_variables:
        raise ValueError(f"Missing environment variables: {missing_variables}")

    connection_string = (
        f"postgresql+psycopg2://{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    return create_engine(connection_string)


def load_processed_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    sensors = pd.read_csv(f"{PROCESSED_DATA_PATH}/sensors_clean.csv")
    measurements = pd.read_csv(f"{PROCESSED_DATA_PATH}/measurements_clean.csv")
    alerts = pd.read_csv(f"{PROCESSED_DATA_PATH}/alerts.csv")

    return sensors, measurements, alerts


def truncate_tables(engine) -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                TRUNCATE TABLE alerts, measurements, sensors
                RESTART IDENTITY
                CASCADE;
                """
            )
        )


def load_to_postgresql(
    sensors: pd.DataFrame,
    measurements: pd.DataFrame,
    alerts: pd.DataFrame,
) -> None:
    engine = get_database_engine()

    truncate_tables(engine)

    sensors.to_sql(
        "sensors",
        engine,
        if_exists="append",
        index=False,
    )

    measurements.to_sql(
        "measurements",
        engine,
        if_exists="append",
        index=False,
    )

    alerts.to_sql(
        "alerts",
        engine,
        if_exists="append",
        index=False,
    )


def main() -> None:
    sensors, measurements, alerts = load_processed_data()

    load_to_postgresql(
        sensors,
        measurements,
        alerts,
    )

    print("Data loaded successfully into PostgreSQL.")
    print(f"Sensors loaded: {len(sensors)}")
    print(f"Measurements loaded: {len(measurements)}")
    print(f"Alerts loaded: {len(alerts)}")


if __name__ == "__main__":
    main()