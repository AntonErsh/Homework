import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

    def __lt__(self, other):
        return self.speed < other.speed


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        self.participants.sort(reverse=True)
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result_test_1 = {}
        cls.result_test_2 = {}
        cls.result_test_3 = {}

    def setUp(self):
        self.usain = Runner('Усейн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.result_test_1)
        print(cls.result_test_2)
        print(cls.result_test_3)

    def test_1(self):
        """
        This function are testing Tournament wint runners Usain and Nik
        :return: -> None
        """
        tournament_90 = Tournament(90, self.usain, self.nik)
        result = tournament_90.start()
        self.result_test_1.update(result)
        self.assertTrue(self.result_test_1.get(2) == self.nik)

    def test_2(self):
        """
        This function are testing Tournament with runners Andrew and Nik
        :return:  -> None
        """
        tournament_90 = Tournament(90, self.andrew, self.nik)
        result = tournament_90.start()
        self.result_test_2.update(result)
        self.assertTrue(self.result_test_2.get(2) == self.nik)

    def test_3(self):
        """
        This function are testing Tournament with runners Usain, Andrew and Nik
        :return:  -> None
        """
        tournament_90 = Tournament(90, self.usain, self.andrew, self.nik)
        result = tournament_90.start()
        self.result_test_3.update(result)
        self.assertTrue(self.result_test_3.get(3) == self.nik)

    def test_4(self):
        """
        This function are testing Tournament.start() 100 times
        with sort() for link the dependence place of speed
        :return: -> None
        """
        for n in range(10, 111):
            tour = Tournament(n, self.andrew, self.usain)
            result_dict = tour.start()
            self.assertFalse(result_dict.get(1) == self.andrew, 'должен быть Усейн на первом месте')
