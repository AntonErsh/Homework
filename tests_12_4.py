import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    if_frozen = False

    def setUp(self):
        try:
            self.first = Runner('Вося', -10)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        try:
            self.second = Runner(False, 5)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(if_frozen is True, '')
    def test_walk(self):
        for _ in range(10):
            self.first.walk()
        self.assertEqual(self.first.distance, 100, 'Must be 50')
        logging.info('"test_walk" выполнен успешно')

    @unittest.skipIf(if_frozen is True, '')
    def test_run(self):
        for _ in range(10):
            self.second.run()
        self.assertEqual(self.second.distance, 100, 'Must be 100')
        logging.info('"test_run" выполнен успешно')

    @unittest.skipIf(if_frozen is True, '')
    def test_challenge(self):
        toni_walk = Runner('Toni')
        lex_run = Runner('Alex')
        for _ in range(10):
            toni_walk.walk()
            lex_run.run()
        self.assertNotEqual(toni_walk.distance, lex_run.distance, "Must don't equal")
