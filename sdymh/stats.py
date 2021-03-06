# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

def generate_frequency_table(values):
    values.sort()
    
    value_titles = []
    headcounts: dict = {}
    frequencies: dict = {}
    
    for value in values:
        if value not in value_titles:
            value_titles.append(value)    

        count = 1
        try:
            count = frequencies[value] + 1
        except KeyError:
            pass

        headcounts.update({value: count})
        frequencies.update({value: count})

    value_titles.append("total")

    print("value\t\t|", end=" ")
    for title in value_titles:
        print(f"{title}\t|", end=" ")
    
    # Headcount row
    print("\nheadcount\t|", end=" ")

    total_headcounts = 0
    for key in headcounts:
        r = headcounts[key]
        print(f"{r}\t|", end=" ")

        total_headcounts += r
    
    print(f"{total_headcounts}\t|")

    # Frequency row
    print("frequency\t|", end=" ")

    for key in frequencies:
        r = headcounts[key]
        print(f"{r}/{total_headcounts}\t|", end=" ")

    print(f"1\t|") # total frequencies is always 1

    # To generate the table by yourself
    return (values, headcounts)


# Example :
# You have 15 roses and it represents 60% percent of the flowers (total)
# 60/100 x = 15 <=> 0.6x = 15 <=> x = 15/0.6 = 25
# So, you have 25 flowers in total
def total_from_percentage(percentage, equal, total_id="total", part_id="x", output=False):
    total = 100 / percentage * equal
    if output:
        print(f"{percentage}% of {total_id} = {equal} {part_id}")
        print(f"{total_id} = {total}")
    return total


# 100/400 = 1/4 = 0.25 = 25/100 = 25%
def proportion_to_percentage(n, total):
    return (n / total) * 100

# t = (Vf - Vi) / Vi
def evolution_rate(initial, final):
    return (final - initial) / initial
