# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# GSE288489: Gastric cancer dataset - LUCAT1 expression, pulled using Extract_Data
data_gse288489 = {
    "Sample": [
        "N-delta_TPM", "N6_TPM", "N8_TPM", "NC_TPM", "NV_TPM", "NX_TPM",
        "C-delta_TPM", "C6_TPM", "C8_TPM", "CC_TPM", "CV_TPM", "CX_TPM"
    ],
    "LUCAT1_TPM": [
        0.736652, 0.441554, 0.249550, 0.424481, 0.346003, 1.212087,
        0.745845, 2.260725, 0.324156, 0.754334, 0.435913, 0.073678
    ]
}

# Create a DataFrame
df_gse288489 = pd.DataFrame(data_gse288489)

# Assign group labels: Normal vs Cancer
df_gse288489["Group"] = df_gse288489["Sample"].apply(lambda x: "Normal" if x.startswith("N") else "Cancer")

# Create the plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="Group", y="LUCAT1_TPM", data=df_gse288489, palette={"Normal": "skyblue", "Cancer": "salmon"})
sns.stripplot(x="Group", y="LUCAT1_TPM", data=df_gse288489, color="black", size=6, jitter=True)

# Customize the plot
plt.title("LUCAT1 Expression in Gastric Cancer vs Normal (GSE288489)", fontsize=14)
plt.ylabel("LUCAT1 TPM", fontsize=12)
plt.xlabel("")
plt.xticks(fontsize = 18)
plt.tight_layout()
plt.show()



# GSE255501: Glioblastoma knockdown experiment - LUCAT1 expression, also pulled form Extract_Data.py
data_gse255501 = {
    "Sample": ["NT1_1", "NT1_2", "NT21_1", "NT21_2", "sh1_1", "sh1_2", "sh2_1", "sh2_2"],
    "LUCAT1_Count": [585, 645, 10, 8, 153, 84, 343, 344]
}

# Create a DataFrame
df_gse255501 = pd.DataFrame(data_gse255501)

# Assign group labels based on sample condition
#Easier to ready than pre-assigned labels
def assign_group(sample):
    if sample.startswith("NT1"):
        return "Control-Normoxia"
    elif sample.startswith("NT21"):
        return "Control-Hypoxia"
    elif sample.startswith("sh1"):
        return "Knockdown-Normoxia"
    elif sample.startswith("sh2"):
        return "Knockdown-Hypoxia"

df_gse255501["Group"] = df_gse255501["Sample"].apply(assign_group)

# Creating the plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="Group", y="LUCAT1_Count", data=df_gse255501, palette="Set3")
sns.stripplot(x="Group", y="LUCAT1_Count", data=df_gse255501, color="black", size=6, jitter=True)

# Customizung the plot
plt.title("LUCAT1 Expression in Glioblastoma Knockdown Experiment (GSE255501)", fontsize=14)
plt.ylabel("LUCAT1 Raw Counts", fontsize=12)
plt.xlabel("")
plt.xticks(rotation=20, fontsize = 18)
plt.tight_layout()
plt.show()