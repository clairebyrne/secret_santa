import random

all_peeps = ['Aaron', 'David', 'Keith', 'Claire', 
            'Angela', 'Eric', 
            'Aisling', 'Jen', 'Marcelina']


def draw(peeps):
    selected = random.choice(peeps)
    return selected 

def remove_from_list(peeps, remove_us):
    valid_peeps = peeps.copy()
    for person in remove_us:
        if person in valid_peeps: valid_peeps.remove(person)
    return valid_peeps

selectors = all_peeps.copy()

exclusions = {'Aaron': 'Jen',
              'Jen': 'Aaron',
              'David': 'Aisling',
              'Aisling': 'David',
              'Keith': 'Marcelina',
              'Marcelina': 'Keith',
              'Angela': 'Eric',
              'Eric': 'Angela'}

drawn = []

for i in selectors:
    exclude = exclusions.get(i)
    if exclude is not None:
        remove = [i] + [exclude] + drawn
    else:
        remove = [i] + drawn
    valid_for_selection = remove_from_list(all_peeps, remove)
    this_selection = draw(valid_for_selection)
    print('\n'*3)
    print(f'{i} is gifting to {this_selection}')
    drawn.append(this_selection)
