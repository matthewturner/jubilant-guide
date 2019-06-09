from jubilant import WheelDriver, queue
import time
import pytest


class TestMotion:
    @pytest.fixture
    def motion(self):
        return WheelDriver()

    def test_turn_right(self, motion):
        motion.turn_right(90)
        assert(motion.is_manoevring())

    def test_turn_left(self, motion):
        motion.turn_left(90)
        assert(motion.is_manoevring())

    def test_turn_right_for_specific_period(self, motion):
        start = time.monotonic()
        motion.turn_right(90)
        while queue.count > 0:
            queue.work_off()
        end = time.monotonic()
        duration = end - start
        assert(round(duration, 1) == 0.5)
        assert(not motion.is_manoevring())