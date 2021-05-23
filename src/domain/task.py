from time import sleep
import logging

from src.helpers.producer import produce_random_num


def busy_work(seconds):
    value_received = produce_random_num()
    sleep(seconds)
    logging.info(f"Value received was {value_received}")
