from tkinter import filedialog
from tkinter import messagebox
import customtkinter
import qrcode
FONT = ("Bahnschrift", 25)

BUTTON_COLOR = "#FFD700"
BUTTON_COLOR_HOVER = "#FFFFE0"
FONT_COLOR = "#000000"


def create_qr():
    data = content_entry.get()
    qr = qrcode.make(data)
    files = [('Portable Network Graphics', '*.png'), 
             ('All Files', '*.*'),
             ('Joint Photographic Experts Group', '*.jpeg')]
    dir = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
    if dir != None:
        qr.save(dir.name)
        messagebox.showinfo(title="Thành công", message="QR code đã được lưu !")


def about_devs():
    messagebox.showinfo(title="About Devs", message="Made by @mahiru7229")






windows = customtkinter.CTk()

label_1 = customtkinter.CTkLabel(windows, text="QR Code Generator", font = FONT)
label_1.grid(row= 0, column = 0, padx=10, pady=10)

content_entry = customtkinter.CTkEntry(windows, placeholder_text="Nhập nội dung để chuyển qua QR Code.", font = FONT, width=500)
content_entry.grid(row= 1, column = 0, padx=10, pady=10)

submit_btn = customtkinter.CTkButton(windows, text="Tạo QR Code", font = FONT, fg_color=BUTTON_COLOR, text_color=FONT_COLOR, hover_color=BUTTON_COLOR_HOVER, command=create_qr)
submit_btn.grid(row= 0, column = 1, padx=10, pady=10)

help_btn = customtkinter.CTkButton(windows, text="Hướng dẫn sử dụng", font = FONT, fg_color=BUTTON_COLOR, text_color=FONT_COLOR, hover_color=BUTTON_COLOR_HOVER)
help_btn.grid(row= 1, column = 1, padx=10, pady=10)

about_btn = customtkinter.CTkButton(windows, text="About Devs", font = FONT, fg_color=BUTTON_COLOR, text_color=FONT_COLOR, hover_color=BUTTON_COLOR_HOVER, command=about_devs)
about_btn.grid(row= 2, column = 1, padx=10, pady=10)



windows.title("QR Code Generator 1.0")
windows.resizable(width=False, height=False)
windows.mainloop()

