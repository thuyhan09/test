import tkinter as tk
from tkinter import messagebox

# =====================
# DỮ LIỆU MẪU
# =====================
USERS = {
    "admin": "123456",
    "user1": "password"
}

ROOMS = [
    {"id": 101, "type": "Phòng đơn", "price": 300000, "status": "Trống"},
    {"id": 102, "type": "Phòng đôi", "price": 500000, "status": "Đã đặt"},
    {"id": 103, "type": "Phòng VIP", "price": 1000000, "status": "Trống"}
]


# =====================
# ĐĂNG KÝ
# =====================
def register():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    if username in USERS:
        messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại!")
        return

    USERS[username] = password
    messagebox.showinfo("Thành công", "Đăng ký tài khoản thành công!")

# =====================
# DASHBOARD
# =====================
def open_dashboard(username):
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")

    tk.Label(
        dashboard,
        text=f"Xin chào {username}",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Button(
        dashboard,
        text="Xem danh sách phòng",
        width=25,
        command=open_room_list
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Đăng xuất",
        width=25,
        command=dashboard.destroy
    ).pack(pady=10)

# =====================
# DANH SÁCH PHÒNG
# =====================
def open_room_list():
    room_window = tk.Toplevel(root)
    room_window.title("Danh sách phòng")
    room_window.geometry("550x300")

    tk.Label(
        room_window,
        text="DANH SÁCH PHÒNG KHÁCH SẠN",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    frame = tk.Frame(room_window)
    frame.pack()

    headers = ["Mã phòng", "Loại phòng", "Giá (VND)", "Trạng thái"]
    for col, header in enumerate(headers):
        tk.Label(frame, text=header, width=15, borderwidth=1, relief="solid").grid(row=0, column=col)

    for row, room in enumerate(ROOMS, start=1):
        tk.Label(frame, text=room["id"], width=15, borderwidth=1, relief="solid").grid(row=row, column=0)
        tk.Label(frame, text=room["type"], width=15, borderwidth=1, relief="solid").grid(row=row, column=1)
        tk.Label(frame, text=room["price"], width=15, borderwidth=1, relief="solid").grid(row=row, column=2)
        tk.Label(frame, text=room["status"], width=15, borderwidth=1, relief="solid").grid(row=row, column=3)


