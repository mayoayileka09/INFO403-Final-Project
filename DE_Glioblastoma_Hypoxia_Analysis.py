# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

#  Create LUCAT1 expression data for Glioblastoma dataset (GSE255501)
data_gse255501 = {
    "Sample": ["NT1_1", "NT1_2", "NT21_1", "NT21_2", "sh1_1", "sh1_2", "sh2_1", "sh2_2"],
    "LUCAT1_Count": [585, 645, 10, 8, 153, 84, 343, 344]
}

df_gbm = pd.DataFrame(data_gse255501)

# Assign groups
def assign_group(sample):
    if sample.startswith("NT1"):
        return "Control-Normoxia"
    elif sample.startswith("NT21"):
        return "Control-Hypoxia"
    elif sample.startswith("sh1"):
        return "Knockdown-Normoxia"
    elif sample.startswith("sh2"):
        return "Knockdown-Hypoxia"

df_gbm["Group"] = df_gbm["Sample"].apply(assign_group)

#Hypoxia comparison (Control vs Knockdown under hypoxia)
control_hypoxia = df_gbm[df_gbm["Group"] == "Control-Hypoxia"]["LUCAT1_Count"]
knockdown_hypoxia = df_gbm[df_gbm["Group"] == "Knockdown-Hypoxia"]["LUCAT1_Count"]

# Calculate statistics
mean_control_hypoxia = np.mean(control_hypoxia)
mean_knockdown_hypoxia = np.mean(knockdown_hypoxia)

# log2 fold change
log2fc_hypoxia = np.log2(mean_knockdown_hypoxia / mean_control_hypoxia)

# t-test
stat_hypoxia, pval_hypoxia = ttest_ind(knockdown_hypoxia, control_hypoxia)

#  Create volcano plot (for LUCAT1 only)
plt.figure(figsize=(6,6))
plt.scatter(log2fc_hypoxia, -np.log10(pval_hypoxia), color='green')
plt.text(log2fc_hypoxia, -np.log10(pval_hypoxia), "LUCAT1", fontsize=12, ha='right')
plt.axhline(y=-np.log10(0.05), color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Volcano Plot (GSE255501 - Glioblastoma Hypoxia)', fontsize=14)
plt.xlabel('log2(Fold Change)', fontsize=18)
plt.ylabel('-log10(p-value)', fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.show()

#  Print results
print(f"Mean Control Hypoxia Expression: {mean_control_hypoxia}")
print(f"Mean Knockdown Hypoxia Expression: {mean_knockdown_hypoxia}")
print(f"log2(Fold Change): {log2fc_hypoxia:.3f}")
print(f"p-value: {pval_hypoxia:.4e}")
