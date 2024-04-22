def rubles_word(number):
    if number % 10 == 1 and number % 100 != 11:
        return "рубль"
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return "рубля"
    else:
        return "рублей"

rubles = int(input("Введите число: "))
print(f"{rubles} {rubles_word(rubles)}")
