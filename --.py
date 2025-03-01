import tkinter as tk
from tkinter import messagebox  
from Pages import genre_page
from Pages import home_page
from Pages import explore_page
from main.app import MainApp


root = tk.Tk()
root.title("GoodReads.com")
root.geometry("1200x1100")
root.resizable(False, True)

#############################################

def create_round_button(parent, width, height, color, command):
    canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0, bg="#ece6d9")
    padding = 4
    canvas.create_oval(padding, padding, width-padding, height-padding, fill=color, outline="")
    canvas.bind("<Button-1>", lambda event: command())
    return canvas

def create_book_icon(parent, size=30):
    icon = tk.Canvas(parent, width=size, height=size, bg="#f4f1ea", highlightthickness=0)
    icon.create_rectangle(5, 5, size-5, size-5, fill="#b9ad97", outline="")
    icon.create_line(10, 10, size-10, 10, fill="white", width=2)
    icon.create_line(10, 15, size-10, 15, fill="white", width=2)
    icon.create_line(10, 20, size-15, 20, fill="white", width=2)
    return icon

def on_entry_click(event):
    if search_bar.get() == 'Search books':
        search_bar.delete(0, "end")  # Delete all the text in the entry
        search_bar.insert(0, '')  # Insert blank for user input
        search_bar.config(fg='grey')

def on_focusout(event):
    if search_bar.get() == '':
        search_bar.insert(0, 'Search books')
        search_bar.config(fg='grey')


header_frame = tk.Frame(root, bg="#b6f47d", width=1200, height=35)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="Read Your Way Around America: A Book For Every State >", bg="#b6f47d", font=('Open Sans', 10))
header_label.place(relx=0.5, rely=0.5, anchor="center")

def show_explore_page():
    for widget in main_content_frame.winfo_children():
        widget.destroy()
    explore_page_content = explore_page.ExplorePage(main_content_frame)
    explore_page_content.pack(fill="both", expand=True)

def show_home_page():
    for widget in main_content_frame.winfo_children():
        widget.destroy()
    home_page_content = home_page.HomePage(main_content_frame)
    home_page_content.pack(fill="both", expand=True)

def show_genre_page():
    for widget in main_content_frame.winfo_children():
        widget.destroy()
    genre_page_content = genre_page.GenrePage(main_content_frame)
    genre_page_content.pack(fill="both", expand=True)

def on_menu_select(item):
    print(f"{item} selected")

def show_main_app():
    for widget in main_content_frame.winfo_children():
        widget.destroy()
    main_app_content = MainApp(main_content_frame)
    main_app_content.pack(fill="both", expand=True)

def create_goodreads_button(parent_frame):
    def on_goodreads_click():
        show_main_app()
        goodreads_button.config(relief="flat")

    goodreads_button = tk.Button(parent_frame, text="GoodReads", bg="#ece6d9", activebackground='#382110', activeforeground='white', font=('bold', 18), relief="flat", command=on_goodreads_click)
    goodreads_button.grid(row=0, column=0, sticky="nsew")

def create_home_button(parent_frame):
    home_button = tk.Button(parent_frame, text="Home", relief="flat", bg="#ece6d9", activebackground='#382110', activeforeground='white', bd=0, command=show_main_app)
    home_button.grid(row=0, column=1, sticky="nsew")


def create_mybooks_button(parent_frame):
    mybooks_button = tk.Menubutton(parent_frame, text="My Books", relief="flat", bg="#ece6d9", activebackground='#382110', activeforeground='white', bd=0)
    mybooks_button.grid(row=0, column=2, sticky="nsew")

