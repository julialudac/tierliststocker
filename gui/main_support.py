import wx

from tierlistformatter import TierlistFormatter
from tierlist_manipulator import TierlistManipulator


class MainSupport(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tierlist", size=(800, 300))
        self.__draw_menu__()
        self.item_to_delete = None
        self.tierlist_manipulator = TierlistManipulator("tierlist")

    def __display_menu_page__(self, event):
        self.__draw_menu__()

    def __display_tierlist_page__(self, event):
        self.__clear__()
        self.__draw_tierlist_table__()
        self.__draw_back_to_menu__()

    def __display_remove_item_page__(self, event):
        self.__clear__()
        self.__draw_remove_item_field()
        self.__draw_back_to_menu__()

    def __draw_menu__(self):
        self.__clear__()
        read_tierlist_button = wx.Button(self, 1, "Get tierlist", pos=(100, 100))
        read_tierlist_button.Bind(wx.EVT_BUTTON, self.__display_tierlist_page__)
        wx.Button(self, 2, "Add item to tier", pos=(100, 125))
        remove_item_button = wx.Button(self, 3, "Remove item", pos=(100, 150))
        remove_item_button.Bind(wx.EVT_BUTTON, self.__display_remove_item_page__)

    def __draw_tierlist_table__(self):
        tierlist_formatter = TierlistFormatter()
        for ind, tier_items in enumerate(tierlist_formatter.tier_items_list):
            wx.StaticText(self, label=tier_items, pos=(10, 10 + ind * 25))

    def __draw_back_to_menu__(self):
        back_button = wx.Button(self, 4, "Back to Menu", pos=(650, 200))
        back_button.Bind(wx.EVT_BUTTON, self.__display_menu_page__)

    # TODO
    def __draw_add_item_widgets(self):
        pass

    def __draw_remove_item_field(self):
        wx.StaticText(self, label="Please select item to remove:", pos=(0, 0))
        choices = self.tierlist_manipulator.get_all_items()
        delete_selection = wx.ListBox(self, size=(100, -1), pos=(0, 20), choices=choices)
        delete_selection.Bind(wx.EVT_LISTBOX, self.__update_item_to_delete__)
        remove_button = wx.Button(self, 2, "Remove!", pos=(120, 150))
        remove_button.Bind(wx.EVT_BUTTON, self.__remove__tierlist__item)

    def __update_item_to_delete__(self, event):
        self.item_to_delete = event.GetEventObject().GetStringSelection()

    def __remove__tierlist__item(self, event):
        if self.item_to_delete:
            print(self.item_to_delete, "deleted!!!")
            self.tierlist_manipulator.remove(self.item_to_delete)
        choices = self.tierlist_manipulator.get_all_items()
        listbox = self.GetChildren()[1]
        listbox.Set(choices)

    def __clear__(self):
        for child in self.GetChildren():
            child.Destroy()
