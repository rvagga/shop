from logger_config import logger

from Inputs import input_product, input_quantity
from Warehouse import Warehouse, ProductInfo
from colorama import Fore, Back, Style


class Cashier(Warehouse):
    def __init__(self):
        super().__init__()
        self._sold_products = {}
        self._total_sales = 0
        self._total_income = 0
        logger.info("Инициализирован класс Cashier")

    def __str__(self):
        if self._sold_products:
            header = f'\n{Back.YELLOW}{Fore.BLACK}Отчет за смену:\n'
            report_lines = []

            for i, (product, info) in enumerate(self._sold_products.items(), 1):
                report_lines.append(
                    f'{i}. Товар: {product}. '
                    f'Всего продано: {info.quantity}, '
                    f'на сумму: {info.price} BYN.'
                )

            footer = (
                f'\n\nВсего продаж: {self._total_sales}. '
                f'Общая выручка: {self._total_income:.2f} BYN\n{Style.RESET_ALL}'
            )
            return header + '\n'.join(report_lines) + footer
        else:
            return f'\n{Back.RED}{Fore.BLACK}Продажи отсутствуют\n{Style.RESET_ALL}'

    def sell_product(self):
        product = input_product()
        logger.info(f"Попытка продажи товара: {product}")

        if product in self._products:
            quantity = input_quantity()
            total_price = self._products[product].price * quantity

            logger.info(
                f"Найден товар {product}: "
                f"запрошено={quantity}, "
                f"остаток={self._products[product].quantity}"
            )

            if quantity == self._products[product].quantity:
                print(
                    f'\n{Back.GREEN}{Fore.BLACK}'
                    f'Товар {product} продан в количестве {quantity}\n'
                    f'Общая стоимость: {total_price} BYN\n'
                    f'ТОВАР ЗАКОНЧИЛСЯ НА СКЛАДЕ\n{Style.RESET_ALL}'
                )

                del self._products[product]

                logger.info(
                    f"Товар {product} распродан полностью. "
                    f"Продано={quantity}, сумма={total_price}"
                )

                self.sales_report(product, quantity, total_price)

            elif quantity < self._products[product].quantity:
                self._products[product].quantity -= quantity

                logger.info(
                    f"Частичная продажа {product}: "
                    f"продано={quantity}, "
                    f"остаток={self._products[product].quantity}, "
                    f"сумма={total_price}"
                )

                print(
                    f'\n{Back.GREEN}{Fore.BLACK}'
                    f'Товар {product} продан в количестве {quantity}\n'
                    f'Общая стоимость: {total_price} BYN\n'
                    f'Остаток на складе: {self._products[product].quantity}\n'
                    f'{Style.RESET_ALL}'
                )

                self.sales_report(product, quantity, total_price)

            else:
                print(
                    f'\n{Back.RED}{Fore.BLACK}'
                    f'Количество {quantity} превышает остаток на складе! '
                    f'({self._products[product].quantity})\n{Style.RESET_ALL}'
                )

                logger.warning(
                    f"Ошибка продажи {product}: "
                    f"запрошено={quantity}, "
                    f"остаток={self._products[product].quantity}"
                )

        else:
            print(
                f'\n{Back.RED}{Fore.BLACK}'
                f'Товар {product} отсутствует на складе\n{Style.RESET_ALL}'
            )

            logger.warning(
                f"Попытка продажи отсутствующего товара: {product}"
            )

    def sales_report(self, product, quantity, total_price):
        self._total_sales += quantity
        self._total_income += total_price

        if product not in self._sold_products:
            self._sold_products[product] = ProductInfo(
                price=total_price,
                quantity=quantity
            )
        else:
            self._sold_products[product].price += total_price
            self._sold_products[product].quantity += quantity

        logger.info(
            f"Обновлен отчет продаж: "
            f"{product}, +{quantity} шт, +{total_price} BYN | "
            f"Итого продаж={self._total_sales}, "
            f"выручка={self._total_income:.2f}"
        )
