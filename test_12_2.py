import module_12_2 as m
import unittest as u


class TournamentTest(u.TestCase):

    @classmethod
    def setUpClass(cls):
        TournamentTest.all_result = {}

    def setUp(self):
        self.runnerY = m.Runner("Усэйн", 10)
        self.runnerA = m.Runner("Андрей", 9)
        self.runnerN = m.Runner("Ник", 3)

    def testTournament(self):
        self.tournament = m.Tournament(90, self.runnerY, self.runnerN)
        finishers = self.tournament.start()
        a = max(finishers.keys())
        self.assertEquals(finishers[a], 'Ник')
        finishers_str = {}
        for f in finishers:
            finishers_str.update({f: str(finishers[f])})
        TournamentTest.all_result.update({1: str(finishers_str).replace("'", "")})

    def testTournament2(self):
        self.tournament = m.Tournament(90, self.runnerA, self.runnerN)
        finishers = self.tournament.start()
        a = max(finishers.keys())
        self.assertEquals(finishers[a], 'Ник')
        finishers_str = {}
        for f in finishers:
            finishers_str.update({f: str(finishers[f])})
        TournamentTest.all_result.update({2: str(finishers_str).replace("'", "")})

    def testTournament3(self):
        self.tournament = m.Tournament(90, self.runnerA, self.runnerY, self.runnerN)
        finishers = self.tournament.start()
        a = max(finishers.keys())
        self.assertEquals(finishers[a], 'Ник')
        finishers_str = {}
        for f in finishers:
            finishers_str.update({f: str(finishers[f])})
        TournamentTest.all_result.update({3: str(finishers_str).replace("'", "")})

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_result:
            print(TournamentTest.all_result[i])

if __name__ == '__main__':
    u.main()
