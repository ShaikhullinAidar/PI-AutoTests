promo_codes = {"get5": 5, "get10": 10, "get15": 15}


def get_price(age: int, promo_code: str):
    price = 0
    if age <= 6:
        price = 200
    elif age < 18:
        price = 300
    elif age > 80:
        price = 200
    else:
        price = 500

    if promo_code in promo_codes.keys():
        price = price * (1 - promo_codes[promo_code] / 100)

    return max(price, 200)


if __name__ == '__main__':
    age = 0
    pc = ""
    try:
        age = int(input("Введите возраст\n"))
        pc = input("Введите промокод\n")
    except ValueError:
        print("введены некоректные значения")
        exit()
    print(get_price(age, pc))
