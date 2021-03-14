import wx
import widget_constants as wc


class Page:
    def __init__(self, panel):
        self.panel = panel

    def draw(self):
        self.panel.__clear__()


class AddItemPage(Page):
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
        self.panel.__draw_back_to_menu__()

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