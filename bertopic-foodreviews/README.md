# Topic Modeling with BERTopic on Amazon Fine Food Reviews

This project applies **BERTopic** to perform topic modeling on the [Amazon Fine Food Reviews](https://www.kaggle.com/snap/amazon-fine-food-reviews) dataset, with a focus on uncovering recurring themes in **negative customer feedback**.

---

## 📌 Overview

**BERTopic** is a topic modeling technique that leverages **BERT embeddings** and **class-based TF-IDF (c-TF-IDF)** to generate coherent and interpretable topics. It performs topic modeling in three main steps:

1. **Document Embedding**: Use pre-trained transformer models (e.g., Sentence-BERT) to convert texts into dense vector representations.
2. **Document Clustering**: Cluster embeddings using dimensionality reduction (e.g., UMAP) and clustering algorithms (e.g., HDBSCAN).
3. **Topic Representation**: Extract and represent the main themes using c-TF-IDF for interpretability.

---

## 📂 Dataset

The dataset used is the [Amazon Fine Food Reviews](https://www.kaggle.com/snap/amazon-fine-food-reviews), which contains over **500,000 food-related reviews** spanning more than a decade (up to October 2012).

### Key fields include:
- `Score` (1 to 5 stars)
- `Text` (full review)
- `Summary` (short summary of the review)
- `Time`, `UserId`, `ProductId`, etc.

---

## 🎯 Objective

The primary goal of this project is to:

- Identify and analyze **dominant topics** within **negative reviews** (1-star and 2-star).
- Enable insights that can support product improvement.

---

## ✅ Features

- Utilizes `all-MiniLM-L6-v2` from SentenceTransformers for efficient and compact embeddings.
- UMAP + HDBSCAN clustering pipeline.
- Interactive visualizations:

---

## 📬 License

Dataset © Amazon. Refer to [Kaggle Terms](https://www.kaggle.com/terms) for dataset usage policy.
