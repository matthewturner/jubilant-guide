from jubilant.queue import Queue
import time


class TestQueue(object):
    def some_action(self):
        print('Do something')

    def test_work_off_single_task(self):
        target = Queue()
        target.enqueue(self.some_action)
        target.work_off()
        assert(target.count == 0)
    
    def test_work_off_single_task_removes_processed_tasks(self):
        target = Queue()
        target.enqueue(self.some_action)
        target.work_off()
        assert(target.count_processed == 0)

    def test_task_repeats_automatically(self):
        target = Queue()
        target.enqueue(self.some_action, repeat=True)
        target.work_off()
        assert(target.count == 1)

    def test_task_repeats_automatically(self):
        target = Queue()
        target.enqueue(self.some_action, repeat=True)
        target.work_off()
        assert(target.count == 1)