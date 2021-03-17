import wx
from main_support import FrameAndItsStates

app = wx.App()
frame = FrameAndItsStates()
frame.Show()
app.MainLoop()

