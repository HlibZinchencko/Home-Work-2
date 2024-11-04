from dbm import error

print("Prev code")
try:
    input()
    print(10 / 0)
    print(value)
except KeyboardInterrupt:
    print("Ошибка с клавиатурой")
except ZeroDivisionError:
    print("нет нельзя делить на ноль")
except (NameError, KeyError) as error:
    print(error)
print("Next code")
