import customtkinter
import os
from tkinter.filedialog import askdirectory
import tkinter
import tkintermapview

class frontend:
    @staticmethod        
    def loadUi():
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()
        root.title("Blitzer Tracker")
        root.resizable(True, True)  # Allow window resizing
        # root.geometry("+20+20+20+20")  # Add 20 pixels of padding to the top and left sides

# Configure grid weights
        # root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(4, weight=1)

        # root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=2)  # This column will take 2/3 of the window width

        title_label = customtkinter.CTkLabel(root, text="Blitzer Tracker", font=("Helvetica", 24))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky='nwse')

        location_frame = customtkinter.CTkFrame(root)
        location_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nwse')
        # location_frame.grid_propagate(False)  # Prevent frame from resizing
        
        location_label = customtkinter.CTkLabel(location_frame, text="Ort", font=("Helvetica", 16), height=20)
        location_label.grid(row=0, column=0, padx=10, pady=10, sticky='nwse')

        location_entry = customtkinter.CTkEntry(location_frame)
        location_entry.grid(row=1, column=0, padx=10, pady=10, sticky='nwse')

        plz_frame = customtkinter.CTkFrame(root)
        plz_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nwse")

        plz_label = customtkinter.CTkLabel(plz_frame, text="PLZ", font=("Helvetica", 16))
        plz_label.grid(row=0, column=0, padx=10, pady=10, sticky='nwse')

        plz_entry = customtkinter.CTkEntry(plz_frame)
        plz_entry.grid(row=1, column=0, padx=10, pady=10, sticky='nwse')

        button = customtkinter.CTkButton(root, text="Start", command=frontend.on_submit)
        button.grid(row=3, column=0, padx=10, pady=10, sticky='nwse')
        

        textbox = customtkinter.CTkTextbox(root)
        textbox.grid(row=1, column=1, rowspan=4, padx=10, pady=10, sticky='nwse')

        map_widget = tkintermapview.TkinterMapView(root, corner_radius=10)
        map_widget.grid(row=1, column=2, rowspan=4, padx=20, pady=10, sticky='nwse')

        root.mainloop()

    @staticmethod
    def on_submit():
        print("test")