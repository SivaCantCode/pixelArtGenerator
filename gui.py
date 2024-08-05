import PySimpleGUI as sg  # Importing the PySimpleGUI library

# Setting the theme for the window
sg.theme("Default1")

# Defining the font to be used for the GUI elements
font = ("Times New Roman", 12)

# Defining the layout of the window
layout = [
    [sg.Text('What canvas size do you want?', font=font)],  # Text prompt for the canvas size
    [sg.Slider(orientation='h', font=font, key='-SIZE-', resolution=10, range=(10, 100))],  # Slider to select the canvas size
    [sg.HorizontalSeparator()],  # Horizontal separator line
    [sg.Button('Submit', key="-SUBMIT-", font=font, size=(9, 1)),  # Submit button
     sg.Button('Exit', key="-EXIT-", font=font, size=(9, 1))],  # Exit button
]

# Creating the window with the specified layout and settings
window = sg.Window('Pixel_Art', layout, grab_anywhere=True, element_justification="c", resizable=True)

# Event loop to handle user interactions
while True:
    event, values = window.read()  # Read the events and values from the window
    if event == sg.WIN_CLOSED:  # If the window is closed, exit the loop
        break

    if event == "-SUBMIT-":  # If the Submit button is clicked
        x = int(values["-SIZE-"])  # Get the value from the slider and convert it to an integer
        break  # Exit the loop

    if event == "-EXIT-":  # If the Exit button is clicked
        break  # Exit the loop

window.close()  # Close the window
