class Thing:
    def __init__(self, name="Suitcases"):
        self.name = name

class Baggage:
    def __init__(self, thingname):
        self.thingname = thingname
        self.things = []
    def add_thing(self, suitcs):
        self.things.append(suitcs)
    def print_things_names(self):
        if self.things!=[]:
            print(f"---- Checked {self.thingname} in luggage: ----")
            for thns in self.things:
                print(thns.name)
        else:
            print(f"---- There are no checked-in {self.thingname} in luggage! ----")

thg1 = Thing("-> suitcase")
thg2 = Thing("-> bag")
thg3 = Thing("-> dog cell")
thg4 = Thing("-> skis")
thg5 = Thing("-> box")
thg6 = Thing("-> golf club")

ths = Baggage("things")

ths.add_thing(thg1)
ths.add_thing(thg2)
ths.add_thing(thg3)
ths.add_thing(thg4)
ths.add_thing(thg5)
ths.add_thing(thg6)

ths.print_things_names()