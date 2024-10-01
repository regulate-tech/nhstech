# We can count the number of relationships with other entities each ICB has in the Relationships_Details.csv file
# We group these by the type of relationship based on these codes
# RE4 = IS COMMISSIONED BY
# RE5 = IS LOCATED IN THE GEOGRAPHY OF
# RE6 = IS OPERATED BY
# RE8 = IS PARTNER OF
# NB This returns the ICB's direct relationships with entities that may themselves have relationships with other entities

# USAGE: run this script in the directory where you have prepared the Organisation Directory Service csv files.
# You must already have run the pull-icb.py script to create a csv file with records for each ICB.
 
import pandas as pd
try:
  df_icb = pd.read_csv('icb.csv')
  df_relationship = pd.read_csv('Relationship_Details.csv')

  # Merge the two DataFrames on OrganisationId
  merged_df = pd.merge(df_icb, df_relationship, left_on='OrganisationId', right_on='TargetOrganisationId', how='inner')
  # print(merged_df.head(10))

  # Filter for active relationships
  active_relationships_df = merged_df[merged_df['Status'] == 'Active']

  # Group by ICB name and RelationshipType and count the number of relationships
  icb_relationship_counts = active_relationships_df.groupby(['Name', 'RelationshipId'])['TargetOrganisationId'].count().reset_index()
  print(icb_relationship_counts)

except FileNotFoundError:
  print("One or more files not found. Please upload 'icb.csv' and 'Relationship_Details.csv' to this directory.")
except Exception as e:
  print(f"An error occurred: {e}")

# Write the counts to a file

try:
  icb_relationship_counts.to_csv('icb_rel_counts.csv', index=False)
  print("Successfully wrote icb_rel_counts.csv")
except Exception as e:
  print(f"Error writing to icb_rel_counts.csv: {e}")
