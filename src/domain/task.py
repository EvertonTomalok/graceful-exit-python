import logging
from time import sleep

from src.helpers.producer import produce_random_num


def generate_number_with_sleep(seconds=5):
    value_received = produce_random_num()
    sleep(seconds)
    logging.info(f"Value received was {value_received}")
