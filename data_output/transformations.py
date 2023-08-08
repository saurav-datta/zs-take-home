
import pandas as pd

# Function to transform the date format from MM/DD/YYYY to DD-MM-YYYY
def transform_date(date_str):
    return pd.to_datetime(date_str).strftime('%m-%d-%Y')

# Reading the contents of table_A.csv
table_a_path = "/mnt/data/table_A.csv"
table_a_data = pd.read_csv(table_a_path)

# Creating a new DataFrame to store the transformed data
transformed_data = pd.DataFrame()

# Mapping the columns according to the template
transformed_data['Date'] = table_a_data['Date_of_Policy'].apply(transform_date)
transformed_data['EmployeeName'] = table_a_data['FullName']
transformed_data['Plan'] = table_a_data['Insurance_Plan']
transformed_data['PolicyNumber'] = table_a_data['Policy_No'].str.replace('-', '')
transformed_data['Premium'] = table_a_data['Monthly_Premium']

# Saving the transformed data to a new CSV file
new_csv_path = "/mnt/data/transformed_data.csv"
transformed_data.to_csv(new_csv_path, index=False)
