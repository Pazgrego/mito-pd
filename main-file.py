import pandas as pd

file_path = "GSE49036_series_matrix.txt"

# Read the expression matrix (skip lines starting with "!")
#file_path = path to the data
#sep="\t" = colums in the file are seperated by tab characters (/t), not commas - this is a TSV file
#comment="!" = Lines stating with ! are metadata, ignore lines starting with "!"
#index_col=0 = the first column should be used as the row index (gene names)
#df = pandas dataframe object that contains the data from the file
#read_csv() = reads the file into a dataframe
df = pd.read_csv(file_path, sep="\t", comment="!", index_col=0)

# Peek at the data - print the first 5 rows of the dataframe
print(df.head())

print(df.shape) #(54675, 28) #54675 genes (rows), 28 samples/brains (colums)

#1007_s_at is the microarray probe IDs 
#GSM1192001 is the sample IDs - each represent a different brain sample
#5.213 is the gene espression values - the measured intensity of how much mRNA for that gene was detected in the sample. theyre usually log transformed - so 5.0 means moderate expression, 8.0 means high expression.

import seaborn as sns
import matplotlib.pyplot as plt

# 1) pick Parkinson/mitochondria-related genes
genes = ["PINK1", "PRKN", "MFN1", "MFN2", "OPA1", "DJ1", "LRRK2", "SNCA"]

# 2) microarray uses probe IDs, so we search rows that CONTAIN these names
mtx = df[df.index.str.contains("|".join(genes), case=False, na=False)]

# 3) plot
plt.figure(figsize=(10, 4))
sns.heatmap(mtx, cmap="viridis")
plt.title("Mitochondrial / PD-related genes in GSE49036")
plt.xlabel("Samples")
plt.ylabel("Probes / genes")
plt.show()

#mito_genes = ["PINK1", "PRKN", "MFN1", "MFN2", "OPA1", "DJ1", "LRRK2", "SNCA"]

# Filter rows containing those genes (case-insensitive)
#mito_df = df[df.index.str.contains('|'.join(mito_genes), case=False, na=False)]
#mito_df.head()

#print(mito_df.shape)

