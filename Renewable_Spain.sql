-- START Gabriel Gaynor BLOCK

CREATE TABLE time_stamps (
	row int PRIMARY KEY,
    time text
    );
    
INSERT INTO 
   time_stamps (row, time) 
SELECT 
   ROW_NUMBER() OVER (ORDER BY time) as row, 
   time 
FROM 
   energy_dataset
 ;
   
CREATE TABLE load (
    row_key int,
    time text PRIMARY KEY,
    forcasted_load int,
    actual_load int
    )
 ;
    
INSERT INTO 
	load (row_key, time, forcasted_load, actual_load) 
SELECT 
	ROW_NUMBER() OVER (ORDER BY total_load_forecast) as row_key,
	time,
	total_load_forecast,
	total_load_actual 
FROM 
	energy_dataset;
	
SELECT * FROM load LIMIT 5;

-- END Gabriel Gaynor Block


-- START Miguel Grella BLOCK
-- Please see `miguel_grella_insert_table.ipynb` for the code used to generate the data for fossil_fuel_generation table

-- Example of query using fossil_fuel_generation table
SELECT
   strftime('%Y', time) AS year, SUM(GEN_OIL), SUM(GEN_GAS)
   FROM fossil_fuel_generation GROUP BY year;


-- Example of query using fossil_fuel_generation and load table

WITH daily_load AS (
SELECT strftime('%Y-%m-%d', time) AS time, AVG(forcasted_load) AS forcasted_load
FROM load
GROUP BY time
)

SELECT fg.TIME, GEN_GAS, GEN_OIL, daily_load.forcasted_load as LOAD
FROM fossil_fuel_generation fg
INNER JOIN daily_load ON fg.TIME = daily_load.time

-- END Miguel Grella  Block



-- START Greg Spina BLOCK
-- Please see `renewable.ipynb` for the code used to generate the data for renewable_fuel_generation table
-- END Greg Spina BLOCK

