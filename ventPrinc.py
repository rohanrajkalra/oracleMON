#-----------------------------------------------------------------------------
# Name:        ventPrinc.py
# Purpose:     
#
# Author:      <your name>
#
# Created:     2010/12/04
# RCS-ID:      $Id: ventPrinc.py $
# Copyright:   (c) 2006
# Licence:     <your licence>
#-----------------------------------------------------------------------------
#Boa:Frame:ventPrincFrame

import wx
import wx.grid
import wx.aui

def create(parent):
	return ventPrincFrame(parent)

[wxID_VENTPRINCFRAME, wxID_VENTPRINCFRAMESTATUSBAR1, 
 wxID_VENTPRINCFRAMETOOLBAR1, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_VENTPRINCFRAMETOOLBAR1CONECTAR_ID, 
 wxID_VENTPRINCFRAMETOOLBAR1DESCONECTAR_ID, 
 wxID_VENTPRINCFRAMETOOLBAR1NOT_USED_INDEX_ID, 
 wxID_VENTPRINCFRAMETOOLBAR1PGAADVISOR, wxID_VENTPRINCFRAMETOOLBAR1SALIR_ID, 
 wxID_VENTPRINCFRAMETOOLBAR1TOOLS10, wxID_VENTPRINCFRAMETOOLBAR1TOOLS8, 
 wxID_VENTPRINCFRAMETOOLBAR1TOOLS9, 
] = [wx.NewId() for _init_coll_toolBar1_Tools in range(8)]

