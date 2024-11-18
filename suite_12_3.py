import unittest
import tests_12_3


test_12_2_TS = unittest.TestSuite()
test_12_2_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_12_2_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
test_text = unittest.TextTestRunner(verbosity=2)
test_text.run(test_12_2_TS)
