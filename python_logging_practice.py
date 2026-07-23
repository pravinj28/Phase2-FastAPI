import logging
import os

logging.warning("Remain calm !!")

logging.debug("This is debug message")

logging.info("This is info message")

logging.error("This is an error message")

logging.critical("This is a critical message")

logging.basicConfig(level= logging.DEBUG, force= True)
logging.debug("This will get logged")

logging.basicConfig(format= "%(levelname)s:%(name)s:%(message)s")
logging.warning("Hello, warning !!")

logging.basicConfig(format= "{levelname}:{name}:{message}", style="{")
logging.warning("Hello, warning !!")

import logging

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.error("Something went wrong")


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)
name = "Avani Joshi"
logging.debug(f"{name}")

donuts = 5
guests = 1

try:
    donuts_per_guests = donuts/guests
except ZeroDivisionError:
    logging.error("DonutCalculationError", exc_info= True)


print("Done")

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode= "a", encoding= "utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.handlers
                                                                       
formatter = logging.Formatter(
    "{asctime}-{levelname}-{message}",
    style= "{",
    datefmt="%Y-%m-%d %H:%M",
)
console_handler.setFormatter(formatter)
logger.warning("Stay calm!")

logger2 = logging.getLogger(__name__)
logger2.level

logger2

logger2.parent

logger2.setLevel(logging.WARNING)

logger2.setLevel(10)
logger2.setLevel("INFO")

formatter = logging.Formatter("{levelname} - {message}", style="{")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.debug("Just checking in!")
logger.info("Just checking in, again!")





