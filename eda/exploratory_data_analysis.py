import matplotlib.pyplot as plt
import matplotlib as mpl

from final_code.parameters.project_parameters import font

def plot_num_headlines(dataset):
    """ plots bar graph of number of headlines per class """
    count = dataset.groupby(['Sport']).count()
    count = count.iloc[:,0]
    sport = ('cricket','f1','football','tennis')

    plt.bar(sport, count, color = 'tan')
    plt.ylabel('Number of headlines')
    mpl.rc('font', **font)
    plt.tight_layout()
    plt.savefig('01_EDA_Headline_Categories.png')
    plt.close()

    