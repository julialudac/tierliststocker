import wx
from main_support import MainSupport

app = wx.App()
frame = MainSupport()
frame.Show()
app.MainLoop()

