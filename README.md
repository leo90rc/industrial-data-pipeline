# Industrial Data Pipeline

End-to-end Data Engineering project that simulates the ingestion, transformation and storage of industrial sensor data.

The project reproduces a typical manufacturing environment where operational measurements are collected from production equipment and processed into analytical datasets for reporting and monitoring.

---

## Project Objective

The goal of this project is to demonstrate a complete Data Engineering workflow using Python, PostgreSQL and SQL.

The pipeline covers:

* Data generation
* Data extraction
* Data validation
* Data transformation
* Data loading
* KPI calculation

---

## Business Scenario

A manufacturing plant continuously collects measurements from industrial equipment and production lines.

Examples of monitored variables include:

* Temperature
* Pressure
* Flow rate
* Energy consumption
* Machine status
* Product quality indicators

Raw operational data often contains missing values, duplicated records and measurements outside acceptable operating ranges.

The purpose of the pipeline is to transform raw sensor data into reliable datasets that can be used for operational reporting and decision making.

---

## Dataset Size

The simulated dataset contains:

- 20 industrial sensors
- 1 year of hourly measurements
- 175,200 measurement records

---

## Architecture

```text
Raw Sensor Data
        │
        ▼
Data Extraction
        │
        ▼
Data Validation
        │
        ▼
Data Transformation
        │
        ▼
PostgreSQL Database
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

The project uses a PostgreSQL database containing:

### Sensors

Information about industrial sensors.

### Measurements

Time-series operational measurements collected from sensors.

### Alerts

Operational alerts generated when measurements exceed predefined limits.

---

## Pipeline Steps

### 1. Generate Data

Synthetic industrial sensor data is generated to simulate a production environment.

### 2. Extract

Raw CSV files are loaded into the pipeline.

### 3. Transform

Data quality checks are applied:

* Missing value handling
* Duplicate removal
* Type validation
* Range validation

### 4. Load

Validated data is loaded into PostgreSQL tables.

### 5. Analyze

SQL queries generate operational KPIs and performance indicators.

---

## Example KPIs

* Average temperature by production unit
* Average pressure by production unit
* Total energy consumption
* Alert count by severity
* Percentage of measurements outside operating limits
* Sensor availability rate

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

Work in progress.
