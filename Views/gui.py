"""
Shichao Tian
Final project GUI files
"""
import tkinter as tk
from tkinter import simpledialog, messagebox
from utils.functions import data_get
from utils.create_instances import (create_park_instances,
                                    create_graffiti_instances)
from models.graffiti import Graffiti
from models.park import Park
from Views.visualization import (plot_park_counts, plot_graffiti_counts,
                                 plot_graffitis_near_parks)
import matplotlib.pyplot as plt


class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Park and Graffiti Analysis Dashboard")
        self.geometry("800x600")
        self.parks, self.graffitis = self.load_data()
        self.intro_screen()

    def load_data(self):
        parks_data, graffs_data = data_get()
        parks = create_park_instances(parks_data)
        graffitis = create_graffiti_instances(graffs_data)

        return parks, graffitis

    def intro_screen(self):
        intro_label = tk.Label(
            self, text="Bonjour! Let's explore the relationship between parks"
            "and graffiti!", font=('Helvetica', 16))
        intro_label.pack(expand=True)
        self.after(2000, intro_label.destroy)
        self.after(2000, self.main_menu)

    def main_menu(self):
        self.clear_screen()
        label = tk.Label(self, text="Shall we look at the park or the graffiti"
                         "first?", font=('Helvetica', 16))
        label.pack(expand=True)

        park_button = tk.Button(
            self, text='Park', command=self.handle_park)
        park_button.pack(pady=10)

        graffiti_button = tk.Button(
            self, text='Graffiti',
            command=self.handle_graffiti)
        graffiti_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", command=self.quit_app)
        quit_button.pack(pady=10)

    def handle_park(self):
        self.clear_screen()
        plot_park_counts(Park.park_in_neighbour(self.parks))
        self.follow_up()

    def handle_graffiti(self):
        self.clear_screen()
        plot_graffiti_counts(Graffiti.graffiti_in_neighbour(self.graffitis))
        self.follow_up()

    def follow_up(self):
        self.clear_screen()
        label = tk.Label(
            self, text="Let's explore the amount of graffiti near the park.",
            font=('Helvetica', 16))
        label.pack(expand=True)

        yes_button = tk.Button(self, text='Yes', command=self.request_distance)
        yes_button.pack(pady=10)

        no_button = tk.Button(self, text="No", command=self.main_menu)
        no_button.pack(pady=10)

        quit_button = tk.Button(self, text='Quit', command=self.quit_app)
        quit_button.pack(pady=10)

    def request_distance(self):
        self.clear_screen()
        distance = simpledialog.askfloat(
            "Distance", "How many kilometers we want to explore?",
            minvalue=0.01)
        if distance is not None and distance > 0:
            self.show_data(distance)
        else:
            messagebox.showerror(
                "Error", "Invalid input,"
                " please enter a valid positive number.")
            self.request_distance()

    def show_data(self, km):
        self.clear_screen()
        plot_graffitis_near_parks(self.parks, self.graffitis, km)
        self.back_to_menu()

    def back_to_menu(self):
        label = tk.Label(
            self, text='Back to main menu?', font=('Helvetica', 16))
        label.pack(expand=True)

        menu_button = tk.Button(self, text='Main Menu', command=self.main_menu)
        menu_button.pack(pady=10)

        quit_button = tk.Button(self, text='Quit', command=self.quit_app)
        quit_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def quit_app(self):
        plt.close('all')
        score = simpledialog.askstring(
            "Feedback", "Thank you for the test. Do you like my final project?"
            "\nWhat score would you give me?")
        if score:
            messagebox.showinfo(
                "Thank you", "Good to know! Have a nice day! : )")
            self.after(10, self.destroy)
        else:
            self.after(10, self.destroy)


# if __name__ == '__main__':
#     app = DashboardApp()
#     app.mainloop()
