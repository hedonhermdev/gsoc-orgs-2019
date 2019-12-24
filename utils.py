FIELDS = ('NAME', 'WEBSITE', 'TECHNOLOGIES')

def pretty_print_results(results):
    print("-" * 215)
    print('{:^70s}{:^60s}{:^10s}'.format(*FIELDS))
    print("-" * 215)
    for org in results:
        print('{name:<70s}{website:<60s}{technologies}'.format(**org)) 
