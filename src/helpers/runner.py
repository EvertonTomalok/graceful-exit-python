import logging
import signal
from collections import Callable


class Runner:
    def __init__(self):
        self.stopped = False

    def run(self, task: Callable, *args, **kwargs):
        while not self.stopped:
            task(*args, **kwargs)

    def stop(self, signal_received, frame):
        logging.warning(f"Graceful exiting ...")
        self.stopped = True


def create_runner_with_signal_to_stop() -> Runner:
    runner = Runner()

    signal.signal(signal.SIGINT, runner.stop)
    signal.signal(signal.SIGTERM, runner.stop)

    return runner
