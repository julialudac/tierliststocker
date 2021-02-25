import wx

from tierlistformatter import TierlistFormatter


class MainSupport(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tierlist", size=(800, 300))
        self.__draw_menu__()

    def __display_menu_page__(self, event):
        self.__draw_menu__()

    def __display_tierlist_page__(self, event):
        self.__clear__()
        self.__draw_tierlist_table__()
        self.__draw_back_to_menu__()

    def __draw_menu__(self):
        self.__clear__()
        read_tierlist_button = wx.Button(self, 1, "Get tierlist", pos=(100, 100))
        read_tierlist_button.Bind(wx.EVT_BUTTON, self.__display_tierlist_page__)
        wx.Button(self, 2, "Add item to tier", pos=(100, 125))
        wx.Button(self, 3, "Remove item", pos=(100, 150))

    def __draw_tierlist_table__(self):
        tierlist_formatter = TierlistFormatter()
        for ind, tier_items in enumerate(tierlist_formatter.tier_items_list):
            wx.StaticText(self, label=tier_items, pos=(10, 10 + ind * 25))

    def __draw_back_to_menu__(self):
        back_button = wx.Button(self, 4, "Back to Menu", pos=(650, 200))
        back_button.Bind(wx.EVT_BUTTON, self.__display_menu_page__)

    def __clear__(self):
        for child in self.GetChildren():
            child.Destroy()


app = wx.App()
frame = MainSupport()
frame.Show()
app.MainLoop()

