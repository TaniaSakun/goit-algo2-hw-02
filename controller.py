from typing import List, Dict
from functools import lru_cache
from dataclasses import dataclass


class TaskHandler:
    """
    Handles business logic for both tasks: 3D print job optimization and rod cutting problem.
    """

    @dataclass
    class PrintJob:
        id: str
        volume: float
        priority: int
        print_time: int

    @dataclass
    class PrinterConstraints:
        max_volume: float
        max_items: int

    class ThePrinter:
        def __init__(self, max_volume, max_items):
            self.max_volume = max_volume
            self.max_items = max_items
            self.total_time = 0
            self.current_times = [0]
            self.job_queue = []
            self.execute()

        def execute(self):
            self.total_time += max(self.current_times)
            self.current_free_volume = self.max_volume
            self.current_free_items = self.max_items
            self.current_times = [0]

        def add_job(self, job):
            if job['volume'] > self.max_volume:
                raise ValueError('Volume is too big')
            if job['volume'] > self.current_free_volume or self.current_free_items == 0:
                self.execute()
            self.job_queue.append(job['id'])
            self.current_times.append(job['print_time'])
            self.current_free_volume -= job['volume']
            self.current_free_items -= 1

        def get_statistics(self):
            self.execute()
            return {
                "print_order": self.job_queue,
                "total_time": self.total_time,
            }

    @staticmethod
    def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
        printer = TaskHandler.ThePrinter(constraints['max_volume'], constraints['max_items'])
        jobs_to_print = len(print_jobs)
        current_priority = 0

        while jobs_to_print > 0:
            current_priority += 1
            for job in print_jobs:
                if job['id'] in printer.job_queue:
                    continue
                if job["priority"] > current_priority:
                    continue
                printer.add_job(job)
                jobs_to_print -= 1
                if jobs_to_print == 0:
                    break

        return printer.get_statistics()

    @staticmethod
    @lru_cache(None)
    def rod_cutting_memo(length: int, prices: List[int]):
        if length == 0:
            return 0, []

        max_profit = 0
        best_cut = []
        for i in range(length):
            profit, cuts = TaskHandler.rod_cutting_memo(length - (i + 1), tuple(prices))
            profit += prices[i]
            if profit > max_profit:
                max_profit = profit
                best_cut = [i + 1] + cuts

        return max_profit, best_cut

    @staticmethod
    def rod_cutting_table(length: int, prices: List[int]):
        dp = [0] * (length + 1)
        cuts = [[] for _ in range(length + 1)]

        for n in range(1, length + 1):
            for i in range(1, n + 1):
                if i <= len(prices) and dp[n - i] + prices[i - 1] > dp[n]:
                    dp[n] = dp[n - i] + prices[i - 1]
                    cuts[n] = [i] + cuts[n - i]
        return {
            "max_profit": dp[length],
            "cuts": cuts[length],
            "number_of_cuts": len(cuts[length]) - 1
        }


class TaskController:
    """
    Manages user interactions, calls TaskHandler for execution, and displays results.
    """
    
    @staticmethod
    def run_tests():
        print("Running Print Job Optimization Tests:")
        constraints = {"max_volume": 300, "max_items": 2}
        jobs = [
            {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
        ]
        print(TaskHandler.optimize_printing(jobs, constraints))

        print("\nRunning Rod Cutting Problem Tests:")
        test_cases = [
            {"length": 5, "prices": [2, 5, 7, 8, 10]},
            {"length": 3, "prices": [1, 3, 8]},
            {"length": 4, "prices": [3, 5, 6, 7]}
        ]
        
        for test in test_cases:
            print(f"\nTesting rod length: {test['length']}, Prices: {test['prices']}")
            print("Memoization:", TaskHandler.rod_cutting_memo(test['length'], tuple(test['prices'])))
            print("Tabulation:", TaskHandler.rod_cutting_table(test['length'], test['prices']))


if __name__ == "__main__":
    TaskController.run_tests()
