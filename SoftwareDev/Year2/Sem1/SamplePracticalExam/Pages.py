from tkinter import *
window = Tk()
window.geometry("280x580")


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # =====| Menus |=====
        menu1 = Menu(window)
        window.config(menu=menu1)
        # TODO - Make commands to swap between drivers and constructors
        menu1.add_command(label="Driver Standings", font=("arial", 12, "bold"), command=lambda: master.switch_frame(PageOne).pack())  # menu item
        menu1.add_command(label="Leaderboard", font=("arial", 12, "bold"), command=lambda: master.switch_frame(PageTwo).pack())
        # =====| End of Menus |=====

        Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        Button(self, text="Open page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()


class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
