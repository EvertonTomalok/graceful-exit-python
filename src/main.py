import logging
import os

from src.usecases.number_generator import SimpleLoopNumberGenerator

logging.basicConfig(
    format='[%(levelname)s][%(asctime)s] %(filename)s - %(message)s',
    level=os.environ.get("LOGLEVEL", "INFO"),
)


def start():
    SimpleLoopNumberGenerator.run()


if __name__ == "__main__":
    start()
