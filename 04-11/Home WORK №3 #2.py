result = ()

def divider(a, b):
    if a < b:
        raise ValueError("Первое значение должен быть больше второго.")
    if b > 100:
        raise IndexError("Значение не должен быть меньше первого числа.")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль.")
    return a / b

data = {10: 2, 2: 5, 123: 4, 18: 1, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Ошибка({key}: {data[key]}): {e}")

print(result)