def create_browse_button(parent_frame):
    browse_button = tk.Menubutton(parent_frame, text="Browse \\/", relief="flat", bg="#ece6d9", activebackground='#382110', activeforeground='white', bd=0)
    browse_button.grid(row=0, column=3, sticky="nsew")
    
    browse_menu = tk.Menu(browse_button, tearoff=0)
    browse_menu.add_command(label="Recommendations", command=lambda: on_menu_select("Recommendations"))
    browse_menu.add_command(label="Choice Awards", command=lambda: on_menu_select("Choice Awards"))
    browse_menu.add_command(label="Giveaways", command=lambda: on_menu_select("Giveaways"))
    browse_menu.add_command(label="New Releases", command=lambda: on_menu_select("New Releases"))
    browse_menu.add_command(label="Lists", command=lambda: on_menu_select("Lists"))
    browse_menu.add_command(label="Explore", command=show_explore_page)
    browse_menu.add_command(label="News & Interviews", command=lambda: on_menu_select("News & Interviews"))
    browse_menu.add_command(label="Genre", command=show_genre_page)
    browse_button.config(menu=browse_menu)

def create_community_button(parent_frame):
    community_button = tk.Menubutton(parent_frame, text="Community \\/", relief="flat", bd=0, bg="#ece6d9", activebackground='#382110', activeforeground='white')
    community_button.grid(row=0, column=4, sticky="nsew")
    
    community_menu = tk.Menu(community_button, tearoff=0)
    community_menu.add_command(label="Groups", command=lambda: on_menu_select("Groups"))
    community_menu.add_command(label="Discussions", command=lambda: on_menu_select("Discussions"))
    community_menu.add_command(label="Quotes", command=lambda: on_menu_select("Quotes"))
    community_menu.add_command(label="Ask the Author", command=lambda: on_menu_select("Ask the Author"))
    community_menu.add_command(label="People", command=lambda: on_menu_select("People"))
    community_button.config(menu=community_menu)

def create_separator(parent_frame, x_pos):
    separator = tk.Frame(parent_frame, width=1200, bg="grey")
    separator.place(x=x_pos, y=80, height=10)

def create_circle_buttons(parent_frame):
    circle_frame = tk.Frame(parent_frame, bg="#ece6d9")
    circle_frame.grid(row=0, column=6, sticky="nsew")

    colors = ["#d2c9af", "#d2c9af", "#d2c9af", "#d2c9af", "#d2c9af"]
    for i, color in enumerate(colors):
        button = create_round_button(circle_frame, width=40, height=40, color=color, 
                                     command=lambda c=color: on_circle_click(c))
        button.grid(row=0, column=i, padx=4)

def on_circle_click(color):
    print(f"Clicked {color} button")

# Create a frame to hold the menu buttons
menu_frame = tk.Frame(root, bg="#ece6d9", height=35)
menu_frame.pack(fill="x")

create_separator(menu_frame, 80)

# Create and configure menu buttons
create_goodreads_button(menu_frame)
create_home_button(menu_frame)
create_mybooks_button(menu_frame)
create_browse_button(menu_frame)
create_community_button(menu_frame)

# Create a frame to hold the main content
main_content_frame = tk.Frame(root, bg="#f8f7f3", width=1200, height=1000)
main_content_frame.place(x=0, y=80, width=1200, height=940)

def perform_search(query):
    print(f"Searching for: {query}")
    messagebox.showinfo("Search Results", f"You searched for: {query}")

def on_search(event=None):
    query = search_bar.get().strip()
    if query:
        perform_search(query)
    else:
        messagebox.showwarning("Empty Search", "Please enter a search term.")

search_barr = tk.Entry(menu_frame, highlightthickness=1, highlightbackground="#b9ad97", highlightcolor="#b9ad97")
search_barr.grid(row=0, column=5, sticky="nsew", pady=10, padx=(80, 0))  # Adjusted pady
search_barr.bind("<Return>", on_search)
search_barr.insert(0, 'Search booksss')
search_barr.bind('<FocusIn>', on_entry_click)
search_barr.bind('<FocusOut>', on_focusout)

# Create a search button
search_button = tk.Button(menu_frame, text="Search", command=on_search)
search_button.grid(row=0, column=6, sticky="nsew", pady=(10, 0), padx=(10, 10))  # Adjusted pady


