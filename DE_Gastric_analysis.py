# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Step 1: Creating the LUCAT1 expression dataframe
data = {
    "Sample": [
        "N-delta_TPM", "N6_TPM", "N8_TPM", "NC_TPM", "NV_TPM", "NX_TPM",
        "C-delta_TPM", "C6_TPM", "C8_TPM", "CC_TPM", "CV_TPM", "CX_TPM"
    ],

    #Expression(TPM), maooed to Samples above
    "LUCAT1_TPM": [
        0.736652, 0.441554, 0.249550, 0.424481, 0.346003, 1.212087,
        0.745845, 2.260725, 0.324156, 0.754334, 0.435913, 0.073678
    ]
}

#Mapping
df = pd.DataFrame(data)
df["Group"] = df["Sample"].apply(lambda x: "Normal" if x.startswith("N") else "Cancer")

# Separate into groups
cancer_expr = df[df["Group"] == "Cancer"]["LUCAT1_TPM"]
normal_expr = df[df["Group"] == "Normal"]["LUCAT1_TPM"]

#  Calculate statistics
mean_cancer = np.mean(cancer_expr)
mean_normal = np.mean(normal_expr)

# log2 fold change
log2fc = np.log2(mean_cancer / mean_normal)

# t-test
stat, pval = ttest_ind(cancer_expr, normal_expr)

# Create volcano plot (for LUCAT1 only)
plt.figure(figsize=(6,6))
plt.scatter(log2fc, -np.log10(pval), color='red')
plt.text(log2fc, -np.log10(pval), "LUCAT1", fontsize=12, ha='right')
plt.axhline(y=-np.log10(0.05), color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Volcano Plot (GSE288489 - LUCAT1)', fontsize=14)
plt.xlabel('log2(Fold Change)', fontsize=18)
plt.ylabel('-log10(p-value)', fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.show()

# Print out the results
print(f"Mean Cancer Expression: {mean_cancer}")
print(f"Mean Normal Expression: {mean_normal}")
print(f"log2(Fold Change): {log2fc:.3f}")
print(f"p-value: {pval:.4e}")