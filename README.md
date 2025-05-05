#  LUCAT1 Expression in Cancer: RNA-Seq Analysis & Stress Response

This repository contains code and data processing pipelines for analyzing the expression of the long non-coding RNA **LUCAT1** across two public RNA-seq datasets in **gastric cancer** and **glioblastoma**. The project explores LUCAT1’s potential roles in cancer progression, therapy resistance, and stress adaptation (particularly hypoxia).

---


##  Datasets

### 1. Gastric Cancer
- **GEO Accession**: [GSE288489](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE288489)
- **Samples**: Gastric cancer cells vs. normal epithelial cells
- **Goal**: Compare LUCAT1 expression in cancer vs. normal tissue

### 2. Glioblastoma
- **GEO Accession**: [GSE255501](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255501)
- **Samples**: Control vs. LUCAT1 knockdown under normoxia and hypoxia
- **Goal**: Explore LUCAT1’s response to cellular stress and knockdown

---

##  Analysis Overview

- Normalization and differential expression analysis using DESeq2 (via Galaxy and Python replication)
- 2-sample t-tests for TPM or raw count comparisons
- Log2 fold change and p-value calculations
- Visualizations (boxplots, volcano plots) using `matplotlib` and `seaborn`
- Optional logistic regression classification based on gene expression

---

##  Key Results

- **Gastric Cancer**: Modest, non-significant upregulation of LUCAT1  
  (log2FC = 0.43, p = 0.584)
- **Glioblastoma**:  
  - Normoxia: LUCAT1 downregulated after knockdown (log2FC = -2.38, p = 0.008)  
  - Hypoxia: LUCAT1 strongly upregulated after knockdown (log2FC = +5.25, p < 1e-5)

---

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn scipy numpy
