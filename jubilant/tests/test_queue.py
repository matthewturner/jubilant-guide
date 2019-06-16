from jubilant.queue import Queue, queue
from jubilant.queueable import Queueable as async
import time
import pytest


class TestQueue:
    @pytest.fixture
    def target(self):
        return Queue()

    def test_work_off_single_task(self, target):
        @async(delay=0, queue=target)
        def some_action_async():
            print('Do something')
        
        some_action_async()
        target.work_off()
        assert(target.count == 0)
    
    def test_work_off_single_task_removes_processed_tasks(self, target):
        @async(delay=0, queue=target)
        def some_action_async():
            print('Do something')
        
        some_action_async()
        target.work_off()
        assert(target.count_processed == 0)

    def test_task_repeats_automatically(self, target):
        @async(repeat=True, queue=target)
        def some_repeatable_action_async():
            print('Do something')
        
        some_repeatable_action_async()
        target.work_off()
        assert(target.count == 1)

    def test_task_can_be_repeated_twice(self, target):
        @async(repeat=True, queue=target)
        def some_repeatable_action_async():
            print('Do something')
        
        some_repeatable_action_async()
        target.work_off()
        target.work_off()
        assert(target.count == 1)

    def test_instance_task_can_be_repeated(self, target):
        class Something:
            @async(repeat=True, queue=target)
            def some_repeatable_action_async(self):
                print('Do something')
        something = Something()
        something.some_repeatable_action_async()
        target.work_off()
        target.work_off()
        assert(target.count == 1)