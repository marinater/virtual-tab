from timeit import default_timer as timer

class FPS:
	def __init__(self):
		self._frame_start = None

	def start_frame(self):
		self._frame_start = timer()

	def stop_frame(self):
		elapsed = timer() - self._frame_start
		self._frame_start = None
		return 1 / elapsed
