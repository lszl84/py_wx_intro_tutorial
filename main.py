import wx
from utils import ensure_hdpi

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.SetSize(self.FromDIP(wx.Size(400, 300)))
        self.panel = wx.Panel(self)

        self.fileContents = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.button = wx.Button(self.panel, label="Click me")
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.button)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.fileContents, 1, wx.EXPAND)
        self.sizer.Add(self.button, 0, wx.ALIGN_CENTER | wx.ALL, self.FromDIP(10))

        self.panel.SetSizer(self.sizer)

        self.Show(True)

    def OnButtonClicked(self, e):
        dialog = wx.FileDialog(self, "Open a file", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, 
                               wildcard="Text files (*.txt)|*.txt")
        if dialog.ShowModal() == wx.ID_OK:
            try:
                with open(dialog.GetPath(), 'r') as file:
                    self.fileContents.SetValue(file.read())
            except Exception as e:
                wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)


class MyApp(wx.App):
    def OnInit(self):
        
        ensure_hdpi()

        frame = MyFrame(None, "Simple wxPython App")
        frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

