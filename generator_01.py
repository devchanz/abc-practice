# generator_01.py


# 전부 생산 후 출하
def generate_numbers_1(max_number: int):
    print('Called generate_numbers_1 function')
    numbers = []
    for i in range(1, max_number+1):
        numbers.append(i)
    return numbers

# Generator 객체를 생성하는 함수
def generate_numbers_2(max_number: int):
    print('Called generate_numbers_2 function')
    for i in range(1, max_number+1):
        yield i 

numbers_1 = generate_numbers_1(10)
numbers_2 = generate_numbers_2(10)
print(numbers_1)
print(numbers_2)