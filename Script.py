# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
import os
import re
import glob
import csv
import shutil

print('Libs Imported')
#endregion

# INPUT VARIABLES----------------------------------------------------------------------------------------
#region
# Directory folder of the csv files you want to process
filename = 'C:/temp/data.csv'
# Can change to xlsx if needed, other changes will be nessesary to code
Extension = 'csv'
# Csv files seperator for input and output files..generally (,) or (|)
Delimiter = ','

# Column to apply the Replacements to
ColName = 'COLUMN_NAME'

# Directory file of Lookup Table
Input_path_Lookup = 'C:/temp/lookuptable.csv'

# Output folder of the Processed CSV file
Output_path_processed_csv = 'C:/FILES/'

new_filename = 'DATA-PROCESSED.csv'

print('Directories loaded...')
#endregion

# READ AND PROCESS THE LOOKUP TABLE----------------------------------------------------------------
#region
df_lookup = pd.read_csv(Input_path_Lookup, dtype={'FIND': object, 'REPLACE': object})

# Delete Rows with everything missing in the row
df_lookup = df_lookup.dropna(axis='index', how='all')

# Delete non Unique (duplicate) FIND rows
df_lookup.drop_duplicates(subset='FIND', keep=False, inplace=True)

# Create a list of Unique Find items
List_Subs = df_lookup['FIND'].tolist()

# Change index to FIND
df_lookup.set_index('FIND', inplace = True)

dict_Subs = df_lookup.to_dict()
dict_Subs = dict_Subs.get('REPLACE')

print(dict_Subs)
#endregion

# Read Data
df_data = pd.read_csv(filename, sep=Delimiter, index_col=False, engine='python', dtype=str)

# Delete Rows with everything missing in the row
df_data = df_data.dropna(axis='index', how='all')

# Swap the name of the column to rename
df.rename(columns={ColName: 'coltoswapxy'}, inplace=True)

# Make the replacements
df_data.coltoswap.replace(dict_Subs , inplace = True)

# Swap back the name of the column to rename
df.rename(columns={'coltoswapxy': ColName}, inplace=True)

print(df_data.head())

#Create new file
Output_filename = Output_path_processed_csv + new_filename
df_data.to_csv(path_or_buf=Output_filename, sep= Delimiter, index=False)
print('---------------------------------------------')
print('DONE')
print('---------------------------------------------')