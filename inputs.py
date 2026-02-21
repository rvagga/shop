
from colorama import Fore, Back, Style # Модуль для разукрашивания консоли
from logger_config import logger

def input_product():
    product = input(f'{Style.BRIGHT}Введите название товара: ').strip().title()
    logger.info(f"Введено название товара: {product}")
    return product

def number_validation(msg, is_int=False):
    # Функция для валидации введенных чисел. Кол-во ожидаем инт, цену - float
    while True:
        data = input(Style.BRIGHT + msg).strip()
        try:
            value = int(data) if is_int else float(data)

            if value > 0:
                logger.info(f"Введено число: {value}")
                return value if is_int else round(value, 2)
            else:
                logger.warning("Введено число <= 0")
                print(f'\n{Back.RED}{Fore.BLACK}Значение должно быть больше 0\n'
                      f'{Style.RESET_ALL}')

        except ValueError:
            logger.exception("Ошибка ввода числа")
            print(f'\n{Back.RED}{Fore.BLACK}Некорректное значение\n'
                  f'{Style.RESET_ALL}')

def input_quantity():
    qty = number_validation('Введите количество: ', is_int=True)
    logger.info(f"Введено количество: {qty}")
    return qty


def input_price():
    price = number_validation('Введите цену: ', is_int=False)
    logger.info(f"Введена цена: {price}")
    return price