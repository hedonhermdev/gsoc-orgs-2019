import json
from utils import *

with open('orgs-19.json', 'r') as file:
    organizations = json.load(file)

tech = input("Name of technology: ")

if tech:
    results = [org for org in filter(lambda x: tech in x['technologies'], organizations)]
else:
    results = organizations

pretty_print_results(results)

