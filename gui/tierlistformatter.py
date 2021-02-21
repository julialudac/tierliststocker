import requests


# No longer a table :( But at least easier unit tests making
class TierlistFormatter():
    def __init__(self):
        self.tier_items_list = []
        self.fill()

    def fill(self):
        tierlist = self.load_tier_list()
        for k, v in tierlist.items():
            self.tier_items_list.append(k + ": " + ", ".join(v))

    def load_tier_list(self):
        url = "http://localhost:5000/tierlist/tierlist"
        data = {}
        response = requests.get(url, data)
        return response.json()
