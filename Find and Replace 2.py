'''
This will find and replace based on a lookup table
'''



# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
print('Libs Imported')
#endregion

# INPUT VARIABLES----------------------------------------------------------------------------------------
#region
# Directory file you want to process
filename = 'C:/DATA.xlsx'

# Column to apply the Replacements to
ColName = 'DIST_NAME'

# Directory file of Lookup Table
Input_path_Lookup = 'C:/lookuptable.xlsx'

#Do you want to replace the subset of a cell? If false it will match on whole cell
replace_subset=True

# Output folder of the Processed CSV file
Output_path_processed = 'C:/'

new_filename = 'DATA-PROCESSED-2.xlsx'

print('Directories loaded...')
print('doing stuff now...')
print('')
#endregion

# READ AND PROCESS THE LOOKUP TABLE----------------------------------------------------------------
#region
df_lookup = pd.read_excel(Input_path_Lookup, dtype=str)
print('lookup dataframe')
print(df_lookup)



# Delete Rows with everything missing in the row
df_lookup = df_lookup.dropna(axis='index', how='all')
print('after dropna')
print(df_lookup)

# Delete non Unique (duplicate) FIND rows keep the first
df_lookup.drop_duplicates(subset=['FIND'], keep='first', inplace=True)
print('after dropdup')

#Concatenate ".00"
# Define the string to concatenate
string_to_concatenate = ".00"
# Concatenate the string to column 'FIND'
df_lookup['FIND'] = df_lookup['FIND'].apply(lambda x: str(x) + string_to_concatenate)

dict_Subs = dict(zip(df_lookup['FIND'], df_lookup['REPLACE']))

print('')
print('Reading Data...')
print('')
#endregion



# Read Data
df_data = pd.read_excel(filename, dtype=str)
print('data read')

# Delete Rows with everything missing in the row
#df_data = df_data.dropna(axis='index', how='all')

# Swap the name of the column to rename
print('')
print('Swapping...')
print('')
df_data.rename(columns={ColName: 'coltoswap'}, inplace=True)

# Make the replacements
# Line Below finds and replaces on a whole cell
#df_data.coltoswap.replace(dict_Subs , inplace = True)

# Line Below finds and replaces subsets of cells
df_data['coltoswap'] = df_data['coltoswap'].replace(dict_Subs, regex=replace_subset)

# Swap back the name of the column to rename
df_data.rename(columns={'coltoswap': ColName}, inplace=True)
print('swapped')

print('NEW DATA PREVIEW')
print(df_data.head())
print('')
print('Creating new file...')
#Create new file
Output_filename = Output_path_processed + new_filename
df_data.to_excel(Output_filename, index=False)
print('---------------------------------------------')
print('DONE')
print('---------------------------------------------')
