import pytest
from menu import main_menu, cashier_menu, warehouse_menu
from logger_config import logger


def test_main_menu(mocker):
    mocker.patch("builtins.input", return_value="1")
    mock_logger = mocker.patch("menu.logger.info")
    result = main_menu()

    assert result == "1"
    mock_logger.assert_called_once_with("Главное меню: выбор 1")


def test_cashier_menu(mocker):
    mocker.patch("builtins.input", return_value="7")
    mock_logger = mocker.patch("menu.logger.info")
    result = cashier_menu()

    assert result == "7"
    mock_logger.assert_called_once_with("Касса: выбор 7")


def test_warehouse_menu(mocker):
    mocker.patch("builtins.input", return_value="566")
    mock_logger = mocker.patch("menu.logger.info")
    result = warehouse_menu()

    assert result == "566"
    mock_logger.assert_called_once_with("Управление: выбор 566")

    #чек инпута и его вывода в каждой функции + логгер