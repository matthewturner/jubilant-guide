from jubilant import motion
from jubilant.queue import queue
import time


class TestMotion(object):
    def test_turn_right(self):
        motion.turn_right(90)
        assert(motion.is_manoevring())

    def test_turn_left(self):
        motion.turn_left(90)
        assert(motion.is_manoevring())

    def test_turn_right_for_specific_period(self):
        start = time.monotonic()
        motion.turn_right(90)
        while queue.count > 0:
            queue.work_off()
        end = time.monotonic()
        duration = end - start
        assert(round(duration, 1) == 0.5)
        assert(not motion.is_manoevring())