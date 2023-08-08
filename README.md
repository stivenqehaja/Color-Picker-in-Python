-RGB and CMY Color Picker
This simple Python application utilizes the pyautogui and tkinter libraries to create a color picker that displays the RGB and CMY color values of the pixel under the cursor.

-How it Works
The script captures the current position of the mouse cursor using pyautogui and retrieves the pixel color at that position using the screenshot().getpixel() method. It then calculates the RGB and CMY color values and updates the labels in the GUI with the respective values. The GUI is built using the Tkinter library.

-Dependencies
Python 3.x
pyautogui
tkinter

-You can install the required dependencies using the following command:
  pip install pyautogui

-Usage
Make sure you have the required dependencies installed.
Run the script using the following command:
  python color_picker.py
A GUI window will appear displaying the current position of the cursor and the RGB and CMY color values of the pixel under the cursor.
Move the cursor around the screen to see real-time updates of the color values.

-Note
The script will update the color values every 100 milliseconds using the after() method to create a continuous color-picking experience.
The RGB values represent Red, Green, and Blue color components (0-255 range).
The CMY values represent Cyan, Magenta, and Yellow color components (0-255 range) and are calculated by subtracting the corresponding RGB values from 255.
Feel free to modify and enhance the code to suit your specific needs or integrate it into your projects. Happy coding!
