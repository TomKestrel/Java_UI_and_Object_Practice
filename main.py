import tkinter as tk


root = tk.Tk()                      # this line will actually "create" the first GUI panel screen we will look at

root.title("My GUI")                # the title name of our GUI screen
root.geometry("400x300")            # sets the size of our GUI screen

def click():
    print("button has been clicked")
    window2 = tk.Toplevel(root)     #  Toplevel() is a specific class in the Tkinter module that is already included when you import tkinter.
                                    # It is used to create a new, independent window in your application, separate from the main window (root),
                                    # but still part of the same application.
    window2.title("2nd window")
    window2.geometry("400x400")
    label2 = tk.Label(window2, text = "This is the 2nd window")     # likewise Label() is also another method that came from the Tkinter module
    label2.pack(pady=20)
    topPanel = tk.Frame(window2, bg = "lightblue", height = 50, width = 50) # Frame() is another method to create panels
    topPanel.pack (side = "top") # fill = "both", expand = True

button = tk.Button(root, text = "Click Me!", command = click)    # creating a button
button.pack(pady=20)                                    # adding the button to the gui window
                                                        # "pady:" This stands for "padding on the y-axis." It adds space both above and below the widget,
                                                        # effectively creating vertical space between the widget and other elements in the window.
                                                        # the 20 means "by 20 pixels"

root.mainloop()                     #The root.mainloop() at the end of the script is what keeps the window open and responsive.
                                    # Without it, the window would open and then immediately close as the script finishes executing.


