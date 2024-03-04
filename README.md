# ETL Processor and Data Analyzer

This repository contains two Python scripts for data processing and analysis: **ETL Processor** and **Data Analyzer**.

## ETL Processor

The ETL Processor script is designed to extract data from a test data CSV file for AML data provided by kaggle, transform it, and load it into a SQLite database. It supports basic ETL operations and is implemented using Python with the `sqlite3` module.

You can download this data here : https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml/versions/2?resource=download 

### Usage

1. Ensure you have Python installed on your system. We can confirm it works with Python 3.10.11. No additional pip libraries should be required. Please let us know if you have trouble running this locally.
2. Clone this repository to your local machine.
3. Make sure you add the downloaded csv file from kaggle as a file named SAML-D.csv. You can use a different name but then just change the variable db_file in etl_processor.py
4. Navigate to the directory containing the `etl_processor.py` file.
5. Run the script using the following command:
