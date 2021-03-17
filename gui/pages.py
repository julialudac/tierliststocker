import wx
import widget_constants as wc

from tierlistformatter import TierlistFormatter


class ActionPage:
    def __init__(self, panel):
        self.panel = panel

    def draw(self):
        self.__clear__()
        self.__draw_back_to_menu__()

    def __clear__(self):
        for child in self.panel.GetChildren():
            child.Destroy()

    def __draw_back_to_menu__(self):
        back_button = wx.Button(self.panel, wc.widget_name_and_id["Back to Menu"], "Back to Menu", pos=(650, 200))
        back_button.Bind(wx.EVT_BUTTON, self.panel.__display_menu_page__)


class AddItemPage(ActionPage):
    def __init__(self, panel):
        super().__init__(panel)
        self.selected_item = None
        self.selected_tier = None

    def draw(self):
        super().draw()
        wx.StaticText(self.panel, label="Name of the item to add:", pos=(10, 0))
        entered_item_field = wx.TextCtrl(self.panel, wc.widget_name_and_id["<entered_item_field>"],
                                         "", (10, wc.LINE_HEIGHT))
        entered_item_field.Bind(wx.EVT_TEXT, self.__update_selected_item__)
        wx.StaticText(self.panel, label="Tier of the item to add:", pos=(10, 2 * wc.LINE_HEIGHT))
        tier_selection_list = wx.ListBox(self.panel, pos=(10, 70), choices=["S", "A", "B", "C", "D", "E", "F"])
        tier_selection_list.Bind(wx.EVT_LISTBOX, self.__update_selected_rank)
        add_item_button = wx.Button(self.panel, label="Add item!", pos=(200, 2 * wc.LINE_HEIGHT))
        add_item_button.Bind(wx.EVT_BUTTON, self.__add_item_to_tierlist__)

    def __update_selected_item__(self, event):
        self.selected_item = event.GetEventObject().GetValue()

    def __update_selected_rank(self, event):
        self.selected_tier = event.GetEventObject().GetStringSelection()

    def __add_item_to_tierlist__(self, event):
        print("Item to be added:", self.selected_item, "and selected rank:", self.selected_tier)
        try:
            self.panel.tierlist_manipulator.add(self.selected_item,
                                          self.selected_tier)
            wx.StaticText(self.panel, label="Item '{}' successfully added as a {}-tier!"
                                      .format(self.selected_item, self.selected_tier),
                          pos=wc.RESPONSE_POS)
        except Exception as e:
            wx.StaticText(self.panel, label=str(e), pos=wc.RESPONSE_POS)


class RemoveItemPage(ActionPage):
    def __init__(self, panel):
        super().__init__(panel)
        self.selected_item = None

    def draw(self):
        super().draw()
        try:
            wx.StaticText(self.panel, label="Please select item to remove:", pos=(0, 0))
            choices = self.panel.tierlist_manipulator.get_all_items()
            delete_selection = wx.ListBox(self.panel, size=(100, -1), pos=(0, wc.LINE_HEIGHT), choices=choices)
            delete_selection.Bind(wx.EVT_LISTBOX, self.__update_selected_item__)
            remove_button = wx.Button(self.panel, wc.widget_name_and_id["Remove!"], "Remove!",
                                      pos=(wc.CLASSIC_COORDINATE_VALUE + wc.LINE_HEIGHT,
                                           wc.CLASSIC_COORDINATE_VALUE + 2*wc.LINE_HEIGHT))
            remove_button.Bind(wx.EVT_BUTTON, self.__remove__tierlist__item)
        except Exception as e:
            wx.StaticText(self.panel, label="An error occured. Please try later. Error: " + str(e), pos=wc.RESPONSE_POS)

    def __update_selected_item__(self, event):
        self.selected_item = event.GetEventObject().GetStringSelection()

    def __remove__tierlist__item(self, event):
        if self.selected_item:
            try:
                self.panel.tierlist_manipulator.remove(self.selected_item)
                wx.StaticText(self.panel, label="Item '{}' successfully deleted!"
                              .format(self.selected_item),
                              pos=wc.RESPONSE_POS)
            except Exception as e:
                wx.StaticText(self.panel, label=str(e), pos=wc.RESPONSE_POS)
        else:
            wx.StaticText(self.panel, label="Please select an item!", pos=wc.RESPONSE_POS)
        choices = self.panel.tierlist_manipulator.get_all_items()
        listbox = self.panel.GetChildren()[2]  # 2 means the listbox which is the 3rd child
        listbox.Set(choices)


class DisplayTierlistPage(ActionPage):
    def draw(self):
        super().draw()
        try:
            tierlist_formatter = TierlistFormatter(self.panel.tierlist_manipulator.tierlist_name)
            for ind, tier_items in enumerate(tierlist_formatter.tier_items_list):
                wx.StaticText(self.panel, label=tier_items, pos=(10, 10 + ind * wc.LINE_HEIGHT))
        except Exception as e:
            wx.StaticText(self.panel, label=str(e), pos=(10, 10))

