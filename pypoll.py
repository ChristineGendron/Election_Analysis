import csv, os
from email import header

from requests import head

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    print(headers)

    election_data.close()