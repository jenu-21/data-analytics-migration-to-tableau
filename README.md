# Data Analytics Migration Tableau

###### This project takes the role of a data analyst at Skyscanner who has to migrate existing data analytics tasks from an excel based system to a visually interactive Tableau report.  
###### The project involved using a variety of data sources and techniques such as AWS RDS, CSV files, Pandas, data cleaning in Vscode Python, exporting onto Postgresql on PgAdmin4 to undertake SQL queries and finally exporting the data onto Tableau desktop for data visualisation. 

## AWS RDS
#####  Created an RDS instance and an S3 bucket which setups the database and stores it respectively. 

## Loading the data 
##### The CSV datafiles containing the flight's data for each year from 1987 - 1996 are imported into my local machine through Pandas 
##### The data is cleaned in my flights.py file to remove null values and then combined into one master dataframe.
##### The data is then exported on my s3 bucket through the 'aws s3 cp' command and then downloaded from my bucket onto my local machine.

## PostgreSQL RDS Data import and reporting
##### Connected my PgAdmin4 to the PostgreSQL RDS database, then imported my master dataframe into it and proceeded to undertake some SQL queries. 

## Integrate Tableau desktop with PostgreSQL RDS and Tableau reports
##### Once connecting my PostgreSQL to my Tableau Desktop it was easier to explore the dataset through a variety of visualisation techniques tableau has such as treemap, line charts or histograms. 
