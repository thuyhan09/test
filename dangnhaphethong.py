import tkinter as tk
from tkinter import messagebox

# Dữ liệu người dùng mẫu (thường lưu trong DB)
USERS = {
    "admin": "123456",
    "user1": "password"
}

# Hàm xử lý đăng nhập
def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    
    if not username or not password:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!")
        return
    
    if username in USERS and USERS[username] == password:
        messagebox.showinfo("Thành công", f"Đăng nhập thành công! Chào {username}")
        open_dashboard(username)
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu sai!")

# Mở Dashboard (cửa sổ mới)
def open_dashboard(username):
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("300x200")
    tk.Label(dashboard, text=f"Chào mừng {username} đến Dashboard!", font=("Arial", 14)).pack(pady=50)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form Đăng Nhập")
root.geometry("350x220")

# Nhãn và ô nhập Tên đăng nhập
tk.Label(root, text="Tên đăng nhập:").pack(pady=(20,5))
entry_username = tk.Entry(root, width=40)
entry_username.pack()

# Nhãn và ô nhập Mật khẩu
tk.Label(root, text="Mật khẩu:").pack(pady=(10,5))
entry_password = tk.Entry(root, show="*", width=40)
entry_password.pack()

# Nút đăng nhập
tk.Button(root, text="Đăng nhập", command=login).pack(pady=20)

root.mainloop()
