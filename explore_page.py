import tkinter as tk
from PIL import Image, ImageTk
import os

class ExplorePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.canvas = tk.Canvas(self, bg="#f8f7f3")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f8f7f3")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)


########################################################################


        top_frame = tk.Frame(self.scrollable_frame, bg="#f8f7f3", height=400)
        top_frame.grid(row=0, column=0, sticky="ew", pady=(20, 10), padx=200)
    
        top_frame.grid_columnconfigure(0, weight=3)  
        top_frame.grid_columnconfigure(1, weight=1)  
        top_frame.grid_columnconfigure(2, weight=1)  
    
        paper_backs = self.create_paperback(top_frame)
        paper_backs.grid(row=0, column=0, padx=(5, 0), pady=(10, 10), sticky="nsew")
        paper_backs.config(width=400, height=400)
        paper_backs.grid_propagate(False)
        
        
###################################################################

#    R I G H T     F R A M E
        
        
        
        right_frame = tk.Frame(top_frame, bg="#e9e6e6", width=200, height=400)
        right_frame.grid(row=0, column=1, padx=(0), pady=(10, 10), sticky="nsew")
        right_frame.grid_propagate(False)
        
        
        new_paperbacks = tk.Label(right_frame, bg="#e9e6e6", text="84 New Paperbacks to Take with you Everywhere", font=("Helvetica", 17, "bold"), fg="#382110", 
        anchor="w", 
        wraplength=190, 
        justify="left" )
        new_paperbacks.pack(pady=(10, 10), fill="x")
        
        released_paperbacks = tk.Label(right_frame, bg="#e9e6e6", text="This one is pretty straightforward: Below we've gathered recently released paperback editions of popular books from across all genres, ficition, and nonficition. Each of the...", 
        font=("Helvetica", 12), 
        fg="#382110", 
        anchor="w", 
        wraplength=170, 
        justify="left" )
        released_paperbacks.pack(pady=(20, 10), fill="x")
        
        likes_comments = tk.Label(right_frame, text="53 likes · 7 comments", bg="#e9e6e6", font=("Helvetica", 7, "bold"), fg="gray", anchor="sw")
        likes_comments.pack(pady=(50, 10), fill="x")

        author_summers = tk.Label(
            top_frame, 
            text="The Author's of Summer's Scariest Books Share \nTheir Horror Picks\n\n\n\nThe 60 Most Popular \nScience Fiction Books\nof the Past 3 Years \n\n\n\nA Look Back at Five Years of Historical Fiction Hits \n\n\nMore news & interviews >",
            font=("Helvetica", 13), 
            bg="#f8f7f3", 
            fg="#382110", 
            anchor="w", 
            wraplength=230, 
            justify="left"
        )
        author_summers.grid(row=0, column=2, padx=(0), pady=(20, 0), sticky="n")

        trending_frame = tk.Frame(self.scrollable_frame, bg="#f8f7f3")
        trending_frame.grid(row=1, column=0, sticky="ew", pady=5, padx=200)


###################################################################

