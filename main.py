from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(root, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0,END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(END, content)
    root.title(f"Open file : {filepath}")
    
def save_file(root, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open (filepath, "w") as f:
        content = text_edit.gett(1.0, END)
        f.write(content)
    root.title(f"Open file : {filepath}")

root = Tk()
root.title("Notepad")
root.rowconfigure(0, minsize=400)
root.columnconfigure(1, minsize=500)

text_edit = Text(root, font="Helvatica 12")
text_edit.grid(row=0, column=1)

frame = Frame(root, relief=RAISED, bd=2)
save_button = Button(frame, text="Save",command= lambda: save_file(root, text_edit))
open_button = Button(frame, text="Open", command= lambda: open_file(root, text_edit))



save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
frame.grid(row=0 ,column=0, sticky="ns")


root.mainloop()