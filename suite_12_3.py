import unittest
import test_12_1
import test_12_2

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
