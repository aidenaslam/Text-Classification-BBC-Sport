import time

from parameters.project_parameters import url_list_bbc, url_list_sky_sports
from data_prep.scrape_data import bbc_sport_news, sky_sports_news
from data_prep.data_processing import data_processing, split_dataset
from modelling.build_models import (
    logistic_regression_model
    )
from evaluation.model_evaluation import cross_validation, confusion_matrix

## implement logs
## unit testing


start = time.time()

# scrape data
print("Scraping data")
bbc_dataset = bbc_sport_news(url_list_bbc)
skysports_dataset = sky_sports_news(url_list_sky_sports)

# process_datasets
print("Processing data for machine learning...")
X_vec, y = data_processing(bbc_dataset, skysports_dataset, True)

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

total_time = round((time.time() - start) / 60, 2)
print(f"Total runtime: {total_time} minutes")
