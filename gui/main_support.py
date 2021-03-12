import wx

from tierlistformatter import TierlistFormatter
from tierlist_manipulator import TierlistManipulator

# TODO julia make an enum of the button or text titles

RESPONSE_POS = (200, 100)


class MainSupport(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tierlist", size=(800, 300))
        self.selected_item = None
        self.selected_tier = None
        self.tierlist_manipulator = TierlistManipulator("tierlist")
        self.tierlist_selected_text = None
        self.__draw_menu__()

    def __display_menu_page__(self, event):
        self.__draw_menu__()

    def __display_tierlist_page__(self, event):
        self.__clear__()
        self.__draw_tierlist_table__()
        self.__draw_back_to_menu__()

    def __display_remove_item_page__(self, event):
        self.__clear__()
        self.__draw_remove_item_field__()
        self.__draw_back_to_menu__()

    def __display_add_item_page__(self, event):
        self.__clear__()
        self.__draw_add_item_widgets__()
        self.__draw_back_to_menu__()

    def __ask_new_tierlist__(self, event):
        dialog = wx.TextEntryDialog(self, "Please enter the name of the tierlist to switch to:", "New tierlist")
        dialog.ShowModal()
        user_input = dialog.GetValue()
        if user_input != "":
            self.tierlist_manipulator.switch_tierlist(user_input)
        self.tierlist_selected_text.SetLabel("Tierlist selected: " + self.tierlist_manipulator.tierlist_name)

    def __draw_menu__(self):
        self.__clear__()
        read_tierlist_button = wx.Button(self, 1, "Get tierlist", pos=(100, 100))
        read_tierlist_button.Bind(wx.EVT_BUTTON, self.__display_tierlist_page__)
        add_item_button = wx.Button(self, 2, "Add item to tier", pos=(100, 125))
        add_item_button.Bind(wx.EVT_BUTTON, self.__display_add_item_page__)
        remove_item_button = wx.Button(self, 3, "Remove item", pos=(100, 150))
        remove_item_button.Bind(wx.EVT_BUTTON, self.__display_remove_item_page__)
        self.tierlist_selected_text = wx.StaticText(self, label="Tierlist selected: "
                                                                + self.tierlist_manipulator.tierlist_name,
                                         pos=(200, 20))
        switch_tierlist_button = wx.Button(self, 10, "Switch tierlist", pos=(200, 40))
        switch_tierlist_button.Bind(wx.EVT_BUTTON, self.__ask_new_tierlist__)

    def __draw_tierlist_table__(self):
        try:
        tierlist_formatter = TierlistFormatter(self.tierlist_manipulator.tierlist_name)
        for ind, tier_items in enumerate(tierlist_formatter.tier_items_list):
            wx.StaticText(self, label=tier_items, pos=(10, 10 + ind * 25))
        except Exception as e:
            wx.StaticText(self, label=str(e), pos=(10, 10))

    def __draw_back_to_menu__(self):
        back_button = wx.Button(self, 4, "Back to Menu", pos=(650, 200))
        back_button.Bind(wx.EVT_BUTTON, self.__display_menu_page__)

    def __draw_add_item_widgets__(self):
        wx.StaticText(self, label="Name of the item to add:", pos=(10, 0))
        entered_item_field = wx.TextCtrl(self, 5, "", (10, 30))
        entered_item_field.Bind(wx.EVT_TEXT, self.__update_selected_item__)
        wx.StaticText(self, label="Tier of the item to add:", pos=(10, 50))
        tier_selection_list = wx.ListBox(self, pos=(10, 70), choices=["S", "A", "B", "C", "D", "E", "F"])
        tier_selection_list.Bind(wx.EVT_LISTBOX, self.__update_selected_rank)
        add_item_button = wx.Button(self, label="Add item!", pos=(200, 50))
        add_item_button.Bind(wx.EVT_BUTTON, self.__add_item_to_tierlist__)

    def __draw_remove_item_field__(self):
        try:
        wx.StaticText(self, label="Please select item to remove:", pos=(0, 0))
        choices = self.tierlist_manipulator.get_all_items()
        delete_selection = wx.ListBox(self, size=(100, -1), pos=(0, 20), choices=choices)
        delete_selection.Bind(wx.EVT_LISTBOX, self.__update_selected_item__)
        remove_button = wx.Button(self, 2, "Remove!", pos=(120, 150))
        remove_button.Bind(wx.EVT_BUTTON, self.__remove__tierlist__item)
        except Exception as e:
            wx.StaticText(self, label="An error occured. Please try later. Error: " + str(e), pos=RESPONSE_POS)

    def __update_selected_item__(self, event):
        # Case when we select the item (during delete action)
        self.selected_item = event.GetEventObject().GetStringSelection()
        # Case when we write the item (during add action)
        if not self.selected_item:
            self.selected_item = event.GetEventObject().GetValue()

    def __update_selected_rank(self, event):
        self.selected_tier = event.GetEventObject().GetStringSelection()

    def __add_item_to_tierlist__(self, event):
        print("Item to be added:", self.selected_item, "and selected rank:", self.selected_tier)
        try:
        self.tierlist_manipulator.add(self.selected_item,
                                      self.selected_tier)
            wx.StaticText(self, label="Item '{}' successfully added as a {}-tier!"
                                      .format(self.selected_item, self.selected_tier),
                          pos=RESPONSE_POS)
        except Exception as e:
            wx.StaticText(self, label=str(e), pos=RESPONSE_POS)

    def __remove__tierlist__item(self, event):
        if self.selected_item:
            try:
            self.tierlist_manipulator.remove(self.selected_item)
                wx.StaticText(self, label="Item '{}' successfully deleted!"
                              .format(self.selected_item),
                              pos=RESPONSE_POS)
            except Exception as e:
                wx.StaticText(self, label=str(e), pos=RESPONSE_POS)
        else:
            wx.StaticText(self, label="Please select an item!", pos=RESPONSE_POS)
        choices = self.tierlist_manipulator.get_all_items()
        listbox = self.GetChildren()[1]
        listbox.Set(choices)

    def __clear__(self):
        for child in self.GetChildren():
            child.Destroy()
