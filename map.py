class Map:
    def __init__(self):
        self.explorableareas = []
        self.allAreas = [{"id" : 1, "name" : "Weird Woods", "lvlreq" : 1},
                         {"id" : 2, "name" : "Slug Swamp", "lvlreq" : 6}]

    def lvlCheck(self, playerlevel):
        for area in self.allAreas:
            if playerlevel >= area["lvlreq"]:
                self.explorableareas.append(area)
                self.allAreas.pop(area["id"] - 1)
    

    def areaP(self):
        print(self.explorableareas)
        print(self.allAreas)
        input()