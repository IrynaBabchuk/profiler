import time
import math
import cProfile
import pstats
from io import StringIO


# Функція для обрахунку факторіалу
def calculate_factorial(n):
    return math.factorial(n)


# Функція для обрахунку таблиці квадратів
def calculate_squares(numbers):
    return [x ** 2 for x in numbers]


# Функція для обрахунку таблиці кубів
def calculate_cubes(numbers):
    return [x ** 3 for x in numbers]


# Функція для затримки
def delay(seconds):
    time.sleep(seconds)


# Основна функція
def main():
    n = 10
    numbers = list(range(1, 1000))
    delay_time = 2

    # Обрахунок факторіалу
    factorial_result = calculate_factorial(n)

    # Обрахунок таблиці квадратів
    squares_result = calculate_squares(numbers)

    # Обрахунок таблиці кубів
    cubes_result = calculate_cubes(numbers)

    # Затримка
    delay(delay_time)


# Профілювання програми
def profile_program():
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
    ps.print_stats()

    with open("profile_results.txt", "w") as f:
        f.write(s.getvalue())


# Виконання профілювання
profile_program()

# Виконання основної програми
if __name__ == "__main__":
    main()
