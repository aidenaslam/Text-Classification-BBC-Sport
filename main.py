
## add run time
## implement logs
## unit testing
# create environment

# scrape data
bbc_dataset = bbc_sport_news(url_list)
skysports_dataset = sky_sports_news(url_list)

# merge datasets
dataset_combined = pd.concat([bbc_dataset,skysports_dataset])

# process_datasets

# Build machine learning models

# cross validation

# confusion matrix

