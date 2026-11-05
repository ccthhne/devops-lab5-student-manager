"""
Student Manager — DevOps Lab 5
Module: Main Application
"""

from student import Student


# --- Chức năng thêm sinh viên ---
def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách."""
    for s in students:
        if s.student_id == student_id:
            print(f"Mã sinh viên {student_id} đã tồn tại!")
            return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Đã thêm sinh viên: {new_student}")
    return students


# --- Chức năng tìm kiếm sinh viên ---
def search_student(students: list, keyword: str) -> list:
    """Tìm sinh viên theo tên hoặc mã, không phân biệt hoa thường."""
    keyword_lower = keyword.lower()
    results = []
    for s in students:
        if keyword_lower in s.name.lower() or keyword_lower in s.student_id.lower():
            results.append(s)

    if results:
        print(f"\nTìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for s in results:
            print(f"  {s}")
    else:
        print(f"\nKhông tìm thấy sinh viên nào với từ khóa '{keyword}'.")
    return results


# --- Chức năng sửa sinh viên ---
def update_student(students: list, student_id: str, new_name=None, new_age=None, new_grade=None) -> list:
    """Sửa tên/tuổi/khóa của sinh viên theo mã."""
    for s in students:
        if s.student_id == student_id:
            if new_name is not None:
                s.name = new_name
            if new_age is not None:
                s.age = new_age
            if new_grade is not None:
                s.grade = new_grade
            print(f"Đã cập nhật sinh viên: {s}")
            return students

    print(f"Không tìm thấy sinh viên có mã {student_id}!")
    return students


# --- Chức năng xóa sinh viên ---
def delete_student(students: list, student_id: str) -> list:
    """Xóa sinh viên theo mã."""
    for s in students:
        if s.student_id == student_id:
            students.remove(s)
            print(f"Đã xóa sinh viên: {s}")
            return students

    print(f"Không tìm thấy sinh viên có mã {student_id}!")
    return students


def show_students(students):
    """Hiển thị toàn bộ danh sách."""
    print("\nDanh sách sinh viên:")
    for student in students:
        print(f"  {student}")
    print(f"\nTotal: {len(students)} students")


def main():
    """Hàm chính: menu tương tác, bạn tự chọn hành động."""
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    while True:
        print("\n" + "=" * 50)
        print("STUDENT MANAGER — DevOps Lab 5")
        print("=" * 50)
        print("1. Thêm sinh viên")
        print("2. Tìm kiếm sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Hiển thị danh sách")
        print("0. Thoát")
        choice = input("Chọn chức năng (0-5): ").strip()

        if choice == "0":
            print("Tạm biệt!")
            break

        elif choice == "1":
            student_id = input("Nhập mã sinh viên: ").strip()
            name = input("Nhập tên sinh viên: ").strip()
            try:
                age = int(input("Nhập tuổi: ").strip())
            except ValueError:
                print("Tuổi phải là số!")
                continue
            grade = input("Nhập khóa: ").strip()
            students = add_student(students, student_id, name, age, grade)

        elif choice == "2":
            keyword = input("Nhập tên hoặc mã cần tìm: ").strip()
            search_student(students, keyword)

        elif choice == "3":
            student_id = input("Nhập mã sinh viên cần sửa: ").strip()
            new_name = input("Nhập tên mới (để trống nếu giữ nguyên): ").strip()
            new_age_input = input("Nhập tuổi mới (để trống nếu giữ nguyên): ").strip()
            new_grade = input("Nhập khóa mới (để trống nếu giữ nguyên): ").strip()
            new_age = None
            if new_age_input:
                try:
                    new_age = int(new_age_input)
                except ValueError:
                    print("Tuổi phải là số!")
                    continue
            students = update_student(
                students,
                student_id,
                new_name if new_name else None,
                new_age,
                new_grade if new_grade else None,
            )

        elif choice == "4":
            student_id = input("Nhập mã sinh viên cần xóa: ").strip()
            students = delete_student(students, student_id)

        elif choice == "5":
            show_students(students)

        else:
            print("Lựa chọn không hợp lệ, chỉ nhập 0-5 thôi!")


if __name__ == "__main__":
    main()
