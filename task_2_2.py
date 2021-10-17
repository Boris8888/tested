list_cub = []
numbers = 0
num_elem = 0
sum_elem = 0
# "b, c" Создать список, состоящий из кубов нечётных чисел от 1 до 1000
while numbers < 1001:
    if numbers % 2 != 0:
        numbers_str = str(numbers ** 3)
        while num_elem < len(numbers_str):
            sum_elem = sum_elem + int(numbers_str[num_elem])
            num_elem = num_elem + 1
        if sum_elem % 7 == 0:
            list_cub.append(sum_elem)
    num_elem = 0
    sum_elem = 0
    numbers = numbers + 1
print(list_cub)