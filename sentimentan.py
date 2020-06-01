import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from processing import main as processed


def most_active_users(df):
    # Number of messages per author
    author_counts = df['Author'].value_counts()
    most_active_authors = author_counts.head(15)

    # Plot and save graph
    plt.figure()
    most_active_authors.plot.barh()
    plt.xlabel("Individual Messages")
    plt.title("Most Active Members")
    plt.savefig("most_active.png",dpi=300, bbox_inches = "tight")



def main():
    df = processed()
    #most_active_users(df)
    media_messages_df = df[df['Message'] == 'image omitted']
    print(media_messages_df)


if __name__ == "__main__":
    main()
