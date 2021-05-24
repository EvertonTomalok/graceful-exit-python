import logging
import signal
from collections import Callable

from termcolor import colored


class LoopRunner:
    def __init__(self):
        self.stopped = False

    def run(self, task: Callable, *args, **kwargs):
        while not self.stopped:
            task(*args, **kwargs)

    def stop(self, signal_received, frame):
        logging.warning(colored("Graceful exiting ...", "green", attrs=["bold"]))
        self.stopped = True


def create_loop_runner_with_signal_to_stop() -> LoopRunner:
    loop_runner = LoopRunner()

    signal.signal(signal.SIGINT, loop_runner.stop)
    signal.signal(signal.SIGTERM, loop_runner.stop)

    return loop_runner
