# Python-Sentiment

## 1. Introduction

Models are created that are capable of predicting the sentiment of documents.

## 2. Installation

This step only on Windows 10:

- Install Windows subsystem for Linux
- Install Ubuntu from the store

## 3. Run

In Ubuntu (sudo may be required):

      git clone git@github.com:Menziess/Python-Sentiment.git
      cd Python-Sentiment

      pip3 install -r requirements.txt
      jupyter notebook

The classifier expects a .csv file with two columns in the data folder:
- Review: the review text
- Score: a star rating from 1...5

Run the [jupyter notebook](src/Tensorflow%20DNNClassifier.ipynb) to train a model, save it in the [/models](src/models/) folder.

Run [App.py] to run a web api that classifies a string that is passed as a url fragment.

```
python src/App.py
```
