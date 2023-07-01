import pandas as pd
import matplotlib.pyplot as plt

def generate_graph(players):
    names = players["Name"]
    percentages = players["Performance Percentage"]

    plt.bar(names, percentages)
    plt.xlabel("Players")
    plt.ylabel("Performance Percentage")
    plt.title("Player Performance")
    plt.xticks(rotation=45)
    plt.show()

def main():
    file_name = "player.csv"

    try:
        players_data = pd.read_csv(file_name)
        generate_graph(players_data)
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please make sure the file exists in the current directory.")

if __name__ == "__main__":
    main()
