# Industrial Data Pipeline

End-to-end Data Engineering project that simulates the ingestion, transformation and storage of industrial sensor data.

The project reproduces a simplified industrial process where operational measurements are collected from process equipment and transformed into analytical datasets for monitoring, reporting and operational analysis.

---

## Project Objective

The goal of this project is to demonstrate a complete Data Engineering workflow using Python, PostgreSQL and SQL.

The pipeline covers:

* Data generation
* Data extraction
* Data validation
* Data transformation
* Alert generation
* Data loading
* KPI calculation

---

## Business Scenario

A manufacturing plant continuously collects measurements from industrial process equipment.

Examples of monitored variables include:

* Temperature (°C)
* Pressure (bar)
* Flow Rate (m³/h)
* Energy Consumption (kWh)

Raw operational data may contain measurements outside predefined operating limits. These abnormal operating conditions must be detected, classified and stored for further analysis.

The purpose of the pipeline is to transform raw sensor data into reliable datasets that can be used for operational reporting and decision making.

---

## Simulated Process

The simulated process includes:

* Reactor A
* Reactor B
* Steam inlet to condenser
* Condensate outlet from condenser
* Heat exchanger inlet
* Heat exchanger outlet

Sensors monitor operating conditions such as temperature, pressure, flow rate and energy consumption across different process units.

The generated dataset includes both normal operating conditions and abnormal measurements outside predefined operating limits.

---

## Dataset Size

The simulated dataset contains:

* 20 industrial sensors
* 1 year of hourly measurements
* 175,200 measurement records
* Automatically generated operational alerts

---

## Architecture

```text
Raw Sensor Data
        │
        ▼
Extract
        │
        ▼
Transform
        │
        ├── Column Validation
        ├── Type Validation
        ├── Duplicate Removal
        ├── Range Validation
        └── Alert Generation
        │
        ▼
PostgreSQL
        │
        ▼
SQL KPIs & Analytics
```

---

## Tech Stack

* Python
* PostgreSQL
* SQLAlchemy
* Pandas
* NumPy
* SQL
* ETL Pipelines
* Data Quality Validation

---

## Project Structure

```text
industrial-data-pipeline/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── generate_data.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── sql/
│   ├── create_tables.sql
│   └── kpi_queries.sql
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
└── docs/
    └── data_model.md
```

---

## Data Model

The PostgreSQL database contains three core entities:

### Sensors

Stores sensor metadata and operating limits.

### Measurements

Stores time-series measurements collected from industrial sensors.

### Alerts

Stores operational alerts generated when measurements exceed configured operating limits.

Additional details are available in:

```text
docs/data_model.md
```

---

## Pipeline Steps

### 1. Generate Data

Synthetic industrial sensor data is generated to simulate a production environment.

### 2. Extract

Raw CSV files are loaded into the pipeline.

### 3. Transform

Data quality checks and transformations are applied:

* Column validation
* Data type validation
* Duplicate removal
* Range validation
* Operating limit validation
* Alert generation

### 4. Load

Processed datasets are loaded into PostgreSQL.

The loading process is idempotent and can be executed multiple times without creating duplicate records.

### 5. Analyze

SQL queries generate operational KPIs and performance indicators.

---

## Example KPIs

The project includes SQL queries for:

* Sensors with the highest number of alerts
* Alerts by production unit
* Average temperature by production unit
* Alert severity distribution
* Daily alert trends
* Percentage of measurements outside operating limits

---

## Future Improvements

* Dockerized deployment
* Airflow orchestration
* dbt transformations
* Automated testing
* Data warehouse layer
* Power BI dashboard

---

## Status

Completed MVP.

The project implements a functional end-to-end ETL pipeline with PostgreSQL integration, range validation, operational alert generation and SQL-based KPI analysis.