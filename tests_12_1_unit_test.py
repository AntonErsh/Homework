import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        vasya_walk = Runner('Vasya')
        for _ in range(10):
            vasya_walk.walk()
        self.assertEqual(vasya_walk.distance, 50, 'Must be 50')

    def test_run(self):
        slava_run = Runner('Slava')
        for _ in range(10):
            slava_run.run()
        self.assertEqual(slava_run.distance, 100, 'Must be 100')

    def test_challenge(self):
        toni_walk = Runner('Toni')
        lex_run = Runner('Alex')
        for _ in range(10):
            toni_walk.walk()
            lex_run.run()
        self.assertNotEqual(toni_walk.distance, lex_run.distance, "Must don't equal")
