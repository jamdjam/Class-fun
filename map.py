from huntable_camps import wolf, wolfEasy

class Map:
    def __init__(self):
        self.explorableareas = []
        self.allAreas = [{"id" : 1, "name" : "Weird Woods", "lvlreq" : 1},
                         {"id" : 2, "name" : "Slug Swamp", "lvlreq" : 6}]

    def lvlCheck(self, playerlevel):
        for area in self.allAreas:
            ind = 0
            if playerlevel >= area["lvlreq"]:
                self.explorableareas.append(area)
                self.allAreas.pop(ind)
            ind += 1
    

    def areaP(self):
        print(self.explorableareas)
        print(self.allAreas)
        input()

class weird_woods:
    def __init__(self):
        None

        