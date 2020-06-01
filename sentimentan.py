import pandas as pd
import matplotlib.pyplot as plt
from processing import main as processed

def main():
    df = processed()    
    author_value_counts = df['Author'].value_counts() # Number of messages per author
    top_10_author_value_counts = author_value_counts.head(10) # Number of messages per author for the top 10 most active authors
    top_10_author_value_counts.plot.barh() # Plot a bar chart using pandas built-in plotting apis

    plt.show(block=True)

if __name__ == "__main__":
    main()
