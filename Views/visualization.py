"""
Shichao Tian
Final project visualization files
"""
import matplotlib.pyplot as plt


def plot_park_counts(park_count):
    plt.figure(figsize=(10, 8))
    plt.bar(
        park_count.keys(), park_count.values(), color='blue', label='Parks')
    plt.title('Number of Parks in Each Neighbourhood')
    plt.xlabel('Neighbourhood')
    plt.ylabel('Number of Parks')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show(block=False)


def plot_graffiti_counts(graff_count):
    plt.figure(figsize=(10, 8))
    plt.bar(
        graff_count.keys(), graff_count.values(), color='red',
        label='Graffitis')
    plt.title('Number of Graffitis in Each Neighbourhood')
    plt.xlabel('Neighbourhood')
    plt.ylabel('Number of Graffitis')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show(block=False)


def plot_graffitis_near_parks(parks_instances, graffiti_instances, km):
    park_names = []
    graffiti_counts = []
    for park in parks_instances:
        park_names.append(park.name)
        graffiti_count = park.graffitis_within_km(graffiti_instances, km)
        graffiti_counts.append(graffiti_count)

    plt.figure(figsize=(25, 10))
    bars = plt.bar(
        park_names, graffiti_counts, color='purple',
        label=f'Graffitis within {km} km')
    plt.title(f'Number of Graffitis within {km} km of Each Park')
    plt.xlabel('Park Name')
    plt.ylabel('Number of Graffitis')
    plt.xticks(rotation=90)
    plt.tick_params(axis='x', labelsize=8)
    plt.legend()
    plt.tight_layout()
    plt.show(block=False)

    return bars
