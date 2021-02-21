import wx

from tierlistformatter import TierlistFormatter


class MainSupport(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tierlist", size=(800, 300))
        self.draw_menu()

    def draw_menu(self):
        read_tierlist_button = wx.Button(self, 1, "Get tierlist", pos=(100, 100))
        read_tierlist_button.Bind(wx.EVT_BUTTON, self.draw_tierlist_table)
        wx.Button(self, 2, "Add item to tier", pos=(100, 125))
        wx.Button(self, 3, "Remove item", pos=(100, 150))

    def draw_tierlist_table(self, event):
        for child in self.GetChildren():
            child.Destroy()
        tierlist_formatter = TierlistFormatter()
        for ind, tier_items in enumerate(tierlist_formatter.tier_items_list):
            wx.StaticText(self, label=tier_items, pos=(10, 10 + ind * 25))


app = wx.App()
frame = MainSupport()
frame.Show()
app.MainLoop()

