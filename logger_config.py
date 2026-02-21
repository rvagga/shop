import logging

class UserFilter(logging.Filter):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    def filter(self, record):
        record.user_id = self.user_id
        return True

logging.basicConfig(
    filename="store.log",
    level=logging.INFO,
    format="%(asctime)s | USER %(user_id)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()

logger.addFilter(UserFilter(user_id=123))

logger.info("Логирование с USER ID")
