import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightgrey")
        label = tk.Label(self, text="Main Page", bg="lightgrey", font=('Bold', 18))
        label.pack(pady=20)
        
        # Create an invisible area for clicking
        self.clickable_area = tk.Frame(self, width=400, height=300, bg="lightgrey", cursor="hand2")
        self.clickable_area.pack(fill="both", expand=True)
        self.clickable_area.bind("<Button-1>", self.go_to_home_page)

    def go_to_home_page(self, event):
        self.master.show_home_page()

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        label = tk.Label(self, text="Homeee Page", bg="white", font=('Bold', 18))
        label.pack(pady=20)
        
        # Create an invisible area for clicking
        self.clickable_area = tk.Frame(self, width=400, height=300, bg="white", cursor="hand2")
        self.clickable_area.pack(fill="both", expand=True)
        self.clickable_area.bind("<Button-1>", self.go_to_main_page)

    def go_to_main_page(self, event):
        self.master.show_main_page()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create frames for each page
        self.main_page = MainPage(self)
        self.home_page = HomePage(self)
        
        # Show the main page initially
        self.show_main_page()

    def show_main_page(self):
        self.home_page.pack_forget()
        self.main_page.pack(fill="both", expand=True)

    def show_home_page(self):
        self.main_page.pack_forget()
        self.home_page.pack(fill="both", expand=True)

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()