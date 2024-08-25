class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


runnerY = Runner("Усэйн", 10)
runnerA = Runner("Андрей", 9)
runnerN = Runner("Ник", 3)

tournament = Tournament(90, runnerA, runnerY, runnerN)
finishers = tournament.start()
finishers_str = {}
for f in finishers:
    finishers_str.update({f: str(finishers[f])})
    # print(finishers[f])
print(str(finishers_str).replace("'", ""))
print(max(finishers.keys()))

a = max(finishers.keys())
print(finishers[a])


