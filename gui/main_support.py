import wx

from tierlistformatter import TierlistFormatter
from tierlist_manipulator import TierlistManipulator

# TODO julia regroup well the classes

import widget_constants as wc
import pages


class MainSupport(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tierlist", size=(800, 300))
        self.selected_item = None
        self.tierlist_manipulator = TierlistManipulator("tierlist")
        self.tierlist_selected_text = None
        self.widget_name_and_id = {
            "Get tierlist": 1,
            "Add item to tier": 2,
            "Remove item": 3,
            "Back to Menu": 4,
            "<entered_item_field>": 5,
            "Remove!": 6
        }
        self.__draw_menu__()

    def __display_menu_page__(self, event):
        self.__draw_menu__()

    def __display_tierlist_page__(self, event):
        self.__clear__()
        self.__draw_tierlist_table__()
        self.__draw_back_to_menu__()

    def __display_remove_item_page__(self, event):
        pages.RemoveItemPage(self).draw()

    def __display_add_item_page__(self, event):
        pages.AddItemPage(self).draw()

    def __ask_new_tierlist__(self, event):
        dialog = wx.TextEntryDialog(self, "Please enter the name of the tierlist to switch to:", "New tierlist")
        dialog.ShowModal()
        user_input = dialog.GetValue()
        if user_input != "":
            self.tierlist_manipulator.switch_tierlist(user_input)
        self.tierlist_selected_text.SetLabel("Tierlist selected: " + self.tierlist_manipulator.tierlist_name)

    def __draw_menu__(self):
        self.__clear__()
        read_tierlist_button = wx.Button(self, self.widget_name_and_id["Get tierlist"],
                                         "Get tierlist", pos=(wc.CLASSIC_COORDINATE_VALUE, wc.CLASSIC_COORDINATE_VALUE))
        read_tierlist_button.Bind(wx.EVT_BUTTON, self.__display_tierlist_page__)
        add_item_button = wx.Button(self, self.widget_name_and_id["Add item to tier"],
                                    "Add item to tier", pos=(wc.CLASSIC_COORDINATE_VALUE, wc.CLASSIC_COORDINATE_VALUE +
                                                             wc.LINE_HEIGHT))
        add_item_button.Bind(wx.EVT_BUTTON, self.__display_add_item_page__)
        remove_item_button = wx.Button(self, self.widget_name_and_id["Remove item"], "Remove item",
                                       pos=(wc.CLASSIC_COORDINATE_VALUE, wc.CLASSIC_COORDINATE_VALUE + 2*wc.LINE_HEIGHT))
        remove_item_button.Bind(wx.EVT_BUTTON, self.__display_remove_item_page__)
        self.tierlist_selected_text = wx.StaticText(self, label="Tierlist selected: "
                                                                + self.tierlist_manipulator.tierlist_name,
                                         pos=(200, wc.LINE_HEIGHT))
        switch_tierlist_button = wx.Button(self, 10, "Switch tierlist", pos=(200, 2*wc.LINE_HEIGHT))
        switch_tierlist_button.Bind(wx.EVT_BUTTON, self.__ask_new_tierlist__)

    def __draw_tierlist_table__(self):
        try:
            tierlist_formatter = TierlistFormatter(self.tierlist_manipulator.tierlist_name)
            for ind, tier_items in enumerate(tierlist_formatter.tier_items_list):
                wx.StaticText(self, label=tier_items, pos=(10, 10 + ind * wc.LINE_HEIGHT))
        except Exception as e:
            wx.StaticText(self, label=str(e), pos=(10, 10))

    def __draw_back_to_menu__(self):
        back_button = wx.Button(self, self.widget_name_and_id["Back to Menu"], "Back to Menu", pos=(650, 200))
        back_button.Bind(wx.EVT_BUTTON, self.__display_menu_page__)

    def __clear__(self):
        for child in self.GetChildren():
            child.Destroy()
