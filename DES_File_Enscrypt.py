import random
import string
from Crypto.Cipher import DES
import os
from tkinter import *
from tkinter import font, filedialog, messagebox

def choose_file():
    # Mở hộp thoại chọn file và lấy đường dẫn
    filename = filedialog.askopenfilename()
    # Nếu người dùng đã chọn một tệp
    if filename:
        # Xóa nội dung hiện tại trong Text box
        text_box.delete(1.0, 'end')
        # Chèn đường dẫn của tệp vào Text box
        text_box.insert('end', filename)
def generate_key():
    # Sinh một chuỗi ngẫu nhiên có 16 ký tự từ các ký tự chữ và số
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # Insert khóa vào text_box1
    text_box1.delete(1.0, 'end')  # Xóa nội dung hiện tại trong text_box1
    text_box1.insert('end', key)   # Chèn khóa vào text_box1

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def encrypt(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.rstrip()

# Tạo font Times New Roman
root = Tk()
times_new_roman_font = font.Font(family="Slab Serif", size=10, weight="normal")
times_new_roman_font1 = font.Font(family="Slab Serif ", size=35, weight="bold")
# Tạo Frame cho vùng màu vàng
yellow_frame = Frame(root, bg="yellow", width=500, height=100)
yellow_frame.grid(row=0, column=0, columnspan=4, sticky="ew")

# Nhãn "MÃ HÓA FILE"
label_title = Label(yellow_frame, text="    MÃ HÓA FILE", font=times_new_roman_font1, bg="yellow")
label_title.pack()

# Nhãn "File mã hóa"
label_file = Label(root, text="File", font=times_new_roman_font)
label_file.grid(row=2, column=0, columnspan=2)

# Chỉnh kích thước của nhãn
label_file.config(width=20, height=2)

# Frame chứa ô văn bản và nút chọn tệp
frame = Frame(root)
frame.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky='ew')

# Ô văn bản cho phép nhập
text_box = Text(frame, font=times_new_roman_font,height=2, width=50)
text_box.pack(side='left', fill='x', expand=True)

# Nút chọn tệp
button_choose_file = Button(frame, text="Chọn tệp", command=choose_file,font=times_new_roman_font)
button_choose_file.pack(side='right', padx=10)
#
#
# Nhãn "Sinh khóa"
label_file1 = Label(root, text="Sinh khóa", font=times_new_roman_font)
label_file1.grid(row=3, column=0, columnspan=2)

# Chỉnh kích thước của nhãn
label_file1.config(width=20, height=2)

# Frame chứa ô văn bản và nút chọn tệp
frame1 = Frame(root)
frame1.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky='ew')

# Ô văn bản cho phép nhập
text_box1 = Text(frame1, font=times_new_roman_font, height=2, width=50)
text_box1.pack(side='left', fill='x', expand=True)

# Nút chọn tệp
button_choose_file1 = Button(frame1, text="Sinh khóa",command=generate_key,font=times_new_roman_font)
button_choose_file1.pack(side='right', padx=10)
#
#
#
# Tạo Frame để chứa hai nút "Mã hóa" và "Giải mã"
frame_buttons = Frame(root)
frame_buttons.grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky='ew')


def main1():
    file_path = text_box.get(1.0, 'end-1c')
    print(file_path)
    with open(file_path, 'rb') as file:
        original_content = file.read()

    # Chia file thành phần đã mã hóa và chưa mã hóa
    encrypted_part = original_content[:16]  # 16 kí tự đầu tiên
    remaining_part = original_content[16:]

    key = text_box1.get(1.0, 'end-1c').encode()

    # Mã hóa phần đầu tiên của file
    encrypted_part = encrypt(encrypted_part, key)

    # Kết hợp phần đã mã hóa và phần chưa mã hóa để tạo ra nội dung mới
    new_content = encrypted_part + remaining_part

    # Ghi nội dung đã mã hóa vào file mới
    with open('file_output1.pdf', 'wb') as file:
        file.write(new_content)
    messagebox.showinfo("Thông báo", "Mã hóa thành công!")
def main2():
    file_path = text_box.get(1.0, 'end-1c')
    print(file_path)
    with open(file_path, 'rb') as file:
        original_content = file.read()

    # Chia file thành phần đã mã hóa và chưa mã hóa
    encrypted_part = original_content[:16]  # 16 kí tự đầu tiên
    remaining_part = original_content[16:]

    key = text_box1.get(1.0, 'end-1c').encode()

    # Mã hóa phần đầu tiên của file
    encrypted_part = decrypt(encrypted_part, key)

    # Kết hợp phần đã mã hóa và phần chưa mã hóa để tạo ra nội dung mới
    new_content = encrypted_part + remaining_part

    # Ghi nội dung đã mã hóa vào file mới
    with open('file_output2.pdf', 'wb') as file:
        file.write(new_content)
    messagebox.showinfo("Thông báo", "Giải mã thành công!")

# Tạo Button "Mã hóa"
button_encrypt = Button(frame_buttons, text="Mã hóa",command=main1)
button_encrypt.pack(side='left', padx=10)

# Tạo Button "Giải mã"
button_decrypt = Button(frame_buttons, text="Giải mã",command=main2)
button_decrypt.pack(side='left', padx=10)

root.mainloop()