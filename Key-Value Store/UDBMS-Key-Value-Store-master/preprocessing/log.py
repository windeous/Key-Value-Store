import logging


def get_logger(name: str = __name__) -> logging.Logger:
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
