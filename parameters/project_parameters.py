import os

# Define global font for EDA
font = {'family' : 'calibri',
        'weight' : 'normal',
        'size'   : 18}

url_list_bbc = [
        'https://www.bbc.co.uk/sport/football',
        'https://www.bbc.co.uk/sport/formula1',
        'https://www.bbc.co.uk/sport/cricket',
        'https://www.bbc.co.uk/sport/tennis'
        ]

url_list_sky_sports = [
        'https://www.skysports.com/football',
        'https://www.skysports.com/f1',
        'https://www.skysports.com/cricket',
        'https://www.skysports.com/tennis'
]

# Save outputs 
project_path = r'C:\Users\Aiden\Documents\Data_Science_Stuff\sf_Data_Science_Stuff\Projects\01_SportsNewsClassifier\final_code'
input_folder = "input_data"
output_folder = "outputs"
models_folder = "saved_models"
save_ouptuts = os.path.join(project_path, output_folder)
save_input = os.path.join(project_path, input_folder)
save_models = os.path.join(project_path, models_folder)