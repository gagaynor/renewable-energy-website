
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
    row_key int PRIMARY KEY,
    time text,
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