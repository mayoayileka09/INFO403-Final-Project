import pandas as pd

# Load the glioblastoma expression data
df = pd.read_csv('GSE255501_rawcounts.txt', sep='\t', index_col=0)

#Finds the row where the gene ID matches LUCAT1's Ensembl ID
lucat1_data = df.loc[df.index.str.contains("ENSG00000248323")]

# View the extracted LUCAT1 counts
print(lucat1_data)

# Load the GSE288489 gastric cancer expression data
df_gastric = pd.read_csv('Gastric_Cancer.txt', sep='\t')

# Filter for LUCAT1 using Gene_Symbol column
lucat1_data = df_gastric[df_gastric['Gene_Symbol'].str.contains("LUCAT1", case=False)]

# View the extracted LUCAT1 expression row
print(lucat1_data)