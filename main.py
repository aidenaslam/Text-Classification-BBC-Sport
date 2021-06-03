import time
from modelling_evaluation.modelling import model_eval

start = time.time()

model_eval()

total_time = round((time.time() - start) / 60, 2)
print(f"Total runtime: {total_time} minutes")
