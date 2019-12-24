import json
from utils import *

with open('orgs-19.json', 'r') as file:
    organizations = json.load(file)

while True:
    print("\n")
    print("Enter the name of a technology to search for (Enter 'exit' to exit)")
    user_input = input(">")
    if user_input == 'exit':
        break
    else:
        if user_input:
            tech_name = user_input
        else:
            tech_name = ""

    if tech_name:
        results = [org for org in filter(lambda x: tech_name in x['technologies'], organizations)]
    else:
        results = organizations

    pretty_print_results(results)

    if results:
        while True:
            print("\n")
            print("Enter the Sr No. of an organization to know more about it. Press Enter to exit")
            try:
                org_number = int(input(">"))
                print_org_data(results[org_number])
            except ValueError:
                break

    print("\n")
    print("Search again? (yN)")
    ans = input(">")
    if not (ans[0] == 'y' or ans[0] == 'Y'):
        break

