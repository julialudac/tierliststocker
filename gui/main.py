import wx

from tierlisttable import TierlistTable

app = wx.App()
frame = wx.Frame(None, title="Tierlist", size=(800, 300))
TierlistTable(frame)
frame.Show()
app.MainLoop()