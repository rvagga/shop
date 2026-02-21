import logging
from logger_config import UserFilter

def test_logger_with_user_id(mocker):
    logger = logging.getLogger()
    mock_info = mocker.patch.object(logger, "info")
    user_filter = UserFilter(user_id=123)

    logger = logging.getLogger()
    logger.addFilter(user_filter)

    logger.info("Логирование с USER ID")
    mock_info.assert_called_once_with("Логирование с USER ID")

    #чек фильтра, который добавляет user-id лог