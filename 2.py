n = int(input("Введите что нибудь:"))

all_list = []

for i in range(n):
    current_string = input()
    all_list.extend(current_string)
print(all_list)