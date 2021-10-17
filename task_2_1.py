list_cub = []
numbers = 0

# "a" Создать список, состоящий из кубов нечётных чисел от 1 до 1000
while numbers < 1001:
    if numbers % 2 != 0:
        list_cub.append(numbers ** 3)
    numbers = numbers + 1
print(list_cub)


