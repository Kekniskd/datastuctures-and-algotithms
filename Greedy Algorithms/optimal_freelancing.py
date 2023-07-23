# You recently started freelance software development and have been offered a variety of job opportunities. Each job has a deadline, meaning there is no value in completing the work after the deadline. Additionally, each job has an associated payment representing the profit for completing that job. Given this information, write a function that returns the maximum profit that can be obtained in a 7-day period.
#
# Each job will take 1 full day to complete, and the deadline will be given as the number of days left to complete the job. For example, if a job has a deadline of 1, then it can only be completed if it is the first job worked on. If a job has a deadline of 2, then it could be started on the first or second day.
#
# Note: There is no requirement to complete all the jobs. Only one job can be worked on at a time, meaning that in some scenarios it will be impossible to complete them all.
#
# Sample Input
# jobs = [
#   {"deadline": 1, "payment": 1},
#   {"deadline": 2, "payment": 1},
#   {"deadline": 2, "payment": 2}
# ]
#
# Sample Output
# 3 // Job 0 would be completed first, followed by job 2. Job 1 is not completed.

import unittest


def optimalFreelancing(jobs):
    LENGTH_OF_WEEK = 7
    profit = 0
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    timeline = [False] * LENGTH_OF_WEEK
    for job in jobs:
        maxTime = min((job["deadline"], LENGTH_OF_WEEK))
        for time in reversed(range(maxTime)):
            if not timeline[time]:
                timeline[time] = True
                profit += job["payment"]
                break
    return profit


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            {"deadline": 2, "payment": 1},
            {"deadline": 2, "payment": 2},
            {"deadline": 2, "payment": 3},
            {"deadline": 2, "payment": 4},
            {"deadline": 2, "payment": 5},
            {"deadline": 2, "payment": 6},
            {"deadline": 2, "payment": 7}
        ]
        expected = 13
        actual = optimalFreelancing(input)
        self.assertEqual(actual, expected)
