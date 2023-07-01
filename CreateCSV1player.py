import csv
import tkinter as tk
from tkinter import filedialog

def save_to_csv():
    filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if filename:
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Player", "DOB", "Percentage"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(11):
                entry_name = entry_names[i].get()
                entry_dob = entry_dobs[i].get()
                entry_percentage = entry_percentages[i].get()

                writer.writerow({"Player": entry_name, "DOB": entry_dob, "Percentage": entry_percentage})

        print(f"CSV file '{filename}' saved successfully.")

window = tk.Tk()
window.title("Player Data Entry")

label_title = tk.Label(window, text="Enter Player Information")
label_title.pack()

entry_names = []
entry_dobs = []
entry_percentages = []

frame_heading = tk.Frame(window)
frame_heading.pack()

label_number_heading = tk.Label(frame_heading, text="Player")
label_number_heading.pack(side=tk.LEFT)

label_name_heading = tk.Label(frame_heading, text="Name")
label_name_heading.pack(side=tk.LEFT)

label_dob_heading = tk.Label(frame_heading, text="DOB")
label_dob_heading.pack(side=tk.LEFT)

label_percentage_heading = tk.Label(frame_heading, text="Percentage")
label_percentage_heading.pack(side=tk.LEFT)

for i in range(11):
    frame = tk.Frame(window)
    frame.pack()

    label_number = tk.Label(frame, text=f"Player {i+1}:")
    label_number.pack(side=tk.LEFT)

    entry_name = tk.Entry(frame)
    entry_name.pack(side=tk.LEFT)
    entry_names.append(entry_name)

    entry_dob = tk.Entry(frame)
    entry_dob.pack(side=tk.LEFT)
    entry_dobs.append(entry_dob)

    entry_percentage = tk.Entry(frame)
    entry_percentage.pack(side=tk.LEFT)
    entry_percentages.append(entry_percentage)

button_save = tk.Button(window, text="Save to CSV", command=save_to_csv)
button_save.pack()

window.mainloop()
