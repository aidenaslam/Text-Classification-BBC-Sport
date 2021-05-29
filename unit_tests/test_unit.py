import unittest   # The test framework

from parameters.project_parameters import url_list_bbc, url_list_sky_sports
from data_prep.scrape_data import bbc_sport_news, sky_sports_news
from data_prep.data_processing import data_processing, split_dataset
from modelling.build_models import (
    logistic_regression_model
    )
from evaluation.model_evaluation import cross_validation

class Unit_testing(unittest.TestCase):

    def test_cross_validation_accuracy_larger_than_80(self):
        bbc_dataset = bbc_sport_news(url_list_bbc)
        skysports_dataset = sky_sports_news(url_list_sky_sports)
        X_vec, y = data_processing(bbc_dataset, skysports_dataset, True)
        X_train, X_test, y_train, y_test = split_dataset(X_vec, y, 0.3)
        log_reg = logistic_regression_model(X_train, y_train)
        models = (('Logistic Reg (baseline)', log_reg ))
        cross_val = cross_validation(models, X_train, y_train, 10)
        
        self.assertTrue(cross_val.mean() > 0.75)

