import logging
import os

from src.domain.task import busy_work
from src.helpers.runner import create_runner_with_signal_to_stop

logging.basicConfig(
    format='[%(levelname)s][%(asctime)s] %(filename)s - %(message)s',
    level=os.environ.get("LOGLEVEL", "INFO")
)


def start():
    runner = create_runner_with_signal_to_stop()
    runner.run(busy_work, 2)


if __name__ == "__main__":
    start()
