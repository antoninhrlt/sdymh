# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

def generate_frequency_table(values):
    values.sort()
    
    value_titles = []
    frequencies: dict = {}
    
    for value in values:
        if value not in value_titles:
            value_titles.append(value)    

        count = 1
        try:
            count = frequencies[value] + 1
        except KeyError:
            pass

        frequencies.update({value: count})
    
    value_titles.append("total")

    print("value\t\t|", end=" ")
    for title in value_titles:
        print(f"{title}\t|", end=" ")
    
    print("\nfrequency\t|", end=" ")

    total = 0
    for key in frequencies:
        r = frequencies[key]
        print(f"{r}\t|", end=" ")
        total += r
    
    print(f"{total}\t|")
