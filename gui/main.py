import wx
from frame_and_states import FrameAndItsStates

app = wx.App()
frame = FrameAndItsStates()
frame.Show()
app.MainLoop()

