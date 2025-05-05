# Logistic Regression on LUCAT1 Expression (Gastric Cancer Dataset)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Create the dataset
data = {
    "Sample": [
        "N-delta_TPM", "N6_TPM", "N8_TPM", "NC_TPM", "NV_TPM", "NX_TPM",
        "C-delta_TPM", "C6_TPM", "C8_TPM", "CC_TPM", "CV_TPM", "CX_TPM"
    ],
    "LUCAT1_TPM": [
        0.736652, 0.441554, 0.249550, 0.424481, 0.346003, 1.212087,
        0.745845, 2.260725, 0.324156, 0.754334, 0.435913, 0.073678
    ]
}

#Loading into DataFrame
df = pd.DataFrame(data)
df["Group"] = df["Sample"].apply(lambda x: "Normal" if x.startswith("N") else "Cancer")

#Setting up Features (X) and Labels (y)
X = df["LUCAT1_TPM"].values.reshape(-1, 1)  # Feature: LUCAT1 expression
y = (df["Group"] == "Cancer").astype(int)   # Label: 1 if Cancer, 0 if Normal

#  Building and training Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

#Make Predictions
predictions = model.predict(X)

# Evaluate Model
accuracy = accuracy_score(y, predictions)
print("Accuracy:", accuracy)

# Plot Logistic Regression Curve

# Generate points for smooth curve
# X_test = np.linspace(X.min() - 0.2, X.max() + 0.2, 300).reshape(-1, 1)
# y_prob = model.predict_proba(X_test)[:, 1]

# # Assign colors based on true group
# color_map = {'Normal': 'blue', 'Cancer': 'red'}
# colors = df['Group'].map(color_map)

# # Create figure
# plt.figure(figsize=(8,6))

# # Plot logistic curve
# plt.plot(X_test, y_prob, color='blue', linewidth=2, label='Logistic Regression Curve')
# plt.axhline(0.5, color='grey', linestyle='--', label='Decision Threshold')

# # Plot actual points slightly jittered vertically
# for xi, yi, color in zip(X.flatten(), y, colors):
#     plt.scatter(xi, 0.05 if yi == 0 else 0.95, color=color, edgecolor='k', s=100)

# # Manual legend
# legend_elements = [
#     Line2D([0], [0], marker='o', color='w', label='Normal Sample', markerfacecolor='blue', markersize=10),
#     Line2D([0], [0], marker='o', color='w', label='Cancer Sample', markerfacecolor='red', markersize=10),
#     Line2D([0], [0], color='blue', label='Logistic Regression Curve'),
#     Line2D([0], [0], color='grey', linestyle='--', label='Decision Threshold')
# ]
# plt.legend(handles=legend_elements)

# # Labels
# plt.xlabel('LUCAT1 Expression (TPM)', fontsize=14)
# plt.ylabel('Predicted Probability of Cancer', fontsize=14)
# plt.title('Logistic Regression Model for LUCAT1 Expression', fontsize=16)
# plt.grid(True)
# plt.tight_layout()
# plt.show()