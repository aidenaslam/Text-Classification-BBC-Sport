# Sports News Classification

Text classification is becoming an increasingly important part of businesses as it allows to easily get insights from data and automate business processes. In this project web scraping was performed to create a dataset of sports news headlines alongside the name of the sport in order to construct a model, using machine learning, that can accurately classify the type of sport a headline presents. The best model was found to be logistic regression which was evaluated using accuracy, precision and f1 score. The dataset and python notebook can be found in the upload sections.

## Collecting Data

* The Beautiful Soup python library was used to scrape news headlines from BBC Sport and Sky Sports News. Both these sources are ethical and no personal data was collected. 

* The dataset consisted of 242 headlines across four sports: football, cricket, tennis and formula 1.

## Exploratory Data Analysis

* Sky Sports News used the terminology *F1* to indicate formula 1 whereas BBC Sport used *formula1*. Therefore, as they are the same sport, the dataset was cleansed to keep the labels of formula 1 headlines consistent to *F1*.

* There were no duplicate headlines or missing labels as a result of the web scraping implemented. 

* A quick analysis showed no class having a significantly smaller number of headlines. 
<img src="https://github.com/aidenaslam/Text-Classification-Sports-News/blob/master/01_EDA_Headline_Categories.png" width="350" height="200" />

## Data Processing

* Count vectorisation and term frequency–inverse document frequency (TFIDF) was implemented to transform text data to numerical data

* The dataset was split using the holdout method with a ratio of 70:30 between training and testing

## Modelling

* The baseline model was logistic regression

* The considered models to beat the baseline were: support vector machine, random forest and naive Bayes.

* Each model was evaluated using 10-fold stratified cross-validation

* As shown below, the baseline model performed the best and thus was selected to be evaluated on the testing dataset.
<img src="https://github.com/aidenaslam/Text-Classification-Sports-News/blob/master/02_CV_Models.png" width="450" height="400" />

## Evaluation

* The logistic regression model produced an accuracy of 94.5% as shown by the confusion matrix below.
<img src="https://github.com/aidenaslam/Text-Classification-Sports-News/blob/master/03_Confusion_Matrix.png" width="450" height="400" />

* The f1 score across all classes was above 90% indicating a high-performing model that can classify sports headlines.
<img src="https://github.com/aidenaslam/Text-Classification-Sports-News/blob/master/04_classification_report.PNG" width="400" height="200" />

## Limitations and Future Work

* This project achieved its goal to accurately classify sports news headlines however, the amount of data collected would need to increase in the future and perhaps be expanded towards other news categories. However, for this project my aim was to use web scraping and NLP to gain an introductory understanding in this subset of AI. 
