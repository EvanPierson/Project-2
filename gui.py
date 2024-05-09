from tkinter import *
import logic


class GUI:
    def __init__(self, window) -> None:
        """
        Sets up the GUI application
        """
        self.window = window

        # Title labels and input window
        self.input1_label = Label(window, text='Enter set of coordinates:')
        self.input1_label.pack()

        self.entry1 = Entry(window)
        self.entry1.pack()

        self.transport_label = Label(window, text='Select mode of transport:')
        self.transport_label.pack()

        # Radio buttons to determine mode of transport
        self.var = StringVar()
        self.var.set('Drive')

        self.drive_radio = Radiobutton(window, text='Drive', variable=self.var, value='Drive')
        self.drive_radio.pack()

        self.fly_radio = Radiobutton(window, text='Fly', variable=self.var, value='Fly')
        self.fly_radio.pack()

        # Radio buttons to determine number of coordinates
        self.coord_var = IntVar()
        self.coord_var.set(4)

        self.four_coords_radio = Radiobutton(window, text='4 Coordinates', variable=self.coord_var, value=4)
        self.four_coords_radio.pack()

        self.six_coords_radio = Radiobutton(window, text='6 Coordinates', variable=self.coord_var, value=6)
        self.six_coords_radio.pack()

        # Calculate button and the outputs
        self.calculate_button = Button(window, text='Calculate', command=self.calculation)
        self.calculate_button.pack()

        self.distance_output_label = Label(window, text='')
        self.distance_output_label.pack()

        self.driving_output_label = Label(window, text='')
        self.driving_output_label.pack()

        self.flying_output_label = Label(window, text='')
        self.flying_output_label.pack()

    def calculation(self) -> None:
        try:
            coords = self.entry1.get().split(',')

            if len(coords) >= 6:
                multi_distance_str = logic.distance_three_points(coords)
                self.distance_output_label.config(text=multi_distance_str)
            else:
                mode_source = logic.distance_two_points(coords)

                distance_result_str = f'Distance = {mode_source["distance"]:.2f} km'
                self.distance_output_label.config(text=distance_result_str)

                transport = self.var.get()

                if transport == 'Drive':
                    driving_result_str = f'Driving = {mode_source["driving"]:.2f} hours'
                    self.driving_output_label.config(text=driving_result_str)
                else:
                    flying_result_str = f'Flying = {mode_source["flying"]:.2f} hours'
                    self.flying_output_label.config(text=flying_result_str)

            self.entry1.delete(0, END)

        except Exception as e:

            if self.coord_var.get() == 4 and len(coords) != 4:
                return self.distance_output_label.config(text='Invalid number of coordinates. Please enter 4 '
                                                              'coordinates.')

            if self.coord_var.get() == 6 and len(coords) != 6:
                return self.distance_output_label.config(text='Invalid number of coordinates. Please enter 6 '
                                                              'coordinates.')

            self.distance_output_label.config(text='Invalid coordinates.')
