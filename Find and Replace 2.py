# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
print('Libs Imported')
#endregion

# INPUT VARIABLES----------------------------------------------------------------------------------------
#region
# Directory folder of the csv files you want to process
filename = 'C:/DATA.xlsx'
# Can change to xlsx if needed, other changes will be nessesary to code
Extension = 'xlsx'

# Column to apply the Replacements to
ColName = 'DIST_NAME'

# Directory file of Lookup Table
Input_path_Lookup = 'C:/lookuptable.xlsx'

# Output folder of the Processed CSV file
Output_path_processed = 'C:/'

new_filename = 'DATA-PROCESSED.xlsx'

print('Directories loaded...')
print('doing stuff now...')
print('')
#endregion

# READ AND PROCESS THE LOOKUP TABLE----------------------------------------------------------------
#region
df_lookup = pd.read_excel(Input_path_Lookup, dtype=str)

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

print('SUBSTITUTIONS...')
print(dict_Subs)
print('')
print('Reading Data...')
print('')
#endregion

# Read Data
df_data = pd.read_excel(filename, dtype=str)

# Delete Rows with everything missing in the row
#df_data = df_data.dropna(axis='index', how='all')

# Swap the name of the column to rename
df_data.rename(columns={ColName: 'coltoswap'}, inplace=True)

# Make the replacements
# Line Below finds and replaces on a whole cell
#df_data.coltoswap.replace(dict_Subs , inplace = True)

# Line Below finds and replaces subsets of cells
df_data['coltoswap'] = df_data['coltoswap'].apply(lambda x: ''.join([dict_Subs.get(i, i) for i in x]))

# Swap back the name of the column to rename
df_data.rename(columns={'coltoswap': ColName}, inplace=True)

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