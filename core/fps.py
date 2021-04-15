from timeit import default_timer as timer

class FPS:
	def __init__(self):
		self.frame_start = None

	def start_frame(self):
		self.frame_start = timer()

	def stop_frame(self):
		elapsed = timer() - self.frame_start
		self.frame_start = None
		return 1 / elapsed
