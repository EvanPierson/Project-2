import tkinter as tk
from geopy.distance import geodesic


class Distance_Calculator():

    def __init__(self, master):
        self.master = master
        master.title('Distance Calculator')

        self.input_label = tk.Label(master, text='Enter Coords in sequence: (Lat1, Long1, Lat2, Long2)')
        self.input_label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.distance_output_label = tk.Label(master, text='')
        self.distance_output_label.pack()

    def distance(self):

        try:
            coords = self.entry.get().split(',')
            coords = [float(coord) for coord in coords]
            start = (coords[0], coords[1])
            end = (coords[2], coords[3])

            distance = geodesic(start, end).kilometers

            distance_result_str = f'Distance = {distance:.2f} km'
            self.distance_output_label.config(text=distance_result_str)

        except Exception as e:
            self.distance_output_label.config(text='Invalid coordinates.')


root = tk.Tk()
app = Distance_Calculator(root)
root.mainloop()

# https://zzzcode.ai/python/code-generator -> Origin of code
