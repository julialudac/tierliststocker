from tierlist_manipulator import TierlistManipulator


# No longer a table :( But at least easier unit tests making
class TierlistFormatter():
    def __init__(self, tierlist_name):
        self.tier_items_list = []
        self.fill(tierlist_name)

    def fill(self, tierlist_name):
        tierlist_manip = TierlistManipulator(tierlist_name)
        tierlist = tierlist_manip.load_tier_list()
        for k, v in tierlist.items():
            self.tier_items_list.append(k + ": " + ", ".join(v))
