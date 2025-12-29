import sqlite3
import hashlib

# Kết nối đến cơ sở dữ liệu (hoặc tạo mới nếu chưa có)
conn = sqlite3.connect('hotel_system.db')
cursor = conn.cursor()

# Tạo bảng users nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')

# Hàm mã hóa mật khẩu
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Tài khoản admin mặc định
default_admin = {
    "username": "admin",
    "password": hash_password("Admin@123"),  # mật khẩu mặc định
    "role": "admin"
}

# Kiểm tra nếu admin chưa tồn tại thì thêm
cursor.execute("SELECT * FROM users WHERE username = ?", (default_admin["username"],))
if cursor.fetchone() is None:
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (default_admin["username"], default_admin["password"], default_admin["role"])
    )
    conn.commit()
    print("Tài khoản admin mặc định đã được tạo!")
else:
    print("Tài khoản admin mặc định đã tồn tại.")

conn.close()
