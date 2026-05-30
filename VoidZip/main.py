import customtkinter as ctk
from tkinter import filedialog, messagebox
from compressor import compress_file
from extractor import extract_file
import os


# =========================
# APP SETTINGS
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()
app.title("VoidZip")
app.geometry("900x550")
app.configure(fg_color="#050505")
app.resizable(False, False)


selected_file = None


# =========================
# LEFT SIDEBAR
# =========================
sidebar = ctk.CTkFrame(
    app,
    width=220,
    corner_radius=0,
    fg_color="#0d0d0d"
)
sidebar.pack(side="left", fill="y")


logo = ctk.CTkLabel(
    sidebar,
    text="VoidZip",
    font=("Segoe UI", 30, "bold"),
    text_color="#00ff99"
)
logo.pack(pady=(40, 10))


subtitle = ctk.CTkLabel(
    sidebar,
    text="Modern File Compressor",
    font=("Segoe UI", 13),
    text_color="gray"
)
subtitle.pack()


line = ctk.CTkFrame(
    sidebar,
    height=2,
    fg_color="#1a1a1a"
)
line.pack(fill="x", padx=20, pady=25)


feature1 = ctk.CTkLabel(
    sidebar,
    text="• ZIP Compression",
    anchor="w",
    font=("Segoe UI", 14),
    text_color="#d9d9d9"
)
feature1.pack(fill="x", padx=30, pady=8)


feature2 = ctk.CTkLabel(
    sidebar,
    text="• Fast Extraction",
    anchor="w",
    font=("Segoe UI", 14),
    text_color="#d9d9d9"
)
feature2.pack(fill="x", padx=30, pady=8)


feature3 = ctk.CTkLabel(
    sidebar,
    text="• Secure Local Storage",
    anchor="w",
    font=("Segoe UI", 14),
    text_color="#d9d9d9"
)
feature3.pack(fill="x", padx=30, pady=8)


feature4 = ctk.CTkLabel(
    sidebar,
    text="• Modern Black UI",
    anchor="w",
    font=("Segoe UI", 14),
    text_color="#d9d9d9"
)
feature4.pack(fill="x", padx=30, pady=8)


# =========================
# MAIN CONTENT AREA
# =========================
main_frame = ctk.CTkFrame(
    app,
    fg_color="#050505",
    corner_radius=0
)
main_frame.pack(side="right", expand=True, fill="both")


heading = ctk.CTkLabel(
    main_frame,
    text="Compress & Extract Files",
    font=("Segoe UI", 32, "bold"),
    text_color="white"
)
heading.pack(pady=(60, 10))


subheading = ctk.CTkLabel(
    main_frame,
    text="Minimal • Fast • Clean",
    font=("Segoe UI", 15),
    text_color="gray"
)
subheading.pack(pady=(0, 40))


# =========================
# FILE STATUS BOX
# =========================
status_frame = ctk.CTkFrame(
    main_frame,
    width=500,
    height=80,
    corner_radius=18,
    fg_color="#101010",
    border_width=1,
    border_color="#1f1f1f"
)
status_frame.pack(pady=10)

status_frame.pack_propagate(False)


status_label = ctk.CTkLabel(
    status_frame,
    text="No file selected",
    font=("Segoe UI", 14),
    text_color="#bfbfbf"
)
status_label.pack(expand=True)


# =========================
# FUNCTIONS
# =========================
def browse_file():
    global selected_file

    selected_file = filedialog.askopenfilename()

    if selected_file:
        filename = os.path.basename(selected_file)

        status_label.configure(
            text=f"Selected File: {filename}"
        )



def compress():
    global selected_file

    if not selected_file:
        messagebox.showerror("Error", "Please select a file first")
        return

    try:
        output = compress_file(selected_file)

        messagebox.showinfo(
            "Success",
            f"File compressed successfully!\n\nSaved to:\n{output}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))



def extract():
    global selected_file

    if not selected_file:
        messagebox.showerror("Error", "Please select a ZIP file")
        return

    try:
        output = extract_file(selected_file)

        messagebox.showinfo(
            "Success",
            f"ZIP extracted successfully!\n\nSaved to:\n{output}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# BUTTONS
# =========================
button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)
button_frame.pack(pady=40)


browse_btn = ctk.CTkButton(
    button_frame,
    text="Browse File",
    command=browse_file,
    width=220,
    height=55,
    corner_radius=16,
    fg_color="#00cc88",
    hover_color="#00aa72",
    text_color="black",
    font=("Segoe UI", 15, "bold")
)

browse_btn.grid(row=0, column=0, padx=15, pady=15)


compress_btn = ctk.CTkButton(
    button_frame,
    text="Compress",
    command=compress,
    width=220,
    height=55,
    corner_radius=16,
    fg_color="#121212",
    hover_color="#1f1f1f",
    border_width=1,
    border_color="#00cc88",
    text_color="#00ff99",
    font=("Segoe UI", 15, "bold")
)

compress_btn.grid(row=0, column=1, padx=15, pady=15)


extract_btn = ctk.CTkButton(
    button_frame,
    text="Extract ZIP",
    command=extract,
    width=220,
    height=55,
    corner_radius=16,
    fg_color="#121212",
    hover_color="#1f1f1f",
    border_width=1,
    border_color="#00cc88",
    text_color="#00ff99",
    font=("Segoe UI", 15, "bold")
)

extract_btn.grid(row=1, column=0, columnspan=2, pady=10)


# =========================
# FOOTER
# =========================
footer = ctk.CTkLabel(
    main_frame,
    text="Built with Python + CustomTkinter",
    font=("Segoe UI", 12),
    text_color="#666666"
)
footer.pack(side="bottom", pady=20)


app.mainloop()