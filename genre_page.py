import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class GenrePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.canvas = tk.Canvas(self, bg="#f8f7f3")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f8f7f3")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.pack(fill="both", expand=True)
        self.container_frame = tk.Frame(self.scrollable_frame, bg="#f8f7f3")
        self.container_frame.pack(fill="both", expand=True)
        
        self.main_content = tk.Frame(self.container_frame, bg="#f8f7f3")
        self.main_content.pack(side="left", fill="both", expand=True)
        
        self.more_info = tk.Frame(self.container_frame, bg="#f8f7f3", width=200)
        self.more_info.pack(side="right", fill="y")
        self.more_info.pack_propagate(False)
    
    
###################################################################

#    R I G H T     F R A M E

    

        fav_genre = tk.Label(self.more_info, text="MY FAVORITE GENRES", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
        fav_genre.pack(pady=(70, 5), padx=(10, 0), anchor="w")
        
        separator_frame = tk.Frame(self.more_info, height=1, bg="grey")
        separator_frame.pack(pady=(0, 5), fill="x")
        
        selec = tk.Label(self.more_info, text="Not selected yet.", font=("Helvetica", 8), bg="#f8f7f3", anchor="w", justify="left")
        selec.pack(pady=(0, 10), padx=(10, 0), anchor="w")
        
        browse = tk.Label(self.more_info, text="BROWSE", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
        browse.pack(pady=(5, 5), padx=(10, 0), anchor="w")
        
        separator_frame = tk.Frame(self.more_info, height=1, bg="grey")
        separator_frame.pack(pady=(0, 5), fill="x")
        
        browse_frame = tk.Frame(self.more_info, bg="#f8f7f3", width=300)
        browse_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        browse_canvas = tk.Canvas(browse_frame, bg="#f8f7f3", highlightthickness=0)
        browse_scrollbar = tk.Scrollbar(browse_frame, orient="vertical", command=browse_canvas.yview)
        browse_scrollable_frame = tk.Frame(browse_canvas, bg="#f8f7f3")
        
        browse_scrollable_frame.bind(
            "<Configure>",
            lambda e: browse_canvas.configure(
                scrollregion=browse_canvas.bbox("all")
            )
        )
        
        browse_canvas.create_window((0, 0), window=browse_scrollable_frame, anchor="nw")
        browse_canvas.configure(yscrollcommand=browse_scrollbar.set)
        
        browse_canvas.pack(side="left", fill="both", expand=True)
        browse_scrollbar.pack(side="right", fill="y")
        
        self.create_browse_list(browse_scrollable_frame)
       

###################################################################

#    T O P     F R A M E

        

        self.top_frame = tk.Frame(self.main_content, bg="#f8f7f3", width=800)
        self.top_frame.pack(pady=(20, 10), padx=(200, 20), fill="both", expand=True)
        
        genre_label = tk.Label(self.top_frame, text="Genres",font=("Helvetica", 15, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
        genre_label.pack(pady=(10, 5), padx=(0,500))
    
        search_frame = tk.Frame(self.top_frame, bg="#eeeeee", height=20, width=600)
        search_frame.pack(pady=(5, 0), padx=(0), fill="x")
        
        search_bar2 = tk.Entry(search_frame, highlightthickness=1,fg="gray", highlightbackground="#b9ad97", highlightcolor="#b9ad97")
        search_bar2.pack(pady=(10,1), padx=(10, 110), fill="x")
        search_bar2.bind("<Return>", self.on_search)
        search_bar2.insert(0, 'Find a genre by name')
        search_bar2.bind('<FocusIn>', self.on_entry_click)
        search_bar2.bind('<FocusOut>', self.on_focusout)
        
        search_button = tk.Button(search_frame, text="Find Genre", bg="#eeeeee", highlightthickness=1, highlightbackground="#b9ad97", highlightcolor="#b9ad97")
        search_button.pack(pady=(0, 10), side="left", padx=(10, 90))
 
        
 
 ############################################################       
  

      
        image_paths = [
            r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\row1.png",
            r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\row2.png",
            r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\row3.png",
            r"C:\Users\kimmy\OneDrive\Desktop\School folder\OOprogramming FinalProject\Images\row4.png",
        ]

        self.create_genre_section("FANTASY", image_paths[0], "More fantasy...")
        self.create_genre_section("NONFICTION", image_paths[1], "More nonfiction...")
        self.create_genre_section("GRAPHIC NOVELS & COMICS", image_paths[2], "More graphic novels & comics...")
        self.create_genre_section("MYSTERY & THRILLER", image_paths[3], "More mystery & thriller...")

        print("GenrePage initialized")
        
        self.create_footer()
        





###################################################################

#     F U N T I O N S





    def create_footer(self):
        footer_frame = tk.Frame(self.scrollable_frame, bg="#ece6d9")
        footer_frame.pack(side="bottom", fill="x", expand=True)
        
        footer_inner = tk.Frame(footer_frame, bg="#ece6d9", width=1500)
        footer_inner.pack(pady=(20, 10), padx=20, fill="x", expand=True)
        
        footer_inner.columnconfigure(0, weight=1)
        footer_inner.columnconfigure(1, weight=1)
        footer_inner.columnconfigure(2, weight=1)
        footer_inner.columnconfigure(3, weight=1)
        footer_inner.columnconfigure(4, weight=1)
        
        company_frame = tk.Frame(footer_inner, bg="#ece6d9")
        company_frame.grid(row=0, column=0, sticky="nw")
        
        footer_left_company = tk.Label(company_frame, text="COMPANY", font=('Open Sans', 10, "bold"), bg="#ece6d9", anchor="nw")
        footer_left_company.pack(anchor="w")
        company_items = ["About Us", "Careers", "Terms", "Privacy", "Interest Based Ads", "Ad Preferences", "Help"]
        for item in company_items:
            tk.Label(company_frame, text=item, font=('Open Sans', 8), bg="#ece6d9", anchor="nw").pack(anchor="w")
        
        work_frame = tk.Frame(footer_inner, bg="#ece6d9")
        work_frame.grid(row=0, column=1, sticky="nw", padx=(20, 0))
        
        footer_left_work = tk.Label(work_frame, text="WORK WITH US", font=('Open Sans', 10, "bold"), bg="#ece6d9", anchor="nw")
        footer_left_work.pack(anchor="w")
        work_items = ["Authors", "Advertise", "Authors & ads blog", "API"]
        for item in work_items:
            tk.Label(work_frame, text=item, font=('Open Sans', 8), bg="#ece6d9", anchor="nw").pack(anchor="w")
        
        footer_connect = tk.Label(footer_inner, text="CONNECT", font=('Open Sans', 10, "bold"), bg="#ece6d9", anchor="nw")
        footer_connect.grid(row=0, column=2, sticky="nw", padx=(20, 0))
        
        footer_download = tk.Label(footer_inner, text="Download on the\nAPP STORE", font=('Open Sans', 10, "bold"), bg="black", fg="white", anchor="center", padx=10, pady=5)
        footer_download.grid(row=0, column=3, sticky="ne", padx=(0, 10))
        
        footer_google = tk.Label(footer_inner, text="Get it on\nGOOGLE PLAY", font=('Open Sans', 10, "bold"), bg="black", fg="white", anchor="center", padx=10, pady=5)
        footer_google.grid(row=0, column=4, sticky="ne")
        
        footer_copyright = tk.Label(footer_inner, text="© 2024 Goodreads, Inc.", font=("Helvetica", 8), bg="#ece6d9", anchor="w")
        footer_copyright.grid(row=1, column=3, columnspan=2, sticky="e", pady=(10, 0))

    def create_browse_list(self, parent):
        genres = [
            ("Art", "Manga"),
            ("Biography", "Memoir"),
            ("Business", "Music"),
            ("Chick Lit", "Mystery"),
            ("Children's", "Nonfiction"),
            ("Christian", "Paranormal"),
            ("Classics", "Philosophy"),
            ("Comics", "Poetry"),
            ("Contemporary", "Psychology"),
            ("Cookbooks", "Religion"),
            ("Crime", "Romance"),
            ("Ebooks", "Science"),
            ("Fantasy", "Science Fiction"),
            ("Fiction", "Self Help"),
            ("Gay and Lesbian", "Suspense"),
            ("Graphic Novels", "Spirituality"),
            ("Historical Fiction", "Sports"),
            ("History", "Thriller"),
            ("Horror", "Travel"),
            ("Humor and Comedy", "Young Adult")
        ]

        for i, (genre, genre2) in enumerate(genres):
            genre_label = tk.Label(parent, text=genre, anchor='w', font=("Helvetica", 8), bg="#f8f7f3", fg="#458677")
            genre_label.grid(row=i, column=0, padx=10, pady=2, sticky='w')
            genre2_label = tk.Label(parent, text=genre2, anchor='e',  font=("Helvetica", 8), bg="#f8f7f3", fg="#458677")
            genre2_label.grid(row=i, column=1, padx=4, pady=2, sticky='e')

        more_genres = tk.Label(parent, text="More genres....", bg="#f8f7f3", font=("Helvetica", 9, "bold"), cursor="hand2", fg="#458677")
        more_genres.grid(row=len(genres), column=0, columnspan=3, padx=(20,0), pady=(10, 2), sticky='e')
        
        more_genres.bind("<Enter>", lambda e: e.widget.config(fg="blue"))
        more_genres.bind("<Leave>", lambda e: e.widget.config(fg="#33544c"))

    def create_genre_section(self, genre_name, image_path, more_text):
        genre_label = tk.Label(self.top_frame, text=genre_name, bg="#f8f7f3", fg="#3b3746", font=("Helvetica", 11, "bold"), anchor="w")
        genre_label.pack(pady=(20, 10), padx=(0,0), anchor="w")

        separator_frame = tk.Frame(self.top_frame, height=1, bg="grey")
        separator_frame.pack(pady=(0, 10), fill="x")
        
        image_row = tk.Frame(self.top_frame, bg="#f8f7f3")
        image_row.pack(pady=(10, 10), fill="x")
        
        image_panel = self.create_paperback(image_row, image_path)
        image_panel.pack(padx=(0, 10), side="left")
        
        more_label = tk.Label(self.top_frame, text=more_text, bg="#f8f7f3", font=('Bold', 9), cursor="hand2")
        more_label.pack(pady=(5, 20), padx=(0, 10), anchor="e")
        
        more_label.bind("<Enter>", lambda e: e.widget.config(fg="blue"))
        more_label.bind("<Leave>", lambda e: e.widget.config(fg="black"))

        print(f"Genre section created: {genre_name}")

    def create_paperback(self, parent, image_path):
        panel = tk.Frame(parent, bg="#f8f7f3", width=550, height=200)
        panel.pack_propagate(False)
        try:
            original_image = Image.open(image_path)
            image = original_image.resize((550, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(panel, image=photo, bg="#f8f7f3")
            image_label.image = photo  
            image_label.pack(fill="both", expand=True)
            print(f"Image loaded: {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
            placeholder = tk.Label(panel, text="Image Not Found", bg="lightgray", width=25, height=15)
            placeholder.pack(fill="both", expand=True)
        return panel
    
    def on_entry_click(self, event):
        if event.widget.get() == 'Search books':
            event.widget.delete(0, "end")  
            event.widget.insert(0, '')  
            event.widget.config(fg='gret')

    def on_focusout(self, event):
        if event.widget.get() == '':
            event.widget.insert(0, 'Search books')
            event.widget.config(fg='gray')

    def on_search(self, event):
        query = event.widget.get().strip()
        if query:
            print(f"Searching for: {query}")
        else:
            print("Search term is empty")




#---------------------------------------------------

root = tk.Tk()
root.geometry("1200x1500")
root.configure(bg="#f8f7f3")
genre_page = GenrePage(root)
genre_page.pack(fill="both", expand=True)
root.mainloop()
