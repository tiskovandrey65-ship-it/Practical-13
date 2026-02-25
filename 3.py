file_path = input("Введите путь к файлу:")

parts = file_path.split("\\")

for part in parts:
    print(part)