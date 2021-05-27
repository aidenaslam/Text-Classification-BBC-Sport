from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix

#from modelling.build_models import logistic_regression_model, svm_model, random_forest_model, naive_bayes_model

# Define global font for EDA
font = {'family' : 'calibri',
        'weight' : 'normal',
        'size'   : 18}

# List models to run CV
models = []
models.append(('Logistic Reg (baseline)', logistic_regression_model ))
models.append(('SVM', SVM_model ))
models.append(('Random Forest', RF_model ))
models.append(('Naive Bayes', NB ))

def cross_validation(models, x, y, number_of_splits):
    """ Startified cross validation """
    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = StratifiedKFold(n_splits=number_of_splits, random_state=1)
        cv_results = cross_val_score(model, x, y, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

    plt.figure(figsize=(7,7))
    plt.xticks(fontsize=12)
    plt.yticks(fontsize = 12)
    plt.boxplot(results, labels=names)
    plt.ylabel('Accuracy', fontsize = 12)
    plt.title('10-fold cross-validation')
    plt.tight_layout()
    mpl.rc('font', **font)
    plt.savefig('02_CV_Models.png')
    plt.close()

def plot_confusion_matrix(best_model, x, y):
    """ Plot confusion matrix """
    fig, ax = plt.subplots(figsize=(8,8))
    disp = plot_confusion_matrix(best_model, x, y, ax=ax)
    plt.figure(figsize=(20,20))
    disp.ax_.set_title('Confusion Matrix')
    fig.savefig('03_Confusion_Matrix.png')
    plt.close()