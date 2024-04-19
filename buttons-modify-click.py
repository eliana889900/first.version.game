from tkinter import *

# putting 'dummy' because in the code below, the buttons are binded to an event
# but the number of the button starts at 1 (button_number = 1)
# if we don't put anything in the list, the index (1) would be out of range
button_list = ['dummy']


class button_box:
    # NOTE : "button" here is not equal to the buttons created further down 
    # in the code : I could put a diff name and it would still work
    
    # The __init__ function runs itself when an object (in this case, the objects
    # are : self, button, ID_number) from the class is created
    def __init__(self, button, ID_number):
        # .self => binds ID_number (instance/variable in button_box class)
        # to ID_number (attribute)
        self.ID_number = ID_number
        # same here, attributing button(attribute) to button(variable) using .self
        self.button = button

    def clicked(self, event):
        # when "clicked", the text below will be printed
        print(f'You pressed button number {self.ID_number}')
        # when "clicked", the clicked button is configured/edited :
        self.button.config(text=int(self.ID_number)+1)
        # the text it contains is added 1 to (int for integer)
        self.ID_number += 1
        # then, the button number is edited too


# create a window
root = Tk()

button_number = 1
for y in range(5):   # create the rows
    for x in range(9):   # create the columns
        # create the buttons
        button = Button(width=5, height=3, text=button_number, highlightcolor="red")
        # configure/edit the created button
        button.config(relief='solid', borderwidth=1)
        # place the buttons in row = y and column = x 
        # .grid() -> in grid disposition, not packed ( .pack() )
        button.grid(row=y, column=x)
        # add the button to the list of buttons, using the button_box function
        # it's adding a tuple to the list:
        #      button        --becomes--> button 
        #      button_number --becomes--> ID_number 
        #                    (bc we're using the button_box function)
        # button: name of the button
        # button_number:  initially 1, adding 1 in each iteration
        button_list.append(button_box(button, button_number))
        # linking the button.clicked to event
        # event : <Button-1> = left click
        # button : in button_list, the button corresponding to button_number
        button.bind('<Button-1>', button_list[button_number].clicked)
        # adding 1 to button_number (so that EACH button has a 
        # DISTINCT identification)
        button_number += 1

mainloop()
