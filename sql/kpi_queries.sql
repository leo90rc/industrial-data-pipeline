-- 1. Sensors with the highest number of alerts
SELECT
    s.sensor_name,
    s.production_unit,
    s.variable_type,
    COUNT(a.alert_id) AS alert_count
FROM alerts a
JOIN measurements m
    ON a.measurement_id = m.measurement_id
JOIN sensors s
    ON m.sensor_id = s.sensor_id
GROUP BY
    s.sensor_name,
    s.production_unit,
    s.variable_type
ORDER BY alert_count DESC;


-- 2. Alerts by production unit
SELECT
    s.production_unit,
    COUNT(a.alert_id) AS alert_count
FROM alerts a
JOIN measurements m
    ON a.measurement_id = m.measurement_id
JOIN sensors s
    ON m.sensor_id = s.sensor_id
GROUP BY s.production_unit
ORDER BY alert_count DESC;


-- 3. Average temperature by production unit
SELECT
    s.production_unit,
    ROUND(AVG(m.value), 2) AS avg_temperature
FROM measurements m
JOIN sensors s
    ON m.sensor_id = s.sensor_id
WHERE s.variable_type = 'temperature'
GROUP BY s.production_unit
ORDER BY avg_temperature DESC;


-- 4. Alert severity distribution
SELECT
    severity,
    COUNT(*) AS alert_count,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM alerts
GROUP BY severity
ORDER BY alert_count DESC;


-- 5. Daily alert trend
SELECT
    DATE(created_at) AS alert_date,
    COUNT(*) AS alert_count
FROM alerts
GROUP BY DATE(created_at)
ORDER BY alert_date;


-- 6. Percentage of measurements outside operating limits by sensor
SELECT
    s.sensor_name,
    s.production_unit,
    s.variable_type,
    COUNT(a.alert_id) AS alert_count,
    COUNT(m.measurement_id) AS total_measurements,
    ROUND(
        COUNT(a.alert_id) * 100.0 / COUNT(m.measurement_id),
        2
    ) AS out_of_limit_percentage
FROM measurements m
JOIN sensors s
    ON m.sensor_id = s.sensor_id
LEFT JOIN alerts a
    ON m.measurement_id = a.measurement_id
GROUP BY
    s.sensor_name,
    s.production_unit,
    s.variable_type
ORDER BY out_of_limit_percentage DESC;