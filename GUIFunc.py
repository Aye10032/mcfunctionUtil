import json

import wx
import os

MC_PATH = ''
MC_SAVE_PATH = ''
MC_Func_Path = ''
CONFIG_PATH = 'config'
CONFIG_FILE = 'config/data.json'
saves = []
data_packs = []

if not os.path.exists(CONFIG_PATH):
    os.mkdir(CONFIG_PATH)

if not os.path.exists(CONFIG_FILE):
    default_config = {
        "mc_path": "",
        "save_name": "",
        "function_name": ""
    }
    with open(CONFIG_FILE, 'w+') as conf:
        json.dump(default_config, conf, indent=4)


class StartWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 400),
                          style=wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU)
        panel = wx.Panel(self)

        wx.StaticText(panel, -1, 'MC路径:', (40, 40), (50, 50))
        self.path_text = wx.TextCtrl(panel, -1, MC_PATH, (100, 36), (310, 23))
        self.path_btn = wx.Button(panel, -1, '...', (417, 36), (25, 23))

        self.Bind(wx.EVT_BUTTON, self.set_path, self.path_btn)

        wx.StaticText(panel, -1, '选择存档:', (40, 80), (60, 50))
        self.save_text = wx.ComboBox(panel, -1, '', (110, 76), (310, 23), choices=saves, style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self.set_save, self.save_text)

        wx.StaticText(panel, -1, '选择数据包:', (40, 120), (70, 40))
        self.data_text = wx.ComboBox(panel, -1, '', (110, 116), (310, 23), choices=saves, style=wx.CB_READONLY)

        self.create_data_btn = wx.Button(panel, -1, '创建数据包', (100, 180), (70, 30))
        self.set_over_btn = wx.Button(panel, -1, '确定', (300, 180), (70, 30))

        self.Bind(wx.EVT_BUTTON, self.creat_data, self.create_data_btn)

        self.Center()
        self.Show(True)

    def init(self):
        with open(CONFIG_FILE, 'r') as conf:
            config = json.load(conf)

            global MC_PATH
            global MC_SAVE_PATH
            global MC_Func_Path

            if os.path.exists(config['function_name']):
                MC_PATH = config['mc_path']
                MC_SAVE_PATH = config['save_name']
                MC_Func_Path = config['function_name']

                this_saves = os.listdir(MC_SAVE_PATH)

                global saves
                for f in this_saves:
                    if os.path.isdir(MC_SAVE_PATH + '\\' + f):
                        saves.append(f)
                self.save_text.SetItems(saves)
                self.save_text.SetValue(os.path.basename(MC_SAVE_PATH))



    def set_path(self, event):
        dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            this_name = os.path.basename(dlg.GetPath())
            if this_name == '.minecraft':

                global MC_PATH
                MC_PATH = dlg.GetPath()
                self.path_text.SetValue(MC_PATH)

                global MC_SAVE_PATH
                MC_SAVE_PATH = MC_PATH + '\\saves'
                this_saves = os.listdir(MC_SAVE_PATH)

                global saves
                saves.clear()
                for f in this_saves:
                    if os.path.isdir(MC_SAVE_PATH + '\\' + f):
                        saves.append(f)
                self.save_text.SetItems(saves)
            else:
                box = wx.MessageDialog(None, '请选择.minecraft文件夹', '警告', wx.OK | wx.ICON_EXCLAMATION)
                box.ShowModal()

        dlg.Destroy()

    def set_save(self, event):
        global MC_SAVE_PATH
        MC_SAVE_PATH = MC_PATH + '\\save\\' + self.save_text.GetValue()

    def creat_data(self, event):
        this_data_path = MC_SAVE_PATH + '\\datapacks\\'

        dlg = wx.TextEntryDialog(self, '输入数据包名称', '新建数据包')

        if dlg.ShowModal() == wx.ID_OK:
            global MC_Func_Path
            MC_Func_Path = this_data_path + dlg.GetValue()

            if os.path.exists(MC_Func_Path):
                os.makedirs(MC_Func_Path)

            mcmeta = {
                "pack": {
                    "pack_format": 1,
                    "description": ""
                }
            }
            with open(MC_Func_Path + '\\pack.mcmeta', 'w') as pack:
                pack.write(str(mcmeta))

            os.makedirs(MC_Func_Path + '\\data\\minecraft\\tags\\functions')

        dlg.Destroy()


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 745),
                          style=wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU)

        self.CreateStatusBar()

        filemenu = wx.Menu()

        menu_mc_path = filemenu.Append(-1, "数据包路径", "选择所需数据包的路径")
        self.Bind(wx.EVT_MENU, self.setPath, menu_mc_path)
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)

        panel = wx.Panel(self)
        nb = wx.Notebook(panel)
        nb.AddPage(LinePanel(nb), '直线')
        nb.AddPage(ParabolaPanel(nb), '抛物线')

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        self.Center()
        self.Show(True)

    def setPath(self, event):
        dialog = wx.DirDialog(None, "Choose a directory:",
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            global MC_Func_Path
            MC_Func_Path = dialog.GetPath()
            print(MCFunc_Path)
        dialog.Destroy()


class LinePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t1 = wx.StaticText(self, -1, '个人设置', (0, 5), (600, -1), wx.ALIGN_CENTER)


class ParabolaPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        bt1 = wx.Button(self, -1, 'open', (0, 5), (10, 10))
        self.Bind(wx.EVT_BUTTON, self.open, bt1)

    def open(self, event):
        global MCFunc_Path
        wx.Execute("explorer " + MCFunc_Path)  # 打开所选目录


if __name__ == '__main__':
    app = wx.App(False)
    frame = StartWindow(None, "初始化")
    app.MainLoop()