#    B O O K    R O W     C O N T E N T



        trending = tk.Label(trending_frame, bg="#f8f7f3", text="Trending with Goodreads members", font=("Helvetica", 14, "bold"), fg="black", anchor="w")
        trending.grid(row=0, column=0, sticky="w")
    
        move_label = tk.Label(trending_frame, bg="#f8f7f3", text="< >", font=("Helvetica", 16, "bold"), fg="black", anchor="e")
        move_label.grid(row=0, column=1, padx=(400, 0))
    
        books_container = tk.Frame(self.scrollable_frame, bg="#f8f7f3")
        books_container.grid(row=2, column=0, sticky="ew", pady=(10, 0), padx=195)
    
        book_data = [
            {"title": "Quicksilver", "author": "Callie Hart", "rating": "⭐4.39", "image_path": r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\Quicksilver.png"},
            {"title": "Powerless", "author": "Lauren Roberts", "rating": "⭐4.24", "image_path": r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\powerless.png"},
            {"title": "Reckless", "author": "Lauren Roberts", "rating": "⭐4.15", "image_path": r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\reckless.png"},
            {"title": "Onyx Storm", "author": "Rebecca Yarros", "rating": "⭐4.34", "image_path": r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\onyx.png"},
            {"title": "The Briar Club", "author": "Kate Quinn", "rating": "⭐4.39", "image_path": r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\briar.png"},
            ]
    
        for i, book in enumerate(book_data):
            book_panel = self.create_book_panel(books_container, book)
            book_panel.grid(row=0, column=i, padx=(0 if i == 0 else 5, 0))


###################################################################

#    F O O T E R    B E C A U S E    O F    G R I D 


    
        footer_frame = tk.Frame(self.scrollable_frame, bg="#ece6d9", height=200)
        footer_frame.grid(row=4, column=0, pady=(60, 0), sticky="ew")
        footer_frame.grid_propagate(False)
        
        footer_inner = tk.Frame(footer_frame, bg="#ece6d9", height=400)
        footer_inner.grid(row=0, column=0, sticky="ew", pady=(20, 10), padx=200)
 
        footer_left_company = tk.Label(footer_inner, text="COMPANY", font=('Open Sans', 10, "bold"), bg="#ece6d9", anchor="nw")
        footer_left_company.grid(row=0, column=0, pady=0, sticky="w")
        footer_about = tk.Label(footer_inner, text="About Us", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_about.grid(row=1, column=0, pady=0, sticky="w")
        footer_Car = tk.Label(footer_inner, text="Careers", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_Car.grid(row=2, column=0, pady=0, sticky="w")
        footer_terms = tk.Label(footer_inner, text="Terms", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_terms.grid(row=3, column=0, pady=0, sticky="w")       
        footer_privacy = tk.Label(footer_inner, text="Privacy", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_privacy.grid(row=4, column=0, pady=0, sticky="w")        
        footer_iba = tk.Label(footer_inner, text="Interest Based Ads", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_iba.grid(row=5, column=0, pady=0, sticky="w")        
        footer_ap = tk.Label(footer_inner, text="Ad Preferences", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_ap.grid(row=6, column=0, pady=0, sticky="w")       
        footer_help = tk.Label(footer_inner, text="Help", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_help.grid(row=7, column=0, pady=0, sticky="w")
        
        footer_left_work = tk.Label(footer_inner, text="WORK WITH US ", font=('Open Sans', 10, "bold"), bg="#ece6d9", anchor="nw")
        footer_left_work.grid(row=0, column=1, pady=0, padx=60, sticky="w")
        footer_author = tk.Label(footer_inner, text="Authors", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_author.grid(row=1, column=1, pady=3, padx=60, sticky="w")
        footer_adver = tk.Label(footer_inner, text="Advertise", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_adver.grid(row=2, column=1, pady=3, padx=60, sticky="w")
        footer_aa = tk.Label(footer_inner, text="Authors & ads blog", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_aa.grid(row=3, column=1, pady=3, padx=60, sticky="w")
        footer_api = tk.Label(footer_inner, text="API", font=('Open Sans', 8), bg="#ece6d9", anchor="nw")
        footer_api.grid(row=4, column=1, pady=3, padx=60, sticky="w")
        
        footer_left_work = tk.Label(footer_inner, text="CONNECT", font=('Open Sans', 10, "bold"), bg="#ece6d9", anchor="nw")
        footer_left_work.grid(row=0, column=2, pady=0, padx=20, sticky="w")
        
        
        footer_download = tk.Label(footer_inner,text="Download on the\nAPP STORE ", font=('Open Sans', 10, "bold"), bg="black", fg="white", anchor="nw")
        footer_download.grid(row=0, column=3, pady=0, padx=(110, 5), sticky="e")
        footer_copyright = tk.Label(footer_inner, text="@ 2024 Goodreads, Inc.", font=("Helvetica", 8), bg="#ece6d9", anchor="nw",  wraplength=230, justify="left")
        footer_copyright.grid(row=1, column=3, pady=0, padx=(110, 5), sticky="e")
        
        footer_google = tk.Label(footer_inner,text="Get it on\nGOOGLE PLAY ", font=('Open Sans', 10, "bold"), bg="black", fg="white", anchor="nw")
        footer_google.grid(row=0, column=4, pady=0, padx=10, sticky="e")
        
   
###################################################################

#     F U N T I O N S

        
        
        def create_round_button(parent, width, height, color, command):
            canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0, bg="#ece6d9")
            padding = 4
            canvas.create_oval(padding, padding, width-padding, height-padding, fill=color, outline="")
            canvas.bind("<Button-1>", lambda event: command())
            return canvas
        
        def on_circle_click(color):
            print(f"Clicked {color} button")

        
        def create_circle_buttons(parent_frame):
            circle_frame = tk.Frame(parent_frame, bg="#ece6d9")
            circle_frame.grid(row=1, column=2, sticky="nsew")

            colors = ["#d2c9af", "#d2c9af", "#d2c9af", "#d2c9af", "#d2c9af"]
            for i, color in enumerate(colors):
                button = create_round_button(circle_frame, width=40, height=40, color=color, 
                                             command=lambda c=color: on_circle_click(c))
                button.grid(row=1, column=2, padx=4)
                

    def create_paperback(self, parent):
        panel = tk.Frame(parent, bg="#f8f7f3", width=450, height=450)
        panel.grid_propagate(False)
        try:
            image_path = r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\paperback.png"
            original_image = Image.open(image_path)
    
            image = original_image.resize((450, 450), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(panel, image=photo, bg="#f8f7f3")
            image_label.image = photo  
            image_label.pack(fill="both", expand=True)
        except Exception as e:
            print(f"Error loading image: {e}")
            placeholder = tk.Label(panel, text="Image Not Found", bg="lightgray", width=25, height=15)
            placeholder.pack(fill="both", expand=True)

        return panel

    def create_book_panel(self, parent, book_info):
        panel = tk.Frame(parent, bg="#f8f7f3", width=200, height=200)
        panel.grid_propagate(False)
        try:
            image_path = os.path.normpath(book_info['image_path'])
            original_image = Image.open(image_path)
            
            aspect_ratio = original_image.width / original_image.height
            
            new_height = 234
            new_width = int(new_height * aspect_ratio)
            
            image = original_image.resize((new_width, new_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(panel, image=photo, bg="#f8f7f3")
            image_label.image = photo
            image_label.pack(pady=(0, 5), padx=(0, 0))
        except Exception as e:
            print(f"Error loading image: {e}")
            placeholder = tk.Label(panel, text="Image Not Found", bg="lightgray", width=25, height=15)
            placeholder.pack(pady=(0, 5))

        title_label = tk.Label(panel, text=book_info['title'], font=("Helvetica", 12, "bold"), bg="#f8f7f3", wraplength=145)
        title_label.pack()

        author_label = tk.Label(panel, text=book_info['author'], font=("Helvetica", 10), bg="#f8f7f3")
        author_label.pack()

        rating_label = tk.Label(panel, text=f"Rating: {book_info['rating']}", font=("Helvetica", 10), bg="#f8f7f3")
        rating_label.pack()

        return panel
        

#---------------------------------------------------
root = tk.Tk()
root.geometry("1200x1200")
root.configure(bg="white")
explore_page = ExplorePage(root)
explore_page.pack(fill="both", expand=True)
root.mainloop()
