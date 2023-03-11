import logging
import os
import sys
from dataclasses import dataclass

from dotenv import dotenv_values


class Config:
    """Загружает переменные окружения и настраивает конфиги."""

    def __init__(self) -> None:
        self.__env_variables = dotenv_values(".env")

    def get_env(self, var_name: str, default: str = None) -> str:
        """Получает значение переменной окружения по имени."""

        return self.__env_variables.get(str(var_name), default)


class Logger:
    """Логгер."""

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.set_logger_config()

    @staticmethod
    def set_logger_config():
        logging.basicConfig(
            level=logging.INFO,
            format=(
                '%(asctime)s [%(levelname)s] - '
                '(%(filename)s).%(funcName)s:%(lineno)d - %(message)s'
            ),
            handlers=[
                logging.FileHandler(f'{Logger.BASE_DIR}/output.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )


@dataclass
class Parameters:
    """Параметры сервиса."""

    config = Config()
    Logger()
    logger = logging
    monitoring = None
