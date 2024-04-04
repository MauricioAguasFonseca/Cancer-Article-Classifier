<h1 align="center"> Cancer Article Classifier </h1>

![2-grama de  Lung_Cancer](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/78c298d1-04c1-4751-8acd-95aa1607a8ef)

The present project aimed to develop a classifier for medical articles that determines whether a article falls into one of the following three categories:
1. Colon Cancer
2. Lung Cancer
3. Thyroid Cancer

To achieve this, we utilized the “Medical TextDataset- Cancer Doc Classification” authored by“FALGUNIPATEL1” accessible on Kaggle https://www.kaggle.com/datasets/falgunipatel19/biomedical-text-publication-classification

<h2>Project Utility </h2>
<h3>Early Diagnosis</h3>
One of the most significant benefits would be the
ability to detect cancer types early through textual
information analysis. Early diagnosis enhances the
prospects of successful treatment and improves patient survival. It’s important to note that ML and
DL models solely serve as SUPPORT for medical
professionals.
<h3>Bibliographic Streamlining</h3>
This project aims to streamline medical research
by identifying patterns and trends within extensive
datasets. Model outcomes could generate research
hypotheses, guide clinical studies, and enhance understanding of unique cancer characteristics.
<h3>Classification Automation</h3>
Automating the article classification process can
save time and resources. The speed of ”Natural
Language Processing” (NLP) model analysis surpasses human capability in processing vast amounts
of information in a short time.
<h2>Exploratory Data Analysis </h2>
<h3>Information Quantity by Type </h3>

The dataset contains a ”Type” column indicating
one of the three cancer types and a ”Symptom”
column containing the corresponding text.
Initially, we ensured data balance, as depicted
in Figure 1.The data is evenly distributed.
![curvas](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/d64d5bcb-ff91-4228-af6d-864805ccabab)

Following that, we examined the word lengths for
each category and their vocabulary coverage, as
seen in Figure 2, it is revealed that there is an
imbalance in the length of the corresponding texts.
Creating word clouds for each category i
