# Find all the Integrated Care Board records in the Organisation_Details.csv file and write these to the file icb.csv
# These are identified by having a RoleId of 'RO318' (NB 'O' is a letter) in linked Role_Details.csv records

# USAGE: run this script in the directory where you have prepared the Organisation Directoru Service csv files.


import pandas as pd

try:
  df_organisation = pd.read_csv('Organisation_Details.csv')
  df_role = pd.read_csv('Role_Details.csv')

  merged_df = pd.merge(df_organisation, df_role, on='OrganisationId', how='inner')
  # print(merged_df.head(10))
  result_df = merged_df[merged_df['RoleId'] == 'RO318'][['OrganisationId', 'Name', 'Status_y', 'RoleId']]
  print(result_df.to_string())

except FileNotFoundError:
  print("One or more files not found. Please upload 'Organisation_Details.csv' and 'Role_Details.csv' to this directory.")

# Write the records out to a file called icb.csv

try:
  result_df.to_csv('icb.csv', index=False)
  print("Successfully wrote icb.csv")
except Exception as e:
  print(f"Error writing to icb.csv: {e}")
