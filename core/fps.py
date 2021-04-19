from timeit import default_timer as timer
from collections import deque

max_queue_length = 30


class FPS:
    def __init__(self):
        self._frame_start = None
        self.prev_rates = deque()

    def start_frame(self):
        self._frame_start = timer()
        if len(self.prev_rates) > max_queue_length:
            self.prev_rates.popleft()

    def stop_frame(self):
        elapsed = timer() - self._frame_start
        self._frame_start = None
        self.prev_rates.append(1 / elapsed)

        return sum(self.prev_rates) / len(self.prev_rates)
