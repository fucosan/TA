# Aspect-Based Sentiment Analysis for Indonesian Academic Reviews

## Project Overview

This project implements an **Aspect-Based Sentiment Analysis (ABSA)** system for analyzing student reviews and opinions about academic experiences in Indonesian language. The system uses Natural Language Processing (NLP) and Machine Learning techniques to automatically extract aspects and determine sentiment polarity from educational feedback.

## Project Purpose

The goal of this project is to automatically analyze student feedback and opinions about their academic experience, specifically focusing on:
- **Aspect Extraction**: Identifying specific aspects mentioned in reviews (e.g., teaching quality, facilities, grading)
- **Sentiment Classification**: Determining the sentiment (positive, negative, neutral) for each identified aspect
- **Multi-aspect Handling**: Processing reviews that contain multiple aspects and opinions

## Key Features

### 1. Indonesian Text Preprocessing
- **Case Folding**: Converting text to lowercase for normalization
- **Text Normalization**: Handling informal Indonesian text, abbreviations, and typos
- **Stopword Removal**: Filtering out common words that don't contribute to sentiment
- **Stemming**: Reducing words to their root forms using Indonesian stemmer

### 2. Sentence Splitting & Multi-Aspect Detection
- **Conjunction Detection**: Identifying coordinating conjunctions (tapi, namun, hanya, cuma, walaupun, meskipun)
- **Sentence Splitting**: Breaking down complex sentences containing multiple aspects
- **Noun Phrase Detection**: Using POS tagging to identify noun phrases that represent aspects

### 3. Feature Engineering
Multiple feature extraction methods are implemented:
- **Bag of Words (BoW)**: Frequency-based feature representation
- **TF-IDF**: Term Frequency-Inverse Document Frequency weighting
- **POS Tagging**: Part-of-speech features (nouns, verbs, adjectives, adverbs)
- **Word2Vec**: Word embedding representations (mean and IDF-weighted)

### 4. Aspect Categories
The system classifies opinions into the following academic aspects:
1. **Dosen#Mengajar** - Teaching quality of lecturers
2. **Dosen#Umum** - General lecturer-related aspects
3. **Perkuliahan** - Course/lecture quality
4. **Nilai** - Grading system
5. **Layanan** - Academic services
6. **Sarpras** - Facilities and infrastructure
7. **NoAspect** - No specific aspect
8. **Bingung** - Unclear/ambiguous

### 5. Sentiment Polarity
Each aspect is labeled with one of three sentiment polarities:
- **Positif** (Positive)
- **Negatif** (Negative)
- **Netral** (Neutral)

## Technical Stack

### Programming Language
- **Python 3.x**

### Key Libraries & Frameworks
- **NLTK** - Natural Language Toolkit for tokenization and text processing
- **scikit-learn** - Machine learning algorithms (SVM) and feature extraction
- **pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Gensim** - Word2Vec implementation
- **requests** - HTTP library for POS tagger API calls

### Tools & Infrastructure
- **Jupyter Notebook** - Interactive development and experimentation
- **POS Tagger Service** - External service for Indonesian part-of-speech tagging (localhost:9000)
- **XML** - Data storage format for annotated reviews

## Project Structure

```
├── AnotateData.py           # Data annotation interface
├── LoadFile.py              # File loading utilities
├── MyXML.py                 # XML processing utilities
├── bag_of_word.py           # Bag of Words and TF-IDF implementation
├── case_folding.py          # Text normalization
├── normalisasi.py           # Text normalization and cleaning
├── stemmer.py               # Indonesian text stemmer
├── stop_word.py             # Stopword removal
├── split_kalimat.py         # Sentence splitting logic
├── processing.py            # Main processing pipeline
├── transform_fitur.py       # Feature transformation
├── word2vec.py              # Word embedding implementation
├── data/                    # Data directory
│   ├── raw/                 # Raw review data
│   ├── anotated/            # Manually annotated data
│   └── anotatedbackup/      # Backup of annotations
├── *.ipynb                  # Jupyter notebooks for experiments
└── pujangga/                # Indonesian NLP library (submodule)
```

