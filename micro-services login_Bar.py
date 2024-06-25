import tkinter


window = tkinter.Tk()
window.title("login form")
window.geometry('420x550')
# window.configure(bg='#333328')

#geometry widget manager are pack, place, grid
label = tkinter.label(window, text="login")
label.grid(row=0, column=0)

#creating widget
logn_label = tkinter.Label(window, text="login")
login_button = tkinter.button(window, text="Login")
username_label = tkinter.label(window, text="Username")
username_entry = tkinter.Entry(window)
password_entry = tkinter.Entry(window, show="*")
password_label = tkinter.label(window, tex ="password")



#placing widget onscreen

 
login_label.grid = tkinter.button(window, text="Login")
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)






















window.mainloop()
