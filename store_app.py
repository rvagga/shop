from logger_config import logger
logger.info("Программа запущена")

from colorama import Fore, Back, Style
from Cashier import Cashier
from Menu import *


cashier = Cashier()
state = 'main'

while True:
    if state == 'main':
        decision = main_menu()
        match decision:
            case '1': state = 'cashier'
            case '2': state = 'warehouse'
            case '3': break
            case _:
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')

    elif state == 'cashier':
        decision = cashier_menu()
        match decision:
            case '1': cashier.sell_product()
            case '2': print(cashier)
            case '3': state = 'main'
            case _:
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')

    elif state == 'warehouse':
        decision = warehouse_menu()
        match decision:
            case '1': cashier.add_product()
            case '2': cashier.remove_product()
            case '3': cashier.change_quantity()
            case '4': cashier.change_price()
            case '5': cashier.products
            case '6': state = 'main'
            case _:
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')