import time
import os

from parameters.project_parameters import (
                url_list_bbc, 
                url_list_sky_sports,
                save_models
)
from data_prep.scrape_data import bbc_sport_news, sky_sports_news
from data_prep.data_processing import (
    data_processing, split_dataset, combine_dataset, rename_class
)
from modelling_evaluation.build_models import (
    logistic_regression_model
    )
from evaluation.model_evaluation import cross_validation, confusion_matrix

from joblib import dump

def model_eval():

    # scrape data
    print("Scraping data")
    bbc_dataset = bbc_sport_news(url_list_bbc)
    skysports_dataset = sky_sports_news(url_list_sky_sports)

    # process_datasets
    print("Processing data for machine learning...")
    dataset_combined = combine_dataset(bbc_dataset, skysports_dataset, True)
    dataset_combined = rename_class(dataset_combined)
    X_vec, y = data_processing(dataset_combined)

    # Split into training and testing (0.3 for testing)
    X_train, X_test, y_train, y_test = split_dataset(X_vec, y, 0.3)
    print("Data processing complete")

    # Build machine learning models
    print("Building machine learning model...")
    log_reg = logistic_regression_model(X_train, y_train)

    # cross validation
    print("Performing stratified cross-validation...")
    models = (('Logistic Reg (baseline)', log_reg ))
    cross_validation(models, X_train, y_train, 10)

    # confusion matrix
    print("Saving confusion matrix...")
    confusion_matrix(log_reg, X_train, y_train, "logistic_regression")

    # Save model to saved_models folder 
    print("Saving model")
    pkl_filename = "final_model.joblib"
    with open(os.path.join(save_models, pkl_filename), 'wb') as file:
        dump(log_reg, file)
