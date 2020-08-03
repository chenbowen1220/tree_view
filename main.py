# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
from windows import wds_register


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("TreeView")
    root.geometry("1400x900")

    wds_register.RegisterGui(root)

    root.mainloop()

    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
