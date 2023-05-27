def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers_input1 = input("Digite o primeiro número: ")
numbers_list1 = [int(num) for num in numbers_input1.split()]

numbers_input2 = input("Digite o segundo número: ")
numbers_list2 = [int(num) for num in numbers_input2.split()]

combined_numbers = numbers_list1 + numbers_list2

result = sum_numbers(combined_numbers)
print("Resultado da Soma:", result)
