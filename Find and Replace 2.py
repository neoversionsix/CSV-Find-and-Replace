'''
This will find and replace based on a lookup table
'''

# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
print('Libs Imported')
print('')
#endregion

# INPUT VARIABLES----------------------------------------------------------------------------------------
#region
# Directory file you want to process
filename = 'C:/rawdata.xlsx'

# Column to apply the Replacements to
ColName = 'DIST_NAME'

# Directory file of Lookup Table
Input_path_Lookup = 'C:/lookuptable.xlsx'

#Do you want to replace the subset of a cell? If "False" it will match on whole cell
replace_subset=True

# Output folder of the Processed CSV file
Output_path_processed = 'C:/'

new_filename = 'DATA-PROCESSED.xlsx'

print('Directories loaded...')
print('')
print('read lookup table...')
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
print(df_lookup)


#Concatenate ".00" to a column in the lookup table
# Define the string to concatenate
#string_to_concatenate = ".00"
# Concatenate the string to column 'FIND'
#df_lookup['FIND'] = df_lookup['FIND'].apply(lambda x: str(x) + string_to_concatenate)
# Remove all spaces from the 'FIND' column
df_lookup['FIND'] = df_lookup['FIND'].str.strip()

print('creating dictionary for replacements...')
dict_Subs = dict(zip(df_lookup['FIND'], df_lookup['REPLACE']))
print('dictionary for replacements made')

print('')
print('Reading Raw Data...')
print('')
#endregion

print('')
# Read Data
df_data = pd.read_excel(filename, dtype=str)
print('raw data read')

# Delete Rows with everything missing in the row
#df_data = df_data.dropna(axis='index', how='all')

# Swap the name of the column to rename
print('')
print('Swapping Data in raw data with lookup table...')
print('')

# Make the replacements
# Line Below finds and replaces on a whole cell
#df_data.coltoswap.replace(dict_Subs , inplace = True)

# Line Below finds and replaces subsets of cells
df_data[ColName] = df_data[ColName].replace(dict_Subs, regex=replace_subset)

print('swapped')

print('NEW DATA PREVIEW')
print(df_data.head())
print('')
print('Creating new file...')
#Create new file
Output_filename = Output_path_processed + new_filename
df_data.to_excel(Output_filename, index=False)
print('---------------------------------------------')
print('ALL DONE')
print('---------------------------------------------')