import os
import random

FACTOR_MULTIPLY = float(os.getenv("FACTOR_MULTIPLY", 100))


def produce_random_num():
    return int(random.random() * 100)
