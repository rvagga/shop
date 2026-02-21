from logger_config import logger


def main_menu():
    print('ГЛАВНОЕ МЕНЮ\n'
          '1. Касса\n'
          '2. Управление\n'
          '3. Выйти')

    choice = input().strip()
    logger.info(f"Главное меню: выбор {choice}")

    return choice


def cashier_menu():
    print('КАССА\n'
          '1. Новая продажа\n'
          '2. Отчет за смену\n'
          '3. Главное меню')

    choice = input().strip()
    logger.info(f"Касса: выбор {choice}")

    return choice


def warehouse_menu():
    print('УПРАВЛЕНИЕ\n'
          '1. Добавить товар в продажу\n'
          '2. Исключить товар из продажи\n'
          '3. Изменить количество товара\n'
          '4. Изменить цену товара\n'
          '5. Товары в продаже\n'
          '6. В главное меню')

    choice = input().strip()
    logger.info(f"Управление: выбор {choice}")

    return choice
