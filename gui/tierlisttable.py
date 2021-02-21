import wx.grid as grid
import requests


class TierlistTable(grid.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)
        self.CreateGrid(7, 1)
        self.SetColMinimalWidth(0, 600)
        self.SetColLabelValue(0, "Items")
        self.SetRowLabelValue(0, "S")
        self.SetRowLabelValue(1, "A")
        self.SetRowLabelValue(2, "B")
        self.SetRowLabelValue(3, "C")
        self.SetRowLabelValue(4, "D")
        self.SetRowLabelValue(5, "E")
        self.SetRowLabelValue(6, "F")
        self.fill()

    def fill(self):
        tierlist = self.get_tier_list()
        ranks = ["S", "A", "B", "C", "D", "E", "F"]
        for k, v in tierlist.items():
            self.SetCellValue(ranks.index(k), 0, ", ".join(v))

    def get_tier_list(self):
        url = "http://localhost:5000/tierlist/tierlist"
        data = {}
        response = requests.get(url, data)
        return response.json()