create_circle_buttons(menu_frame)

# Configure the grid to make the buttons and search bar expand and fill the space
for i in range(7):
    menu_frame.grid_columnconfigure(i, weight=1)
menu_frame.grid_columnconfigure(5, weight=2)  # Search bar column

# LEFT SIDE PANEL
left_margin = tk.Frame(main_content_frame, bg="#f8f7f3", width=100)
left_margin.pack(side="left", fill="y")

left_side_panel = tk.Frame(main_content_frame, bg="#f4f1ea", width=250)
left_side_panel.pack(side="left", fill="y")
left_side_panel.pack_propagate(False)  # Prevent the frame from shrinking

# Add the "CURRENTLY READING" label at the top
currentreading = tk.Label(left_side_panel, text="CURRENTLY READING", fg="#3b3746", font=("Helvetica", 11, "bold"), bg="#f4f1ea", anchor="w")
currentreading.pack(pady=(20, 10), fill="x")

# Create a frame for the "What are you reading?" label and icon
reading_frame = tk.Frame(left_side_panel, bg="#f4f1ea")
reading_frame.pack(pady=(10, 10), padx=10, fill="x")

# Create and pack the book icon
book_icon = create_book_icon(reading_frame)
book_icon.pack(side="left", padx=(0, 10))

# Add the "What are you reading?" label
reading_label = tk.Label(reading_frame, text="What are you reading?", font=("Helvetica", 9), bg="#f4f1ea")
reading_label.pack(side="left")

search_bar = tk.Entry(left_side_panel, font=("Helvetica", 9), highlightthickness=2, highlightbackground="gray", highlightcolor="gray", fg="grey")
search_bar.insert(0, 'Search books')
search_bar.pack(pady=(0, 10), padx=10, fill="x")

search_bar.bind('<FocusIn>', on_entry_click)
search_bar.bind('<FocusOut>', on_focusout)

recommendation_box = tk.Label(left_side_panel, text="Recommendations · General update", font=("Helvetica", 9, "bold"), fg="#237f71", bg="#f4f1ea", anchor="w")
recommendation_box.pack(pady=(0, 20), padx=(0, 10), fill="x")

# Add a separator frame directly under the spacer frame
separator_frame2 = tk.Frame(left_side_panel, height=1, bg="grey")
separator_frame2.pack(pady=(0, 10), padx=10, fill="x")

reading_challenge = tk.Label(left_side_panel, text="2024 READING CHALLENGE", font=("Helvetica", 10, "bold"), bg="#f4f1ea", fg="#3b3746", anchor="w")
reading_challenge.pack(pady=(0, 10), fill="x")

challenge_urs = tk.Label(left_side_panel, text="Challenge yourself to read more this year!", font=("Helvetica", 9), bg="#f4f1ea", anchor="w")
challenge_urs.pack(pady=(0, 10), fill="x")


challengefortheyear = tk.Frame(left_side_panel,bg="lightgray", width=350, height=170)
challengefortheyear.pack(pady=(0, 10), padx=10)
challengefortheyear.pack_propagate(False)

goalsetter = tk.Label(left_side_panel, text="You can change your goal at any time", bg="#f8f7f3", font=("Helvetica", 7, "bold"), fg="gray", anchor="w")
goalsetter.pack(pady=(5, 10), fill="x")

separator_frame2 = tk.Frame(left_side_panel, height=1, bg="grey")
separator_frame2.pack(pady=(0, 10), padx=10, fill="x")

toread = tk.Label(left_side_panel, text="WANT TO READ", font=("Helvetica", 10, "bold"), bg="#f4f1ea", fg="#3b3746", anchor="w")
toread.pack(pady=(0, 10), fill="x")

# Create a frame for the "What are you reading?" label and icon
reading_frame = tk.Frame(left_side_panel, bg="#f4f1ea")
reading_frame.pack(pady=(5, 10), padx=10, fill="x")

