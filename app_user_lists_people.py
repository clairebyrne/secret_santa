import streamlit as st
from streamlit_extras.let_it_rain import rain

# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

# Page configuration
st.set_page_config(page_title="Byrne's Secret Santa Christmas 2025", page_icon="🎄")

# Run snowfall animation
run_snow_animation()

st.header(f"Byrne's Secret Santa Christmas 2025! 🎄", anchor=False)
st.markdown("![Alt Text](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjB3b2FodmRjNW5tdWhsZGtzdWozZGlhbmF4NmtoZGZubnJseGtrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HBMCmtsPEUShG/giphy.gif)")


people_count = st.number_input('How many people are there?', min_value=3)

prompts = ['person' + str(x) for x in range(1,people_count+1)]

get_peeps = [st.text_input(x) for x in prompts]

import random

def draw(peeps):
    selected = random.choice(peeps)
    return selected 

def remove_from_list(peeps, remove_us):
    valid_peeps = peeps.copy()
    for person in remove_us:
        if person in valid_peeps: valid_peeps.remove(person)
    return valid_peeps

exclusions = {'Aaron': 'Jen',
              'Jen': 'Aaron',
              'David': 'Aisling',
              'Aisling': 'David',
              'Keith': 'Marcelina',
              'Marcelina': 'Keith',
              'Angela': 'Eric',
              'Eric': 'Angela'}

st.write(f'These combinations are excluded in this draw: {exclusions}')

drawn = []

if st.button('Draw!'):
    all_peeps = get_peeps.copy()
    selectors = all_peeps.copy()
    for i in selectors:
        exclude = exclusions.get(i)
        if exclude is not None:
            remove = [i] + [exclude] + drawn
        else:
            remove = [i] + drawn
        valid_for_selection = remove_from_list(all_peeps, remove)
        this_selection = draw(valid_for_selection)
        st.write('\n'*3)
        st.write(f'{i} is gifting to {this_selection}')
        drawn.append(this_selection)
