# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách student_list.
    - In ra thông báo "Da them sinh vien <ten> thanh cong."
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

# --- Phần thực thi chính để kiểm tra ---
# Sinh viên không cần chỉnh sửa phần này.
if _name_ == "_main_":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")

    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Yêu cầu 2: In danh sách
    print("\n2. In danh sach sinh vien:")
    print_student_list()

    # Yêu cầu 3: Tìm kiếm
    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")

    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")