# Create and pack the book icon
book_icon = create_book_icon(reading_frame)
book_icon.pack(side="left", padx=(0, 10))

# Add the "What are you reading?" label
reading_next = tk.Label(reading_frame, text="What do you want to read next??", font=("Helvetica", 9), bg="#f4f1ea")
reading_next.pack(side="left")

recommendation = tk.Label(left_side_panel, text="Recommendations", font=("Helvetica", 9, "bold"), fg="#237f71", bg="#f4f1ea", anchor="w")
recommendation.pack(pady=(0, 20), padx=(0, 10), fill="x")

separator_frame2 = tk.Frame(left_side_panel, height=1, bg="grey")
separator_frame2.pack(pady=(0, 10), padx=10, fill="x")

bookshelves = tk.Label(left_side_panel, text="BOOKSHELVES", font=("Helvetica", 10, "bold"), bg="#f4f1ea", fg="#3b3746", anchor="w")
bookshelves.pack(pady=(0, 10), padx=(0, 10), fill="x")

wanttoread = tk.Label(left_side_panel, text="0  Want to Read", font=("Helvetica", 9, "bold"), fg="#237f71", bg="#f4f1ea", anchor="w")
wanttoread.pack(pady=(0, 5), padx=(0, 10), fill="x")

currentread = tk.Label(left_side_panel, text="0  Currently Reading", font=("Helvetica", 9, "bold"), fg="#237f71", bg="#f4f1ea", anchor="w")
currentread.pack(pady=(0, 5), padx=(0, 10), fill="x")

read_ = tk.Label(left_side_panel, text="0  Read", font=("Helvetica", 9, "bold"), fg="#237f71", bg="#f4f1ea", anchor="w")
read_.pack(pady=(0, 5), padx=(0), fill="x")










# CENTRAL CONTENT AREA
central_content = tk.Frame(main_content_frame, bg="#f8f7f3")
central_content.pack(side="left", fill="both", expand=True)
central_content.pack_propagate(False)  # Prevent the frame from shrinking


books_for_summer = tk.Frame(main_content_frame,bg="lightgray")
books_for_summer.pack(pady=(0, 10), padx=0, fill="x")
books_for_summer.pack_propagate(False)


booksummer = tk.Frame(main_content_frame, bg="white", width=550, height=170, highlightthickness=1, highlightbackground="#b9ad97", highlightcolor="#b9ad97")
booksummer.pack(pady=(0, 10), side="left", padx=(10, 90))

big_books = tk.Label(booksummer, text="The Big Books of Summer", font=("Helvetica", 10, "bold"), fg="#3b3746", anchor="w")
big_books.pack(pady=(0, 10), padx=(0), fill="x")

members = tk.Label(booksummer, text="Check out Goodreads members' most anticipated titles for a new season of reading!", font=("Helvetica", 10, "bold"), fg="lightgray", wraplength=230, justify="left", anchor="w")
members.pack(pady=(0, 10), padx=(0), fill="x")













# RIGHT SIDE PANEL
right_side_panel = tk.Frame(main_content_frame, bg="#f8f7f3", width=250)
right_side_panel.pack(side="left", fill="y")
right_side_panel.pack_propagate(False)  # Prevent the frame from shrinking

