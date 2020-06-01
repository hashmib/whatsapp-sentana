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


def most_image_content(df):
    image_messages_df = df[df['Message'] == 'image omitted']

    author_images_count = image_messages_df['Author'].value_counts()
    highest_author = author_images_count.head(15)

    # Plot and save graph
    plt.figure()
    highest_author.plot.barh()
    plt.xlabel("Images/Memes")
    plt.title("Most Images Sent")
    plt.savefig("most_active_images.png",dpi=300, bbox_inches = "tight")


def most_audio_content(df):
    audio_messages_df = df[df['Message'] == 'audio omitted']

    author_audio_count = audio_messages_df['Author'].value_counts()
    highest_author = author_audio_count.head(15)

    # Plot and save graph
    plt.figure()
    highest_author.plot.barh()
    plt.xlabel("Voice Notes")
    plt.title("Most VNs Sent")
    plt.savefig("most_active_vns.png",dpi=300, bbox_inches = "tight")


def busiest_day(df):
    plt.figure()
    df['Date'].value_counts().head(10).plot.barh()
    plt.xlabel("Messages")
    plt.title("Busiest Days")
    plt.savefig("busiest_days.png",dpi=300, bbox_inches = "tight")



def sort_by_jbh(df):
    jbh_df = df[df['Message'].str.contains("jbh", na=False, case=False)]
    jbh_count = jbh_df['Author'].value_counts()
    jbh_count_ranked = jbh_count.head(10)

    plt.figure()
    jbh_count_ranked.plot.barh()
    plt.xlabel("Messages")
    plt.title("Messages by jbh")
    plt.savefig("jbh_count.png", dpi=300, bbox_inches = "tight")

def textMessageData(df):
    # Remove all media content
    media_df = df[df['Message'].str.contains("omitted")]
    txt_msg_df = df.drop(media_df.index)
    
    # Analysis Functions
    #busiest_day(txt_msg_df)
    #sort_by_jbh(df)


def main():
    df = processed()
    #most_active_users(df)
    #most_image_content(df)
    #most_audio_content(df)
    
    textMessageData(df)

if __name__ == "__main__":
    main()
