from logger_config import logger

from Inputs import input_product, input_price, input_quantity
from dataclasses import dataclass
from colorama import Fore, Back, Style


@dataclass
class ProductInfo:
    price: float
    quantity: int


class Warehouse:
    def __init__(self):
        self._products = {
            'Пончик': ProductInfo(price=1.99, quantity=100),
            'Сочник': ProductInfo(price=2.99, quantity=50),
            'Сметанник': ProductInfo(price=2.50, quantity=42)
        }

        logger.info("Инициализирован склад с базовыми товарами")

    @property
    def products(self):
        if self._products:
            logger.info("Просмотр списка товаров на складе")

            print(f'\n{Back.YELLOW}{Fore.BLACK}Товары на складе:')

            for i, (product, info) in enumerate(self._products.items(), 1):
                print(
                    f'{i}. Товар: {product}. '
                    f'Цена: {info.price} BYN. '
                    f'Количество: {info.quantity}.'
                )

            print(Style.RESET_ALL)
        else:
            logger.warning("Попытка просмотра пустого склада")

            print(
                f'\n{Back.RED}{Fore.BLACK}Нет товаров на складе\n'
                f'{Style.RESET_ALL}'
            )

    def add_product(self):
        product = input_product()
        logger.info(f"Попытка добавления товара: {product}")

        if product not in self._products:
            price = input_price()
            quantity = input_quantity()

            self._products[product] = ProductInfo(
                price=price,
                quantity=quantity
            )

            logger.info(
                f"Товар добавлен: {product}, "
                f"цена={price}, количество={quantity}"
            )

            print(
                f'\n{Back.GREEN}{Fore.BLACK}'
                f'Товар {product} добавлен на склад\n'
                f'{Style.RESET_ALL}'
            )
        else:
            logger.warning(
                f"Попытка добавить существующий товар: {product}"
            )

            print(
                f'\n{Back.RED}{Fore.BLACK}'
                f'Товар {product} уже есть на складе\n'
                f'Для изменения количества товара выберите пункт 3\n'
                f'{Style.RESET_ALL}'
            )

    def remove_product(self):
        product = input_product()
        logger.info(f"Попытка удаления товара: {product}")

        if product in self._products:
            del self._products[product]

            logger.info(f"Товар удален со склада: {product}")

            print(
                f'\n{Back.GREEN}{Fore.BLACK}'
                f'Товар {product} убран со склада\n'
                f'{Style.RESET_ALL}'
            )
        else:
            logger.warning(
                f"Попытка удалить отсутствующий товар: {product}"
            )

            print(
                f'\n{Back.RED}{Fore.BLACK}'
                f'Товар {product} отсутствует на складе\n'
                f'{Style.RESET_ALL}'
            )

    def change_quantity(self):
        product = input_product()
        logger.info(f"Попытка изменить количество: {product}")

        if product in self._products:
            quantity = input_quantity()
            self._products[product].quantity = quantity

            logger.info(
                f"Изменено количество товара {product}: "
                f"новое количество={quantity}"
            )

            print(
                f'\n{Back.GREEN}{Fore.BLACK}'
                f'Количество товара {product} изменено на '
                f'{self._products[product].quantity}\n'
                f'{Style.RESET_ALL}'
            )
        else:
            logger.warning(
                f"Попытка изменить количество отсутствующего товара: {product}"
            )

            print(
                f'\n{Back.RED}{Fore.BLACK}'
                f'Товар {product} отсутствует на складе\n'
                f'{Style.RESET_ALL}'
            )

    def change_price(self):
        product = input_product()
        logger.info(f"Попытка изменить цену: {product}")

        if product in self._products:
            price = input_price()
            self._products[product].price = price

            logger.info(
                f"Изменена цена товара {product}: "
                f"новая цена={price}"
            )

            print(
                f'\n{Back.GREEN}{Fore.BLACK}'
                f'Цена товара {product} изменена на '
                f'{self._products[product].price} BYN\n'
                f'{Style.RESET_ALL}'
            )
        else:
            logger.warning(
                f"Попытка изменить цену отсутствующего товара: {product}"
            )

            print(
                f'\n{Back.RED}{Fore.BLACK}'
                f'Товар {product} отсутствует на складе\n'
                f'{Style.RESET_ALL}'
            )
