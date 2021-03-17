import wx

import pages
from tierlist_manipulator import TierlistManipulator


class FrameAndItsStates(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tierlist", size=(800, 300))
        self.selected_item = None
        self.tierlist_manipulator = TierlistManipulator("tierlist")
        self.tierlist_selected_text = None
        pages.MenuPage(self).draw()

