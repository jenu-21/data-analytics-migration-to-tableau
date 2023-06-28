### Creating the flights table

```sql
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    Year INTEGER,
    Month INTEGER,
    DayofMonth INTEGER,
    DayOfWeek INTEGER,
    DepTime FLOAT,
    CRSDepTime FLOAT,
    ArrTime FLOAT,
    CRSArrTime FLOAT,
    UniqueCarrier TEXT,
    FlightNum INTEGER,
    ActualElapsedTime FLOAT,
    CRSElapsedTime FLOAT,
    ArrDelay FLOAT,
    DepDelay FLOAT,
    Origin TEXT,
    Dest TEXT,
    Distance FLOAT,
    Cancelled INTEGER,
    Diverted INTEGER,
    TailNum TEXT,
    AirTime FLOAT,
    TaxiIn FLOAT,
    TaxiOut FLOAT
);
```

### How many total records does the table contain? 
```sql
SELECT COUNT(*) AS total_records
FROM flights;
```
### output:
![total_records](/sql_results/total_records.png)

### Which year had the most number of total inbound and outbound flights? 

```sql
SELECT year, COUNT(*) AS total_flights
FROM flights
GROUP BY year
ORDER BY total_flights DESC
LIMIT 1;
```
### output: 
![inbound_outbound](/sql_results/inbound_outbound.png)

### Which country is the most popular destination for flights?

```sql 

SELECT dest, COUNT(*) AS total_flights
FROM flights
GROUP BY dest
ORDER BY total_flights DESC
LIMIT 1;
```
### output: 
![popular_destination](/sql_results/popular_destination.png)
