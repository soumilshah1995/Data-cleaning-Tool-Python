__Author__ = "soumil shah"
__Verion__ = "0.0.1"
__Email__ = "soumil.shah@budderfly.com"

"""
Problem Statments:  We need to Automate Data cleaning to removes Null Values
Solution:           Python script to select file it will drop all null values and create a new csv File 
                    Later more Functionality can be added 
"""

try:

    from tkinter import filedialog
    from tkinter import ttk
    from tkinter import *
    import pandas as pd
except Exception as e:
    print("Some Modules are Missing {}".format(e))


class Master(object):

    def __init__(self):
        self.root = Tk()

    @property
    def __open_dialog(self):
        """
        This FUnction is Provate
        Open Dialog Box
        :return: None
        """
        self.root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV File ","*.csv"),("all files","*.*")))
        self.filename = self.root.filename
        print (self.filename)
        return self.filename

    def clean_data(self):
        """
        Drops the Null values and 0
        :return: New csv File
        """
        self.filename = self.__open_dialog
        df = pd.read_csv(self.filename, na_values=[0,"0"])
        Data_CLeaned = df.dropna()

        Data_CLeaned.to_csv("Cleaned_Data.csv")
        self.__alert_popup(title="Complete", message="New Csv file has been created",path="Thanks for using  Software ")

    def __alert_popup(self, title="", message="", path=""):
        """Generate a pop-up window for special messages."""

        self.root.title(title)
        w = 400     # popup window width
        h = 200     # popup window height
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = message
        m += '\n'
        m += path
        w = Label(self.root, text=m, width=120, height=10)
        w.pack()
        b = Button(self.root, text="OK", command=self.root.destroy, width=10)
        b.pack()
        mainloop()

if __name__ == "__main__":
    obj = Master()
    obj.clean_data()
