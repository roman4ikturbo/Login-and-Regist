import tkinter as tk
import tkinter.messagebox as messagebox

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Login, Register):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login and Register", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Login", command=lambda: controller.show_frame(Login))
        button.pack()

        button2 = tk.Button(self, text="Register", command=lambda: controller.show_frame(Register))
        button2.pack()




class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        name_label = tk.Label(self, text="Username:")
        name_label.pack()
        name_entry = tk.Entry(self)
        name_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self)
        password_entry.pack()

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Register", command=lambda: controller.show_frame(Register))
        button2.pack()

        button3 = tk.Button(self, text="Login", command=lambda: self.login(name_entry, password_entry, controller))
        button3.pack()

    def login(self, name_entry, password_entry, controller):
        username = name_entry.get()
        password = password_entry.get()

        with open("users.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")

        messagebox.showinfo("Successful Login", "You have successfully logged in!")

        controller.show_frame(StartPage)



class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Register", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        gmail_label = tk.Label(self, text="Gmail:")
        gmail_label.pack()
        gmail_entry = tk.Entry(self)
        gmail_entry.pack()

        name_label = tk.Label(self, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(self)
        name_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self)
        password_entry.pack()

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Login", command=lambda: controller.show_frame(Login))
        button2.pack()

        button3 = tk.Button(self, text="Regist", command=lambda: self.register(name_entry, password_entry, controller))
        button3.pack()

    def register(self, name_entry, password_entry, controller):
        name = name_entry.get()
        password = password_entry.get()

        with open("users.txt", "a") as file:
            file.write(f"Name: {name}, Password: {password}\n")

        messagebox.showinfo("Successful registration", "You have successfully registered!")

        controller.show_frame(StartPage)



app = SeaofBTCapp()
app.mainloop()