import json
import tkinter
from RequestHandler import requestSpeedCameras
from JsonParser import JsonParser
import customtkinter
import tkintermapview

def main():
    
    def onSubmit():
        location_value = getEntryValues()
        response = requestSpeedCameras(location_value)
        json_formatted_str = json.dumps(response, indent=2)
        parser = JsonParser(response)
        speedCameras = parser.parse()
        sumLat = 0
        sumLon = 0
        for speedCamera in speedCameras:
            lat = speedCamera.get('lat')
            lon = speedCamera.get('lon')
            sumLat = sumLat + lat
            sumLon = sumLon + lon
            
            map_widget.set_marker(lat, lon)
            map_widget.set_zoom(12)
            
        averageLat = sumLat / len(speedCameras)
        averageLon = sumLon / len(speedCameras)
        map_widget.set_position(averageLat, averageLon)  
        
        
        elementCount =  len(speedCameras)
        
        blitzer_count_entry_label.configure(text = str(elementCount))
        clearTextbox()
        insertTextbox(json_formatted_str)
    
    def getEntryValues():
        return location_entry.get()

    def insertTextbox(outputString):
        response_textbox.insert("0.0", str(outputString) + "\n")
        
    def clearTextbox():
        response_textbox.delete('1.0', "end")

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.title("Blitzer Tracker")
    root.geometry("1400x900")
    root.resizable(True, True)

    outsidePadding = 20
    padding = 10

    main_frame = customtkinter.CTkFrame(root)
    main_frame.grid(row=0, column=0, padx=outsidePadding,pady=outsidePadding, sticky='nwse')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    title_label = customtkinter.CTkLabel(main_frame, text="Blitzer Tracker", font=("Helvetica", 24))
    title_label.grid(row=0, column=0, padx=padding,pady=padding+10, sticky='nwse')

    location_frame = customtkinter.CTkFrame(main_frame)
    location_frame.grid(row=1, column=0, padx=padding,pady=padding, sticky='nwse')
    location_label = customtkinter.CTkLabel(location_frame, text="Ort", font=("Helvetica", 16), height=20)
    location_label.grid(row=0, column=0, padx=padding,pady=padding, sticky='nwse')
    location_entry = customtkinter.CTkEntry(location_frame, width=200)
    location_entry.grid(row=1, column=0, padx=padding,pady=padding, sticky='nwse')
    location_entry.bind('<Return>', lambda event: onSubmit())

    # plz_frame = customtkinter.CTkFrame(main_frame)
    # plz_frame.grid(row=2, column=0, padx=padding,pady=padding, sticky="nwse")
    # plz_label = customtkinter.CTkLabel(plz_frame, text="PLZ", font=("Helvetica", 16))
    # plz_label.grid(row=0, column=0, padx=padding,pady=padding, sticky='nwse')
    # plz_entry = customtkinter.CTkEntry(plz_frame)
    # plz_entry.grid(row=1, column=0, padx=padding,pady=padding, sticky='nwse')

    # empty_label = customtkinter.CTkLabel(main_frame, text="")

    button = customtkinter.CTkButton(main_frame, text="Start", font=("Helvetica", 16), command=onSubmit)
    button.grid(row=2, column=0, padx=padding, pady=padding, sticky='nwse')

    result_frame = customtkinter.CTkFrame(main_frame)
    result_frame.grid(row=1, column=1, rowspan=1, padx=padding,pady=padding, sticky="nsew")
    result_label = customtkinter.CTkLabel(result_frame, text="Ergebnis", font=("Helvetica", 24), height=20)
    result_label.grid(row=0, column=0,padx=padding,pady=padding, sticky='nsew')
    blitzer_count_title_label = customtkinter.CTkLabel(result_frame, text="Anzahl Blitzer", font=("Helvetica", 16), height=20, width=400)
    blitzer_count_title_label.grid(row=0, column=0, padx=padding,pady=padding, sticky='nsew')
    blitzer_count_entry_label = customtkinter.CTkLabel(result_frame, text="", font=("Helvetica", 16), height=20)
    blitzer_count_entry_label.grid(row=1, column=0, padx=padding,pady=padding, sticky='nsew')

    # response_label = customtkinter.CTkLabel(main_frame, text="Response", font=("Helvetica", 16), height=20)
    # response_label.grid(row=2, column=1, padx=padding,pady=padding, sticky='nwse')
    response_textbox = customtkinter.CTkTextbox(main_frame, width=400) 
    response_textbox.grid(row=2, column=1, rowspan=6, padx=padding, pady=padding, sticky="nwse")

    map_widget = tkintermapview.TkinterMapView(main_frame, corner_radius=10)
    map_widget.grid(row=1, column=2, rowspan=5,padx=padding, pady=padding, sticky='nwse')
    # set current widget position and zoom
    map_widget.set_position(50.09677226088053, 8.645226816465373)  # Paris, France

    main_frame.grid_rowconfigure(3, weight=1)
    # main_frame.grid_columnconfigure(0, weight=1)
    # main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=2)

    root.mainloop()
   
if __name__ == "__main__":
    main()