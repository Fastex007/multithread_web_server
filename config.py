from dotenv import dotenv_values


class Config:
    """Загружает переменные окружения и настраивает конфиги."""

    def __init__(self) -> None:
        self.__env_variables = dotenv_values("env")

    def get_env(self, var_name: str, default: str = None) -> str:
        """Получает значение переменной окружения по имени."""

        return self.__env_variables.get(str(var_name), default)
