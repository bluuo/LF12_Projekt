from RequestHandler import requestSpeedCameras
from JsonParser import JsonParser
import customtkinter
import tkintermapview

def main():
    
    def onSubmit():
        location_value, plz_value = getEntryValues()
        response = requestSpeedCameras(location_value)
        parser = JsonParser(response)
        elements = parser.extract_elements()
        elementCount =  len(elements)
        clearTextbox()
        insertTextbox(elementCount)
    
    def getEntryValues():
        return location_entry.get(), plz_entry.get()
    
    def insertTextbox(outputString):
        textbox.insert("0.0", str(outputString) + "\n")
        
    def clearTextbox():
        textbox.delete('1.0', "end")

    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.title("Blitzer Tracker")
    root.resizable(True, True)  # Allow window resizing

    # Add padding around everything
    padding = 10

    # Create a frame to contain all widgets with padding
    main_frame = customtkinter.CTkFrame(root)
    main_frame.grid(row=0, column=0, padx=padding,
                    pady=padding, sticky='nwse')
    # Configure row and column weights to make them resizable
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    title_label = customtkinter.CTkLabel(
        main_frame, text="Blitzer Tracker", font=("Helvetica", 24))
    title_label.grid(row=0, column=0, padx=padding,
                        pady=padding, sticky='nwse')

    location_frame = customtkinter.CTkFrame(main_frame)
    location_frame.grid(row=1, column=0, padx=padding,
                        pady=padding, sticky='nwse')

    location_label = customtkinter.CTkLabel(
        location_frame, text="Ort", font=("Helvetica", 16), height=20)
    location_label.grid(row=0, column=0, padx=padding,
                        pady=padding, sticky='nwse')

    location_entry = customtkinter.CTkEntry(location_frame)
    location_entry.grid(row=1, column=0, padx=padding,
                        pady=padding, sticky='nwse')

    plz_frame = customtkinter.CTkFrame(main_frame)
    plz_frame.grid(row=2, column=0, padx=padding,
                    pady=padding, sticky="nwse")

    plz_label = customtkinter.CTkLabel(
        plz_frame, text="PLZ", font=("Helvetica", 16))

    plz_label.grid(row=0, column=0, padx=padding,
                    pady=padding, sticky='nwse')

    plz_entry = customtkinter.CTkEntry(plz_frame)
    plz_entry.grid(row=1, column=0, padx=padding,
                    pady=padding, sticky='nwse')

    empty_label = customtkinter.CTkLabel(
        main_frame, text="")

    button = customtkinter.CTkButton(
        main_frame, text="Start", command=onSubmit)
    button.grid(row=4, column=0, padx=padding, pady=padding, sticky='nwse')

    textbox = customtkinter.CTkTextbox(main_frame)
    textbox.grid(row=0, column=1, rowspan=5, padx=padding,
                    pady=padding, sticky='nwse')

    map_widget = tkintermapview.TkinterMapView(
        main_frame, corner_radius=10, )
    map_widget.grid(row=0, column=2, rowspan=5,
                    padx=padding, pady=padding, sticky='nwse')
    # set current widget position and zoom
    map_widget.set_position(50.09677226088053, 8.645226816465373)  # Paris, France

    # Configure grid weights for main frame
    main_frame.grid_rowconfigure(3, weight=1)
    # main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=2)

    root.mainloop()
   
if __name__ == "__main__":
    main()