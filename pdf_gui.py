# GUI for pdf.py

# Imports
import tkinter as tk
from pdf_ops import *
from tkinter.filedialog import askopenfilename, askopenfilenames
import os

# Create Instance
window = tk.Tk()

# GUI Title
window.title('PDF Operations')

# Widgets


# Note that background button color is not supported for macOS
# btn = tk.Button(window, text="Execute", highlightbackground='#3E4149', fg="red", command=partial(function, args))
# btn.grid(column=1, row=0)




# Operation selection
window.op_selection = None
def change_op(selection):
	window.op_selection = selection

op_var = tk.IntVar()

label_1 = tk.Label(window, 
	text='Choose an operation', 
	width='40', 
	height='5', 
	anchor='w')

merge_btn = tk.Radiobutton(window, 
	text='Merge', 
	variable=op_var,
	value=1, 
	command=lambda: change_op(merge))

split_btn = tk.Radiobutton(window, 
	text='Split', 
	variable=op_var, 
	value=2, 
	command=lambda: change_op(split))


label_1.grid(column=0, 
	row=0, 
	padx=40, 
	pady=10)
merge_btn.grid(column=1, 
	row=0, 
	pady=10, 
	sticky='w')
split_btn.grid(column=1, 
	row=1, 
	pady=10, 
	sticky='w')



# File selection
window.paths = []

# d1 stores base names
window.d1 = {}

# d2 stores label objects
window.d2 = {}

# d3 stores button objects
window.d3 = {}

window.counter_len = 1
window.counter = 3


def choose_file():
	fname = askopenfilename()
	window.paths.append(fname)
	key = 'x' + str(window.counter_len)
	
	window.d1[key] = os.path.splitext(os.path.basename(fname))[0]

	window.d2[key] = tk.Label(window,
		text=window.d1[key], 
		width='40', 
		height='5', 
		anchor='w')

	window.d2[key].grid(column=1, 
		row=window.counter, 
		pady=20,)

	window.d3[key] = tk.Button(window,
		text='Delete', 
		command=lambda: remove_path(key, fname, window.d2[key], window.d3[key]))

	window.d3[key].grid(
		column=1, 
		row=window.counter + 1, 
		pady=5, 
		sticky='w')

	window.counter_len += 1
	window.counter += 1

def remove_path(key, fname, object1, object2):
	window.paths.remove(fname)
	object1.grid_forget()
	object2.grid_forget()
	del window.d1[key]
	del window.d2[key]
	del window.d3[key]



label_2 = tk.Label(window, 
	text='Choose files to operate on', 
	width='40', 
	height='5', 
	anchor='w')
file_btn = tk.Button(window, 
	text='Choose files', 
	command=choose_file)


label_2.grid(column=0, 
	row=2, 
	padx=40, 
	pady=20)
file_btn.grid(column=1, 
	row=2, 
	pady=20, 
	sticky='w')




# Execution
def ready_state():
	window.paths = []

def executor():
	if window.op_selection == split and len(window.paths) == 1:
		split(window.paths[0])
		ready_state()
	elif window.op_selection == merge and len(window.paths) >= 2:
		merge(window.paths)
		ready_state()
	else:
		window.paths = []



label_3 = tk.Label(window, 
	text='Choose files to operate on', 
	width='40', 
	height='5', 
	anchor='w')

ex_btn = tk.Button(window, 
	text='Execute',  
	command=executor)


label_3.grid(column=0, 
	row=5, 
	padx=40, 
	pady=20)
ex_btn.grid(column=1, 
	row=5, 
	pady=20, 
	sticky='w')

# Window Size
window.geometry('700x500')

# Start GUI/Create Main Loop
window.mainloop()

