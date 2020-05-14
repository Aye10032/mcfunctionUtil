import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 745),
                          style=wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU)

        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        panel = wx.Panel(self)
        nb = wx.Notebook(panel)
        nb.AddPage(LinePanel(nb), '直线')
        nb.AddPage(ParabolaPanel(nb), '抛物线')

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        self.Center()
        self.Show(True)


class LinePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t1 = wx.StaticText(self, -1, '个人设置', (0, 5), (600, -1), wx.ALIGN_CENTER)


class ParabolaPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Sample editor")
    app.MainLoop()
