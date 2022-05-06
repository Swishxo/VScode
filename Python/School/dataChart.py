#import library
import csv
import pandas as pd

data = pd.read_csv("sr_ss_clean.csv", delimiter="\t")


print(data)