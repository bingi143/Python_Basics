'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
import matplotlib.pyplot as plt

def create_histogram(data, bins=10, title='Histogram', x_label='Value', y_label='Frequency'):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()


data=[3,4,5,7,7,8,9,7,1,4,5,6,8,9]
create_histogram(data, bins=5, title='Sample Histogram', x_label='Integers', y_label='Count')

