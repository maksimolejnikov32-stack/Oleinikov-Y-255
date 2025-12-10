def task_a1():
    def power(x, n):
        if n == 0:
            return 1
        return x * power(x, n - 1)
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)
    x = int(input("Введите X: "))
    n = int(input("Введите N: "))
    result = power(x, n) / factorial(n)
    print(f"{x}^{n} / {n}! = {result}")
    return result
def task_a2():
    def mod(a, b):
        if a < b:
            return a
        return mod(a - b, b)
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    result = mod(a, b)
    print(f"Остаток от деления {a} на {b} = {result}")
    return result
def task_a3():
    def reverse_num(n):
        if n < 10:
            print(n, end='')
            return
        print(n % 10, end='')
        reverse_num(n // 10)
    n = int(input("Введите число: "))
    print(f"Число {n} в обратном порядке: ", end='')
    reverse_num(n)
    print()
def task_a4():
    def sum_digits(n):
        if n < 10:
            return n
        return n % 10 + sum_digits(n // 10)
    n = int(input("Введите число N: "))
    result = sum_digits(n)
    print(f"Сумма цифр числа {n} = {result}")
    return result
def task_a5():
    def print_digits_reverse(n):
        if n < 10:
            print(n)
            return
        print(n % 10)
        print_digits_reverse(n // 10)
    n = int(input("Введите число N: "))
    print(f"Цифры числа {n} в обратном порядке:")
    print_digits_reverse(n)
def task_a6():
    def is_prime(n, divisor=None):
        if divisor is None:
            divisor = 2
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return is_prime(n, divisor + 1)
    n = int(input("Введите число n (>1): "))
    if is_prime(n):
        print(f"Число {n} - простое (YES)")
    else:
        print(f"Число {n} - составное (NO)")
def task_a7():
    def print_range(a, b):
        if a == b:
            print(a)
            return
        print(a, end=' ')
        if a < b:
            print_range(a + 1, b)
        else:
            print_range(a - 1, b)
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    print(f"Числа от {a} до {b}:")
    print_range(a, b)
def task_b1():
    def find_max():
        num = int(input())
        if num == 0:
            return 0
        next_max = find_max()
        return num if num > next_max else next_max
    print("Введите последовательность чисел (0 для завершения):")
    max_value = find_max()
    print(f"Наибольшее значение: {max_value}")
    return max_value
def task_b2():
    def find_second_max(first_max=-1, second_max=-1):
        num = int(input())
        if num == 0:
            return second_max
        if num > first_max:
            return find_second_max(num, first_max)
        elif num > second_max:
            return find_second_max(first_max, num)
        else:
            return find_second_max(first_max, second_max)
    print("Введите последовательность чисел (0 для завершения):")
    second_max = find_second_max()
    print(f"Второе по величине значение: {second_max}")
    return second_max
def task_b3():
    def print_odd_positions(count=1):
        num = int(input())
        if num == 0:
            return
        if count % 2 == 1:
            print(num, end=' ')
        print_odd_positions(count + 1)
    print("Введите последовательность чисел (0 для завершения):")
    print("Элементы на нечетных позициях:", end=' ')
    print_odd_positions()
    print()
def task_b4():
    def is_prime_optimized(n, divisor=2):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        if divisor * divisor > n:
            return True
        if n % divisor == 0:
            return False
        return is_prime_optimized(n, divisor + 6) if divisor % 6 == 1 else is_prime_optimized(n, divisor + 4)
    n = int(input("Введите число n (>1): "))
    if is_prime_optimized(n):
        print(f"Число {n} - простое (YES)")
    else:
        print(f"Число {n} - составное (NO)")
def main():
    tasks = {
        'A1': task_a1,
        'A2': task_a2,
        'A3': task_a3,
        'A4': task_a4,
        'A5': task_a5,
        'A6': task_a6,
        'A7': task_a7,
        'B1': task_b1,
        'B2': task_b2,
        'B3': task_b3,
        'B4': task_b4
    }
    print("=" * 50)
    print("ПРАКТИЧЕСКАЯ РАБОТА 12: РЕКУРСИЯ")
    print("=" * 50)
    print("\nБЛОК А:")
    print("1. Вычислить x^n / n!")
    print("2. Остаток от деления a на b")
    print("3. Вывести число в обратном порядке")
    print("4. Сумма цифр числа")
    print("5. Цифры числа в обратном порядке")
    print("6. Проверка на простоту")
    print("7. Вывести числа от A до B")
    print("\nБЛОК Б:")
    print("8. Наибольшее значение в последовательности")
    print("9. Второе по величине значение")
    print("10. Элементы на нечетных позициях")
    print("11. Проверка на простоту (оптимизированная)")
    print("0. Выход")
    while True:
        try:
            choice = input("\nВыберите задачу (1-11 или 0 для выхода): ").strip()
            if choice == '0':
                print("Завершение программы...")
                break
            if choice == '1':
                task_a1()
            elif choice == '2':
                task_a2()
            elif choice == '3':
                task_a3()
            elif choice == '4':
                task_a4()
            elif choice == '5':
                task_a5()
            elif choice == '6':
                task_a6()
            elif choice == '7':
                task_a7()
            elif choice == '8':
                task_b1()
            elif choice == '9':
                task_b2()
            elif choice == '10':
                task_b3()
            elif choice == '11':
                task_b4()
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите число.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
if __name__ == "__main__":
    main()