from src.domain.task import generate_number_with_sleep
from src.helpers.runner import create_runner_with_signal_to_stop


class SimpleLoopNumberGenerator:

    @staticmethod
    def run():
        runner = create_runner_with_signal_to_stop()
        runner.run(generate_number_with_sleep, 2)
