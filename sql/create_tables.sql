DROP TABLE IF EXISTS alerts;
DROP TABLE IF EXISTS measurements;
DROP TABLE IF EXISTS sensors;

CREATE TABLE sensors (
    sensor_id SERIAL PRIMARY KEY,
    sensor_name VARCHAR(50) NOT NULL,
    production_unit VARCHAR(100) NOT NULL,
    variable_type VARCHAR(50) NOT NULL,
    engineering_unit VARCHAR(20) NOT NULL,
    min_limit NUMERIC NOT NULL,
    max_limit NUMERIC NOT NULL
);

CREATE TABLE measurements (
    measurement_id SERIAL PRIMARY KEY,
    sensor_id INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    value NUMERIC NOT NULL,

    CONSTRAINT fk_measurements_sensor
        FOREIGN KEY (sensor_id)
        REFERENCES sensors(sensor_id)
);

CREATE TABLE alerts (
    alert_id SERIAL PRIMARY KEY,
    measurement_id INTEGER NOT NULL,
    alert_type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_alert_measurement
        FOREIGN KEY (measurement_id)
        REFERENCES measurements(measurement_id)
);