class ventPrincFrame(wx.Frame):
    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'img/connect.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1CONECTAR_ID, kind=wx.ITEM_NORMAL,
              label=u'Conectar', longHelp=u'Conectar a oracle',
              shortHelp=u'Conectar')
        parent.DoAddTool(bitmap=wx.Bitmap(u'img/disconnect.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1DESCONECTAR_ID, kind=wx.ITEM_NORMAL,
              label=u'Desconectar', longHelp=u'Desconectar',
              shortHelp=u'Desconectar')
        parent.DoAddTool(bitmap=wx.Bitmap(u'img/exit.png', wx.BITMAP_TYPE_PNG),
              bmpDisabled=wx.NullBitmap, id=wxID_VENTPRINCFRAMETOOLBAR1SALIR_ID,
              kind=wx.ITEM_NORMAL, label=u'Salir', longHelp=u'Salir',
              shortHelp=u'Salir')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wx.Bitmap(u'img/nui.png', wx.BITMAP_TYPE_PNG),
              bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1NOT_USED_INDEX_ID,
              kind=wx.ITEM_NORMAL, label=u'Not used index',
              longHelp=u'Busca los indices no usados usando los datos de AWR',
              shortHelp=u'Busca indices no usados')
        parent.DoAddTool(bitmap=wx.Bitmap(u'img/databaseLarge.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1PGAADVISOR, kind=wx.ITEM_NORMAL,
              label=u'PGA Advisor', longHelp=u'PGA Advisor',
              shortHelp=u'PGA Advisor')
        parent.DoAddTool(bitmap=wx.NullBitmap, bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1TOOLS8, kind=wx.ITEM_NORMAL,
              label='', longHelp='', shortHelp='Tools8')
        parent.DoAddTool(bitmap=wx.NullBitmap, bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1TOOLS9, kind=wx.ITEM_NORMAL,
              label='', longHelp='', shortHelp='Tools9')
        parent.DoAddTool(bitmap=wx.NullBitmap, bmpDisabled=wx.NullBitmap,
              id=wxID_VENTPRINCFRAMETOOLBAR1TOOLS10, kind=wx.ITEM_NORMAL,
              label='', longHelp='', shortHelp='Tools10')
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Conectar_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1CONECTAR_ID)
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Desconectar_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1DESCONECTAR_ID)
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Salir_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1SALIR_ID)
        self.Bind(wx.EVT_TOOL, self.OnToolBar1Not_used_index_idTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1NOT_USED_INDEX_ID)
        self.Bind(wx.EVT_TOOL, self.OnToolBar1PgaadvisorTool,
              id=wxID_VENTPRINCFRAMETOOLBAR1PGAADVISOR)

        parent.Realize()

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(3)

        parent.SetStatusText(number=0, text=u'Desconectado')
        parent.SetStatusText(number=1, text=u'Destino')
        parent.SetStatusText(number=2, text=u' O')

        parent.SetStatusWidths([-3, -1, 30])

    def _init_sizers(self):
        # generated method, don't edit
        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)

        self.toolBar1.SetSizer(self.sizer)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_VENTPRINCFRAME, name=u'ventPrincFrame',
              parent=prnt, pos=wx.Point(416, 206), size=wx.Size(960, 533),
              style=wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE | wx.CLOSE_BOX,
              title=u'oracleMON')
        self.SetClientSize(wx.Size(960, 533))
        self.SetToolTipString(u'oracleMON')
        self.Center(wx.BOTH)

        self.toolBar1 = wx.ToolBar(id=wxID_VENTPRINCFRAMETOOLBAR1,
              name='toolBar1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(368, 48), style=wx.TB_HORIZONTAL | wx.NO_BORDER)
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

        self._init_coll_toolBar1_Tools(self.toolBar1)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        global conectado
        conectado = "FALSE"

    def OnToolBar1Conectar_idTool(self, event):
        import conectar
        
        dlg = conectar.ConDialogClass(self, -1, '')
        run = dlg.ShowModal()
        user = dlg.UserText.GetValue()
        passwd = dlg.PassText.GetValue()
        sid = dlg.SidText.GetValue()
        if len(user) == 0:
            #print "Falta usuario"
            dlg.Destroy()
        elif  len(passwd) == 0:
            #print "Falta password"
            dlg.Close()
        elif len(sid) == 0:
            #print "Faltan sid"
            dlg.Close()
        else:
            #print "Vamos a conectar"
            import cx_Oracle
            import sys
            global connection
            (user,passwd,sid) = (str(dlg.UserText.GetValue()),str(dlg.PassText.GetValue()),str(dlg.SidText.GetValue()))
            #print "DATOS DE CONEXION: Usuario: "+ user +" Pass: "+ passwd + " SID: "+ sid
            try:
                if user == 'sys':
                    connection = cx_Oracle.connect(user, passwd, sid, mode = cx_Oracle.SYSDBA)
                    constring = user+"@"+sid+" as sysdba"
                else:
                    connection = cx_Oracle.connect( user , passwd , sid )
                    constring = user+"@"+sid
                #print "Conectado a oracle"
                global conectado
                conectado = "TRUE"
                
                self.statusBar1.SetStatusText("Conectado",0)
                self.statusBar1.SetStatusText(constring,1)
                #self.staticBitmap1.SetBitmap(bitmap=wx.Bitmap(u'img/green.png'))
                
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
        cursor.close()
        connection.close()
        self.statusBar1.SetStatusText("Desconectado",0)
        self.statusBar1.SetStatusText("************",1)
        event.Skip()

    def OnToolBar1Salir_idTool(self, event):
        self.Close()
        event.Skip()

    def OnToolBar1Not_used_index_idTool(self, event):
        if ( conectado == "TRUE"):
            #print "Estoy Conectado"
            cursor = connection.cursor()
            cursor.execute("""SELECT n.OWNER ||'.'|| n.TABLE_NAME as TABLA, n.OWNER||'.'||n.INDEX_NAME as INDICE, d.NUM_ROWS AS TOTAL 
			    FROM DBA_TABLES d INNER JOIN NOT_USED_INDEX_MV n ON d.TABLE_NAME = n.TABLE_NAME AND d.OWNER = n.OWNER 
			    WHERE (d.NUM_ROWS >0) AND n.INDEX_NAME in (select INDEX_NAME from DBA_INDEXES) 
			    AND n.OWNER not in ('CTXSYS','EYPS_COUNTRY') AND n.INDEX_NAME not like 'DR$%' 
			    AND n.TABLE_NAME in (select TABLA from table_usage_mv where ACCESOS >= 1) 
			    AND n.INDEX_NAME in (select index_name from index_creation_date_mv where to_date(fecha) <= SYSDATE -35) 
			    ORDER BY TOTAL desc,n.owner, n.TABLE_NAME""")

            resultado = cursor.fetchall()
            num_rows = cursor.rowcount
	    print "numero de rows: ",num_rows

	    #notegrid = wx.Notebook(self,name='notegrid', pos=wx.Point(1, 1), size=wx.Size(958, 460), style=0)
	    notegrid = wx.aui.AuiNotebook(self)
	    rgrid = wx.grid.Grid(parent=notegrid,name='rgrid', 
            pos=wx.Point(0, 0), size=wx.Size(956, 427), style=0 )
	    notegrid.AddPage(rgrid, 'NOT_USED_INDEX')
	    #sizer = wx.BoxSizer()
	    self.sizer.Add(notegrid, 1, wx.EXPAND)
	    #self.SetSizer(sizer)
	    numpages = notegrid.GetPageCount()
	    print "Es la primera pasada",numpages
	    rgrid.CreateGrid(num_rows,3)
	    rgrid.SetColLabelValue(0,'TABLA')
	    rgrid.SetColLabelValue(1,'INDICE')
	    rgrid.SetColLabelValue(2,'Numero de filas')
	    rgrid.ForceRefresh()    
            
            r = 0
            for row in resultado:
		    total = str(row[2])
            	    rgrid.SetCellValue(r,0,row[0])
                    rgrid.SetCellValue(r,1,row[1])
                    rgrid.SetCellValue(r,2,total)
                    r = r+1
            
            rgrid.AutoSizeColumns(True)
            cursor.close()
    	else:
            dlg = wx.MessageDialog(self, 'No estas conectado a Oracle', 'ATENCION', wx.OK | wx.ICON_INFORMATION)
            try:
                result = dlg.ShowModal()
            finally:
                dlg.Destroy()
        event.Skip()

    def OnToolBar1PgaadvisorTool(self, event):
		if (conectado == "TRUE"):
		    cursor = connection.cursor()
		    cursor.execute("""SELECT PGA_TARGET_FACTOR Factor,ROUND(pga_target_for_estimate/1024/1024) target_mb, 
		    estd_pga_cache_hit_percentage cache_hit_perc, estd_overalloc_count 
		    FROM v$pga_target_advice""")

		    resultado = cursor.fetchall()
		    num_rows = cursor.rowcount
		    self.results_grid.ClearGrid()
		    self.results_grid.Show(True)
		    self.results_grid.Enable(True)
		    self.results_grid.CreateGrid(num_rows,4)
		    self.results_grid.SetColLabelValue(0,'FACTOR')
		    self.results_grid.SetColLabelValue(0,'PGA Target MB')
		    self.results_grid.SetColLabelValue(0,'CACHE HIT %')
		    self.results_grid.SetColLabelValue(0,'ESTD_OVERALLOC_COUNT')
		    self.results_grid.ForceRefresh()

		    r = 0
		    for row in resultado:
			    print row
			    (factor,target,hit,estd) = (str(row[0]),str(row[1]),str(row[2]),str(row[3]))
			    self.results_grid.SetCellValue(r,0,factor)
			    self.results_grid.SetCellValue(r,1,target)
			    self.results_grid.SetCellValue(r,2,hit)
			    self.results_grid.SetCellValue(r,0,estd)
			    r = r+1

		    self.results_grid.AutoSizeColumns(True)
		    cursor.close()
			
		else:
			dlg = wx.MessageDialog(self, 'No estas conectado a Oracle', 'ATENCION', wx.OK | wx.ICON_INFORMATION)
			try:
				result = dlg.ShowModal()
                	finally:                  
				dlg.Destroy()         

        	event.Skip()
