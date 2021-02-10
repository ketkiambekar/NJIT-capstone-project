# NJIT-Capstone-Project
This is my Capstone Project @ NJIT

This project was done under the not-for-profit organization called [Eve's Appetite for Cure](https://evesappetiteforcure.org/) for their app "Need to Speak". 
The app caters to individuals experiencing cancer and offers a forum functionality among other features. 

This project aims at creating a Topic Classification Module for identifying topics being talked in a post message in the app.
This would be helpful for friend recommendation (profile matching) within the app. 

### What does topic classification mean?
Generally, topic classification refers to identifying broad topics in any text. In our context, it is the identification of the topics of conversation in the cancer forum and classifying user posts into these topics. 


The project consists of 3 parts:

### 1) Topic Modelling :
Uses Latent Dirichlet Allocation (LDA) Algorithm (clustering) to detect broad topics in the in the text corpus. 

### 2) Dataset Creation :
Labelling of Data Corpus to create a dataset for supervised Machine Learning. 

### 3) Topic Classification using Machine Learning
Uses Machine Learning (Linear SVC) to implement topic classification on the topics detected in part 1. 

## Environment and tools

1. Jupyter Notebook
2. Pandas
3. Matplotlib
4. Scikit-learn

## Instructions to run.

#### Software Prerequisites : python3 
1) Clone the repository 
2) Install dependencies from requirements.txt
3) Navigate to and run '/API/main.py'
4) The app will be accessible on the link obtained in output of of main.py

Alternatively, the funcationality can experienced on Google colab in absence of a local python setup:

1) Open the notebook in Colab "/Topic Classication/EAFC_predict.ipynb" by clicking on the 'Open in Colab' badge. 
2) Upload the files "/bin/EAFC_TC.joblib" and "/bin/EAFC_vectorizer.joblib" and "/Data/stopwords.txt" to the files section in the left pane. 
3) Change the text in first cell as needed. 
4) Click Runtime >> Run all. 
5) The Class should be predicted in the very last cell. 

For any questions regarding the project, feel free to reach out to me (Contact info on my [Github Profile](https://github.com/ketkiambekar) )

Copyright 2021. All rights reserved. 
