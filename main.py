def show_list(list: list):
    print("")
    print(" Danh sách nhân viên ".center(30, "="))
    header = f'{"ID":<5} | {"Họ Tên":<20} | {"Lương Ngày":<15} | {"Ngày Công":<10} | {"Phụ cấp":<10} | {"Tổng thu nhập":<20} | {"Phân loại thu nhập":<20}'
    print(header)
    print("-"*len(header))
    for value in list:
        print(f'{value["id"]:<5} | {value["name"]:<20} | {value["salary"]:<15} | {value["day"]:<10} | {value["bonus"]:<10} | {value["total_salary"]:<20} | {value["rank"]:<20}')
    print("-"*len(header))
    print("")

def add_employee(list):
    id_input = input("Nhập id: ")
    name_input = input("Nhập tên: ")
    salary_input = int(input("Nhập lương ngày: "))
    day_input = int(input("Nhập số ngày công: "))
    bonus_input = int(input("Nhập tiền phụ cấp: "))

    total_salary = (salary_input * day_input) + bonus_input

    if total_salary >= 30000000:
        rank = "Cao"
    elif total_salary >= 15000000:
        rank = "Khá"
    elif total_salary >= 9000000:
        rank = "Trung bình"
    else:
        rank = "Thấp"

    new_employee = {"id": id_input, "name": name_input, "salary": salary_input, "day": day_input, "bonus": bonus_input, "total_salary": total_salary, "rank": rank}

    employees.append(new_employee)
    print("\nThêm mới nhân viên thành công!")
    
def update_employee(list):
    id_find = input("Nhập mã nhân viên: ")

    is_id = False
    id_index = -1

    for index, employee in enumerate(employees):
        if id_find == employee["id"]:
            is_id = True
            id_index = index
            break

    if is_id == False:
        print("Không tìm thấy nhân viên!")
        return

    new_salary_input = int(input("Nhập lương ngày cơ bản: "))
    new_day_input = int(input("Nhập ngày công: "))
    new_bonus_input = int(input("Nhập tiền phụ cấp: "))

    new_total_salary = (new_salary_input * new_day_input) + new_bonus_input

    if new_total_salary >= 30000000:
        new_rank = "Cao"
    elif new_total_salary >= 15000000:
        new_rank = "Khá"
    elif new_total_salary >= 9000000:
        new_rank = "Trung bình"
    else:
        new_rank = "Thấp"

    employees[id_index]["salary"] = new_salary_input
    employees[id_index]["day"] = new_day_input
    employees[id_index]["bonus"] = new_bonus_input
    employees[id_index]["total_salary"] = new_total_salary
    employees[id_index]["rank"] = new_rank
    print("\nCập nhật nhân viên thành công!")

employees = [
    {"id": "NV001", "name": "Nguyen Van A", "salary": 400000, "day": 25, "bonus": 1500000, "total_salary": 11500000, "rank": "Khá"}
]

while True:
    print(" Chương trình quản lý nhân viên ".center(60,"="))
    print("1. Hiển thị danh sách nhân viên")
    print("2. Thêm nhân viên mới")
    print("3. Cập nhật lương nhân viên")
    print("4. Xóa nhân viên")
    print("5. Tìm kiếm nhân viên")
    print("")
    print("")
    print("8. thoát chương trình")
    choice = input("Nhập lựa chọn: ")
    
    match choice:
        case "1":
            show_list(employees)
        case "2":
            add_employee(employees)
        case "3":
            update_employee(employees)
        case "4":
            id_del = input("Nhập id nhân viên: ")

            is_id = False
            id_index = -1

            for index, employee in enumerate(employees):
                    if id_del == employee["id"]:
                        is_id = True
                        id_index = index
                        break

            if is_id == False:
                print("Không tìm thấy nhân viên!")
                continue

            choice = input("Bạn có chắc muốn xóa nhân viên này không? (Y/N): ")

            if choice.lower() == "y":
                del employees[id_index]
                print("Đã xóa nhân viên thành công!")
            elif choice.lower() == "n":
                print("Đã hủy xóa nhân viên!")
                continue
            else:
                print("Lựa chọn không hợp lệ!")
                continue
        case "5":
            input_find = input("Nhập thông tin nhân viên cần tìm(id, name): ")

            is_id = False
            id_index = -1

            for index, employee in enumerate(employees):
                    if input_find == employee["id"]:
                        is_id = True
                        id_index = index
                        break

            if is_id == False:
                for index, employee in enumerate(employees):
                    if input_find.lower() in employee["name"].lower():
                        is_id = True
                        id_index = index
                        break

            if is_id == False:
                print("Không tìm thấy nhân viên!")
                
            print("Thông tin nhân viên", employees[id_index]["name"])
            header = f'{"ID":<5} | {"Họ Tên":<20} | {"Lương Ngày":<15} | {"Ngày Công":<10} | {"Phụ cấp":<10} | {"Tổng thu nhập":<20} | {"Phân loại thu nhập":<20}'
            print(header)
            print(f'{employees[id_index]["id"]:<5} | {employees[id_index]["name"]:<20} | {employees[id_index]["salary"]:<15} | {employees[id_index]["day"]:<10} | {employees[id_index]["bonus"]:<10} | {employees[id_index]["total_salary"]:<20} | {employees[id_index]["rank"]:<20}')
        case "6":
            pass
        case "7":
            pass
        case "8":
            print("Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")