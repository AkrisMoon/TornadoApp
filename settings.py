import os


class Settings:
    SQL_DATABASE = os.environ["SQL_DATABASE"]
    SQL_USER = os.environ["SQL_USER"]
    SQL_PASSWORD = os.environ["SQL_PASSWORD"]
    SQL_HOST = os.environ["SQL_HOST"]
    SQL_PORT = os.environ["SQL_PORT"]


settings = Settings()
