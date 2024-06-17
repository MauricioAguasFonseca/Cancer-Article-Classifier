<h1 align="center"> Cancer Article Classifier </h1>

![2-grama de  Lung_Cancer](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/78c298d1-04c1-4751-8acd-95aa1607a8ef)
Authored by Mauricio Aguas Fonseca and Cristopher Ditter Gochicoa Ángeles

The present project aimed to develop a classifier for medical articles that determines whether a article falls into one of the following three categories:
1. Colon Cancer
2. Lung Cancer
3. Thyroid Cancer

To achieve this, we utilized the “Medical TextDataset- Cancer Doc Classification” authored by“FALGUNIPATEL1” accessible on Kaggle https://www.kaggle.com/datasets/falgunipatel19/biomedical-text-publication-classification

##Index

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
in Figure 2.The data is evenly distributed.
![Figure 2](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/9ea73567-35bc-47e2-bbd2-a362dc7d583c)

Following that, we examined the word lengths for
each category and their vocabulary coverage, as
seen in Figure 3 it is revealed that there is an
imbalance in the length of the corresponding texts.
![Figure 3](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/d64d5bcb-ff91-4228-af6d-864805ccabab)


Creating word clouds for each category in unigrams, bigrams, trigrams, and tetragrams provided insights. Trigrams ( Figures 4, 5 and 6) revealed references to copyrights, licenses, and journals. This, along with disparities in word counts, suggests that the thyroid and colon datasets might stem from a source encompassing copyright-related content.
![Colon](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/cd51b25f-564e-4eb4-834e-a402f4d2ce6b)
To confirm differences between colon and thyroid categories against lung cancer, we processed the text using Spacy, reduced dimensionality with TSNE, and visualized the data with Plotly.
![TSNE](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/b7943658-5a25-4298-8dea-0c1101fc102b)
Indeed, as shown in the Figure, the data on lung cancer data markedly differs from the other categories. This poses a challenge: any model trained might learn to classify based on volume rather than specific lung cancer features. Consequently, the model might predict lung cancer accurately but struggle to generalize with data not present in the data frame.
<h3>Data Cleasing </h3>
A notable disparity is observed in the length of lung cancer data compared to the other two categories. To address this, we restricted the word count to 2500, where the lung cancer graph declines. Our updated graph is shown in Figure below.
![curvas2](https://github.com/MauricioAguasFonseca/Cancer-Article-Classifier/assets/104111028/b18c6e09-9287-4abf-b3ba-b4c6f0de004d)
The word clouds revealed that colon and thyroid data contained abundant bibliographic references, which were absent in lung cancer data. We utilized regex to filter related words using the following code:
```python
patron = re.compile(r'''\b(?:creative|common|et|al |aal|fig|author|original|license|journal|bmc|plo|
    reference|data|journalpone|august|licensed|common|sharing|author|copyright
    |sharing|distribution|international|permit|author|link|format|licence|material|regulation
    |image|plo|source|adaptation|otherwise|permitted|credit|statutory|pone|acces|open|holder
    |third|indicate|exceeds|party|visit|need|permit|common|copyright|directly|intended)\b''', flags=re.IGNORECASE)
    texto = patron.sub('', texto)
    texto = texto.split()[:2500]





