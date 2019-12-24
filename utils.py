_FIELDS = ('SR NO.', 'NAME', 'WEBSITE', 'TECHNOLOGIES')

def pretty_print_results(results):
    print("-" * 215)
    print('{:^8s}{:^70s}{:^60s}{:^80s}'.format(*_FIELDS))
    print("-" * 215)
    for org in enumerate(results):
        print('{num:<8}{name:<70s}{website:<60s}{technologies}'.format(num=org[0], **org[1])) 


def print_org_data(org):
    print(f"Name: {org['name']}\n")
    print(f"Website: {org['website']}\n")
    print(f"Technologies: {org['technologies']}\n")
    print(f"Description: {org['description']}\n")
