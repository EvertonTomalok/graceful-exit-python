from src.domain.task import generate_number_with_sleep
from src.helpers.runner import create_loop_runner_with_signal_to_stop


class SimpleLoopNumberGenerator:
    @staticmethod
    def run():
        loop_runner = create_loop_runner_with_signal_to_stop()
        loop_runner.run(generate_number_with_sleep, 2)
