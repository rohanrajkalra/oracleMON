#Boa:Frame:ventPrincFrame

import wx
import wx.grid

def create(parent):
    return ventPrincFrame(parent)

[wxID_VENTPRINCFRAME, wxID_VENTPRINCFRAMESTATICBITMAP1, 
 wxID_VENTPRINCFRAMESTATUSBAR1, wxID_VENTPRINCFRAMETOOLBAR1, 
] = [wx.NewId() for _init_ctrls in range(4)]

[wxID_VENTPRINCFRAMETOOLBAR1CONECTAR_ID, 
 wxID_VENTPRINCFRAMETOOLBAR1DESCONECTAR_ID, 
 wxID_VENTPRINCFRAMETOOLBAR1SALIR_ID, 
] = [wx.NewId() for _init_coll_toolBar1_Tools in range(3)]

class ventPrincFrame(wx.Frame):
    

    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'img/knetattach.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1CONECTAR_ID, kind=wx.ITEM_NORMAL,
              label=u'Conectar', longHelp=u'Conectar a oracle',
              shortHelp=u'Conectar')
        parent.DoAddTool(bitmap=wx.Bitmap(u'img/kt-stop.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1DESCONECTAR_ID, kind=wx.ITEM_NORMAL,
              label=u'Desconectar', longHelp=u'Desconectar',
              shortHelp=u'Desconectar')
        parent.DoAddTool(bitmap=wx.Bitmap(u'img/quassel_message.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1SALIR_ID, kind=wx.ITEM_NORMAL,
              label=u'Salir', longHelp=u'Salir', shortHelp=u'Salir')
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Conectar_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1CONECTAR_ID)
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Desconectar_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1DESCONECTAR_ID)
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Salir_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1SALIR_ID)

        parent.Realize()

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(3)

        parent.SetStatusText(number=0, text=u'Desconectado')
        parent.SetStatusText(number=1, text=u'Destino')
        parent.SetStatusText(number=2, text=u'')

        parent.SetStatusWidths([-3, -1, 30])

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_VENTPRINCFRAME, name=u'ventPrincFrame',
              parent=prnt, pos=wx.Point(416, 206), size=wx.Size(960, 533),
              style=wx.DEFAULT_FRAME_STYLE, title=u'oracleMON')
        self.SetClientSize(wx.Size(960, 533))
        self.SetToolTipString(u'oracleMON')
        self.Center(wx.BOTH)

        self.toolBar1 = wx.ToolBar(id=wxID_VENTPRINCFRAMETOOLBAR1,
              name='toolBar1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(106, 38), style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.SetToolBar(self.toolBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_VENTPRINCFRAMESTATUSBAR1,
              name='statusBar1', parent=self, style=1)
        self.statusBar1.SetStatusText(u'Desconectado')
        self.statusBar1.SetThemeEnabled(False)
        self.statusBar1.SetLabel(u'')
        self.statusBar1.SetHelpText(u'')
        self.statusBar1.SetToolTipString(u'Estado de la conexion')
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'img/red.png',
              wx.BITMAP_TYPE_PNG), id=wxID_VENTPRINCFRAMESTATICBITMAP1,
              name='staticBitmap1', parent=self.statusBar1, pos=wx.Point(936,
              8), size=wx.Size(24, 24), style=0)

        self._init_coll_toolBar1_Tools(self.toolBar1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnToolBar1Conectar_idTool(self, event):
        import conectar
        dlg = conectar.ConDialogClass(self, -1, '')
        run = dlg.ShowModal()
        user = dlg.UserText.GetValue()
        passwd = dlg.PassText.GetValue()
        sid = dlg.SidText.GetValue()
        if len(user) == 0:
            print "Falta usuario"
            dlg.Destroy()
        elif  len(passwd) == 0:
            print "Falta password"
            dlg.Close()
        elif len(sid) == 0:
            print "Faltan sid"
            dlg.Close()
        else:
            print "Vamos a conectar"
            import cx_Oracle
            import sys
            (user,passwd,sid) = (str(dlg.UserText.GetValue()),str(dlg.PassText.GetValue()),str(dlg.SidText.GetValue()))
            print "DATOS DE CONEXION: Usuario: "+ user +" Pass: "+ passwd + " SID: "+ sid
            try:
                connection = cx_Oracle.connect( user , passwd , sid )
                print "Conectado a oracle"
                global conectado
                conectado = "TRUE"
                constring = user+"@"+sid
                self.statusBar1.SetStatusText("Conectado",0)
                self.statusBar1.SetStatusText(constring,1)
                self.staticBitmap1.SetBitmap(u'imp/green.png')
                
            except cx_Oracle.DatabaseError, exc:
                error, = exc.args
                oraerror = "ORA-" + str(error.code)
                #print >> sys.stderr, "Oracle-Error-Message:", error.message
                dlg = wx.MessageDialog(self, error.message, oraerror, wx.OK | wx.ICON_INFORMATION)
                try:
                    result = dlg.ShowModal()
                finally:
                    dlg.Destroy()
                #print "Error conectando a oracle" 
	
        dlg.Destroy()
	event.Skip()

    def OnToolBar1Desconectar_idTool(self, event):
        event.Skip()

    def OnToolBar1Salir_idTool(self, event):
        self.Close()
        event.Skip()

    def OnNotUsedindexBotonButton(self, event):
        if ( conectado == "TRUE"):
            print "Estoy Conectado"
        else:
            print "No estoy conectado"
        event.Skip()