news_label = tk.Label(right_side_panel, text="NEWS & INTERVIEWS", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
news_label.pack(pady=(20, 10), fill="x")

right_margin = tk.Frame(main_content_frame, bg="white", width=100)
right_margin.pack(side="left", fill="y")

author = tk.Label(right_side_panel, text="The Author of Summer's Scariest Books Share Their Horror Picks", font=("Helvetica", 9, "bold"), bg="#f8f7f3", fg="#237f71", anchor="w", wraplength=230, justify="left")
author.pack(pady=(5, 10), fill="x")

# Create a frame instead of loading an image
book_selections_frame = tk.Frame(right_side_panel, bg="lightgray", width=300, height=130)
book_selections_frame.pack(pady=(0, 10), padx=10)
book_selections_frame.pack_propagate(False)

comments_likes = tk.Label(right_side_panel, text="144 likes · 12 comments", bg="#f8f7f3", font=("Helvetica", 7, "bold"), fg="gray", anchor="w")
comments_likes.pack(pady=(5, 10), fill="x")

separator_frame2 = tk.Frame(right_side_panel, height=1, bg="grey")
separator_frame2.pack(pady=(0, 10), padx=10, fill="x")

improve_recomm = tk.Label(right_side_panel, text="IMPROVE RECOMMENDATIONS", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
improve_recomm.pack(pady=(10, 10), fill="x")

rating_books = tk.Label(right_side_panel, text="Rating at least 20 books improves your recommendations. You have rated 0.", 
                        font=("Helvetica", 9), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
rating_books.pack(pady=(0, 5), fill="x")

separator_frame2 = tk.Frame(right_side_panel, height=15, bg="#d7cfc4")
separator_frame2.pack(pady=(0, 3), padx=10, fill="x")

percentage = tk.Label(right_side_panel, text="0/20 (0%)", bg="#f8f7f3", font=("Helvetica", 9), fg="gray", anchor="w")
percentage.pack(pady=(0, 10), fill="x")

rate_more_books = tk.Label(right_side_panel, text="Rate more books", font=("Helvetica", 9, "bold"), fg="#237f71", bg="#f8f7f3", anchor="w")
rate_more_books.pack(pady=(0, 8), fill="x")

separator_frame2 = tk.Frame(right_side_panel, height=1, bg="grey")
separator_frame2.pack(pady=(0, 5), padx=10, fill="x")

goodsreads_awards = tk.Label(right_side_panel, text="GOODREADS CHOICE AWARDS", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
goodsreads_awards.pack(pady=(10, 10), fill="x")

# Create a frame instead of loading an image
awards_frame = tk.Frame(right_side_panel, bg="lightgray", width=300, height=200)
awards_frame.pack(pady=(0, 10), padx=10)
awards_frame.pack_propagate(False)

separator_frame2 = tk.Frame(right_side_panel, height=1, bg="grey")
separator_frame2.pack(pady=(0, 5), padx=10, fill="x")

footer_replacement = tk.Label(right_side_panel, text="COMPANY              WORK WITH US", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
footer_replacement.pack(pady=(0, 5), fill="x")

aa_footer = tk.Label(right_side_panel, text="About us                          Authors ", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
aa_footer.pack(pady=(0), fill="x")
ca_footer = tk.Label(right_side_panel, text="Careers                           Advertise ", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
ca_footer.pack(pady=(0), fill="x")
ta_footer = tk.Label(right_side_panel, text="Terms                              Authors & ads blog ", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
ta_footer.pack(pady=(0), fill="x")
pa_footer = tk.Label(right_side_panel, text="Privacy                            API ", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
pa_footer.pack(pady=(0), fill="x")
ib_footer = tk.Label(right_side_panel, text="Interest Based Ads", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
ib_footer.pack(pady=(0), fill="x")
ap_footer = tk.Label(right_side_panel, text="Ad Preferences", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
ap_footer.pack(pady=(0), fill="x")
h_footer = tk.Label(right_side_panel, text="Help", font=("Helvetica", 8), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
h_footer.pack(pady=(0), fill="x")

footer_replacement1 = tk.Label(right_side_panel, text="CONNECT", font=("Helvetica", 10, "bold"), fg="#3b3746", bg="#f8f7f3", anchor="w")
footer_replacement1.pack(pady=(0, 5), fill="x")

copy_right = tk.Label(right_side_panel, text="@ 2024 Goodreads, Inc.", font=("Helvetica", 6), bg="#f8f7f3", anchor="w",  wraplength=230, justify="left")
copy_right.pack(pady=(0), fill="x")
######################



# Start the Tkinter event loop
root.mainloop()