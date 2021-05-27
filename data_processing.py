import pandas as pd
from datetime import date


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