## Machine Learning Approach

### Classification Algorithm
- **Support Vector Machine (SVM)** with linear kernel
- Trained on annotated Indonesian academic review data

### Feature Sets
The project experiments with multiple feature combinations:
1. Frequency + POS Tagging + Word2Vec (mean)
2. Frequency + POS Tagging + Word2Vec (IDF-weighted)
3. Frequency (stemmed) + POS Tagging + Word2Vec
4. TF-IDF + POS Tagging + Word2Vec
5. TF-IDF (stemmed) + POS Tagging + Word2Vec

## Data Processing Pipeline

1. **Data Loading**: Import student reviews from Excel/XML files
2. **Data Filtering**: Remove unnecessary information (names, emails, timestamps)
3. **Preprocessing**: 
   - Case folding
   - Remove non-character elements
   - Normalization
   - Stopword removal
   - Stemming
4. **Sentence Splitting**: Handle multi-aspect reviews
5. **Feature Extraction**: Transform text into numerical features
6. **Classification**: Predict aspect categories and sentiment polarity
7. **Evaluation**: Assess model performance

## Challenges Addressed

### 1. Multi-Aspect Sentences
- Handling reviews that discuss multiple aspects in a single sentence
- Example: "Ruangan sudah sejuk, hanya beberapa ruang saja yang belum memadai"
  - Split into: "Ruangan sudah sejuk" (positive) + "beberapa ruang saja yang belum memadai" (negative)

### 2. Conjunctions at Sentence Boundaries
- Detecting and properly handling coordinating conjunctions
- Ensuring proper noun phrase distribution after splitting

### 3. Indonesian Language Specifics
- Dealing with informal Indonesian text
- Handling abbreviations and slang commonly used by students
- Managing spelling variations and typos

## Research Context

This project appears to be part of a final project (Tugas Akhir/TA) focused on sentiment analysis of Indonesian academic reviews. The system processes actual student feedback data from multiple years (2016-2019) to provide insights into various aspects of the academic experience.

## Skills Demonstrated

### Technical Skills
- Natural Language Processing (NLP)
- Machine Learning (supervised learning)
- Feature Engineering
- Text Preprocessing
- Python Programming
- Data Annotation
- API Integration

### Domain Knowledge
- Sentiment Analysis
- Aspect-Based Opinion Mining
- Indonesian Language Processing
- Educational Data Analysis

### Tools & Technologies
- Python (NLTK, scikit-learn, pandas, NumPy, Gensim)
- Jupyter Notebook
- XML/Excel data handling
- Git version control
- RESTful API integration

## Potential Applications

- Automated analysis of student feedback surveys
- Quality assurance in academic institutions
- Identification of specific areas for improvement in education
- Real-time monitoring of student satisfaction
- Data-driven decision making for academic administration

## Academic Value

This project demonstrates:
- Understanding of advanced NLP concepts
- Ability to work with low-resource languages (Indonesian)
- Experience with real-world, noisy data
- End-to-end machine learning pipeline development
- Research-oriented problem solving

---

## For CV/Resume

**Project Title**: Aspect-Based Sentiment Analysis System for Indonesian Academic Reviews

**Description**: Developed a comprehensive NLP system to automatically analyze student feedback in Indonesian, extracting specific aspects (teaching, facilities, grading) and determining sentiment polarity using machine learning techniques.

**Technologies**: Python, NLTK, scikit-learn, SVM, Word2Vec, TF-IDF, POS Tagging, Jupyter Notebook

**Key Achievements**:
- Implemented multi-aspect sentence detection and splitting algorithm
- Created feature extraction pipeline with 5+ different feature combinations
- Processed and analyzed real student review data across multiple years
- Achieved automated classification of 6+ aspect categories with sentiment analysis
- Handled Indonesian language-specific challenges including informal text and conjunctions
