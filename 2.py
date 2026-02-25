n = int(input("Введите количество строк:"))

all_list = []

for i in range(n):
    current_string = input()
    all_list.extend(current_string)
print(all_list)