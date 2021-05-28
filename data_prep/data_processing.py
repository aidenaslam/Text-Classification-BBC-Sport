import pandas as pd
from datetime import date
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split


def data_processing(dataset_1, dataset_2, flag):
    """ Performs data processing of both datasets 
        If flag is set True, CSV of dataset is saved
    """
    # combine datasets
    dataset_combined = combine_dataset(dataset_1, dataset_2)

    # save_to_csv
    if flag == True:
        save_to_csv(dataset_combined)

    # rename class name for F1
    dataset_combined = check_classes(dataset_combined)

    # perform tfidf transformation
    X = dataset_combined.iloc[:,0] # extract column with headlines
    y = dataset_combined.iloc[:,-1] # extract column with labels
    X_vec = tfidf_transform(X)

    return X_vec, y


def combine_dataset(dataset_1, dataset_2):
    """ Combines two datasets """
    dataset_combined = pd.concat([dataset_1, dataset_2])

    return dataset_combined

def save_to_csv(dataset):
    """ Saves dataset as csv with today's date """

    today_date = date.today().strftime("%d_%m_%Y")
    dataset.to_csv(f'Sports_News_{today_date}.csv', index= False)

def check_classes(dataset):
    """ Checks classes of news """

    # Change formula1 to f1 
    dataset['Sport'] = dataset['Sport'].replace(['formula1'],'f1')

    return dataset

def count_vectorise(x):
    """ Perform count vectorisation """
    vectorizer = CountVectorizer(stop_words='english')
    X_vec = vectorizer.fit_transform(x)
    X_vec.todense() # convert sparse matrix into dense matrix
    
    return X_vec

def tfidf_transform(x):
    """ TFIDF transformation """
    tfidf = TfidfTransformer()
    x_vec = count_vectorise(x)
    X_tfidf = tfidf.fit_transform(x_vec)
    X_tfidf = X_tfidf.todense()

    return X_tfidf

def split_dataset(x_tfidf, y, test_size_split):
    """ Split dataset into training and testing """
    X_train, X_test, y_train, y_test = train_test_split(
        x_tfidf, 
        y, 
        test_size = test_size_split, 
        random_state = 0
        )

    return X_train, X_test, y_train, y_test

