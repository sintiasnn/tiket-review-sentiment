# Sentiment Analysis: Tiket.com Google Play Store Reviews

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange?logo=tensorflow)
![Notebook](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter)

Multi-class sentiment classification on Indonesian-language reviews of the Tiket.com app, using deep learning models (LSTM, GRU, CNN) with traditional ML as baseline.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Notebook Flow](#notebook-flow)
- [Experiment Results](#experiment-results)
- [Getting Started](#getting-started)
- [Author](#author)

---

## Overview

This project performs sentiment analysis on user reviews of the Tiket.com app scraped from Google Play Store. Reviews are classified into three sentiment classes using a lexicon-based labeling approach and trained with multiple deep learning architectures.

**Pipeline stages:**
1. **Data Collection** — Scrape reviews via Google Play Scraper
2. **Preprocessing** — Text cleaning, normalization, slang fixing, stopword removal
3. **Labeling** — Lexicon-based sentiment labeling (InSet Lexicon)
4. **Data Balancing** — Resampling to handle class imbalance
5. **Modeling** — Baseline ML + 3 deep learning experiments
6. **Evaluation** — Accuracy comparison across all models

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.10 |
| Deep Learning | TensorFlow / Keras (LSTM, GRU, CNN) |
| ML Baseline | Scikit-learn |
| NLP | NLTK, Sastrawi, Gensim |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Data Source | Google Play Store (google-play-scraper) |
| Environment | Google Colab |

## Project Structure

```
tiket-review-sentiment/
├── notebook/
│   └── sentiment_analysis.ipynb   # Main analysis & modeling
├── src/
│   └── scrape_reviews.py          # Google Play scraper script
├── data/
│   └── raw_reviews.csv            # Raw scraped reviews
└── requirements.txt
```

## Dataset

- **Source**: Google Play Store — Tiket.com app (`com.tiket.gits`)
- **Size**: 20,000 reviews
- **Language**: Bahasa Indonesia
- **Task**: 3-class classification — Positive / Neutral / Negative
- **Labeling**: Lexicon-based using [InSet Lexicon](https://github.com/angelmetanosaa/dataset)

## Notebook Flow

| # | Section |
|---|---|
| 1 | Data Collection |
| 2 | Data Preprocessing |
| 3 | Labeling (3 Classes) |
| 3.1 | Data Balancing |
| 4 | Prepare Data for Deep Learning |
| 4.5 | Baseline: Traditional ML Models |
| 5 | Experiment 1 — LSTM (80/20 split) |
| 6 | Experiment 2 — GRU (80/20 split) |
| 7 | Experiment 3 — CNN (70/30 split) |
| 8 | Visualizations |
| 9 | Inference |
| 10 | Save Best Model |

## Experiment Results

| Model | Type | Split | Test Accuracy |
|---|---|---|---|
| Logistic Regression (TF-IDF) | Traditional ML | 80/20 | 92.76% |
| Random Forest (TF-IDF) | Traditional ML | 80/20 | 94.69% |
| LSTM | Deep Learning | 80/20 | 33.33% |
| GRU | Deep Learning | 80/20 | 33.33% |
| **CNN** | **Deep Learning** | **70/30** | **94.76%** |

> LSTM dan GRU tidak konvergen (stuck di ~33.33% — random chance untuk 3 kelas). Best model saved as `sentiment_model_cnn.h5`.

## Getting Started

### 1. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Scrape Data

```bash
python src/scrape_reviews.py --max-samples 20000 --output data/raw_reviews.csv
```

### 3. Upload to Google Drive

Upload the generated `data/raw_reviews.csv` to your Google Drive root folder.

### 4. Run Notebook

Open `notebook/sentiment_analysis.ipynb` in **Google Colab**, mount your Google Drive, and run all cells.

## Author

**Ni Putu Sintia Wati**
- GitHub: [@sintiasnn](https://github.com/sintiasnn)
