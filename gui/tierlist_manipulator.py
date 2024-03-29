import requests


class TierlistManipulator:
    def __init__(self, tierlist_name):
        self.tierlist_name = tierlist_name

    def load_tier_list(self):
        url = "http://localhost:5000/tierlist/{}".format(self.tierlist_name)
        data = {}
        response = requests.get(url, data)
        return response.json()

    def get_all_items(self):
        tierlist = self.load_tier_list()
        return [item for items in tierlist.values() for item in items]

    def add(self, item, rank):
        url = "http://localhost:5000/tierlist/add"
        data = {
            'rank': rank,
            'item': item,
            'tierlist_name': self.tierlist_name
        }
        response = requests.post(url, json=data)
        print("Add operation status:", response.status_code)

    def remove(self, item):
        url = "http://localhost:5000/tierlist/del/{}/{}".format(self.tierlist_name, item)
        response = requests.delete(url)
        print("Delete operation status:", response.status_code)

    def switch_tierlist(self, new_tierlist_name):
        self.tierlist_name = new_tierlist_name