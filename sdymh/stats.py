# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

def generate_headcount_table(values):
    values.sort()
    
    value_titles = []
    headcounts: dict = {}
    
    for value in values:
        if value not in value_titles:
            value_titles.append(value)    

        count = 1
        try:
            count = headcounts[value] + 1
        except KeyError:
            pass

        headcounts.update({value: count})
    
    value_titles.append("total")

    print("value\t\t|", end=" ")
    for title in value_titles:
        print(f"{title}\t|", end=" ")
    
    print("\nheadcount\t|", end=" ")

    total = 0
    for key in headcounts:
        r = headcounts[key]
        print(f"{r}\t|", end=" ")
        total += r
    
    print(f"{total}\t|")
