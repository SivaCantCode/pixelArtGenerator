
---

# Simple Pixel Art Generator

This project is a simple pixel art generator created using Python and the Pygame library. It allows users to draw pixel art on a grid, choose from various colors, and save their artwork as an image file.

## Features

- Draw pixel art on a customizable grid.
- Select different colors for drawing.
- Change brush size.
- Undo the last few steps.
- Clear the grid.
- Save the artwork as a PNG file.

## Requirements

- Python 3.x
- Pygame library
- PySimpleGUI library

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/).

2. Install the required libraries using pip:
    ```bash
    pip install pygame pysimplegui
    ```

3. Clone this repository or download the project files.

## Usage

1. Navigate to the directory containing the project files.

2. Run the `pixel_art_generator.py` file:
    ```bash
    python pixel_art_generator.py
    ```

3. A window will open where you can draw your pixel art.

## Controls

- **Left Click**: Draw on the grid with the selected color and brush size.
- **Buttons**:
  - **Color Buttons**: Select different colors for drawing.
  - **S1**: Set brush size to 1.
  - **S2**: Set brush size to 3.
  - **S3**: Set brush size to 5.
  - **Erase**: Change the drawing color to the background color (erase).
  - **Clear**: Clear the entire grid.
  - **Undo**: Undo the last few steps (up to the set limit).
  - **Save**: Save the current artwork as a PNG file.

## Code Overview

- `init_grid(rows, cols, color)`: Initializes the grid with the specified color.
- `draw_grid(win, grid, drawRows=True, drawCols=True)`: Draws the grid on the window.
- `draw(win, grid, buttons, drawRows=True, drawCols=True, drawButtons=True)`: Draws the entire window, including the grid and buttons.
- `get_row_col_from_pos(pos)`: Gets the row and column from the mouse position.
- `update_grid(_row, _col)`: Updates the grid with the selected drawing color and brush size.
- `Button`: Class representing a button in the GUI.

## Customization

- **Grid Size**: Change the value of `ROWS` and `COLS` to set the number of rows and columns in the grid.
- **Toolbar Height**: Adjust `TOOLBAR_HEIGHT` to change the height of the toolbar.
- **Background Color**: Modify `BG_COLOR` to change the background color of the grid.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The project uses the [Pygame](https://www.pygame.org/) library for creating the GUI.
- The project uses the [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) library for pop-up dialogs.

---

Feel free to customize this README further to suit your project's specific needs.