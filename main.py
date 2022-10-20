def open_base(file_name):
    file = open(file_name, "r", encoding="utf-8-sig")
    uni_base = file.readlines()
    return uni_base

print(open_base("test_base.csv"))

def open_base_2(file_name):
    with open(file_name, "r", encoding='utf-8-sig') as file:
        uni_base = file.readlines()
    return uni_base

print(open_base_2("test_base.csv"))