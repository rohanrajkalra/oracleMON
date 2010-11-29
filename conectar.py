#Boa:Dialog:ConectarDialog
# -*- coding: utf-8 -*-
import wx

# begin wxGlade: extracode
# end wxGlade



class ConDialogClass(wx.Dialog):
  def __init__(self, parent, id, title):
    wx.Dialog.__init__(self, parent, id, title)
    self.UserLabel = wx.StaticText(self, -1, "Usuario oracle")
    self.UserText = wx.TextCtrl(self, -1, "")
    self.PassLabel = wx.StaticText(self, -1, "Password")
    self.PassText = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
    self.SidLabel = wx.StaticText(self, -1, "SID")
    self.SidText = wx.TextCtrl(self, -1, "")
    self.AceptarBoton = wx.Button(self,wx.ID_OK, "")
    self.CancelarBoton = wx.Button(self, -1, "CANCELAR")

    self.__set_properties()
    self.__do_layout()
    self.Bind(wx.EVT_BUTTON, self.aceptar_evt, self.AceptarBoton)
    self.Bind(wx.EVT_BUTTON, self.salir_evt, self.CancelarBoton)
      
  def __set_properties(self):
    self.SetTitle(u"Conexión a oracle")
    self.SetSize((350, 250))
    self.UserText.SetFocus()
        
  def __do_layout(self):
    grid_sizer_1 = wx.GridSizer(3, 2, 0, 15)
    grid_sizer_1.Add(self.UserLabel, 0, 0, 0)
    grid_sizer_1.Add(self.UserText, 0, 0, 0)
    grid_sizer_1.Add(self.PassLabel, 0, 0, 0)
    grid_sizer_1.Add(self.PassText, 0, 0, 0)
    grid_sizer_1.Add(self.SidLabel, 0, 0, 0)
    grid_sizer_1.Add(self.SidText, 0, 0, 0)
    grid_sizer_1.Add(self.AceptarBoton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
    grid_sizer_1.Add(self.CancelarBoton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
    self.SetSizer(grid_sizer_1)
    grid_sizer_1.Fit(self)
    self.Layout()
    self.Centre()
                	
  def aceptar_evt(self, event):
    #user = self.UserText.GetValue()
    #passwd = self.PassText.GetValue()
    #sid = self.SidText.GetValue()
    #print "DATOS DE CONEXION: Usuario: "+ user +" Pass: "+ passwd + " SID: "+ sid
    self.Close()
    event.Skip

  def salir_evt(self, event): # wxGlade: ConDialogClass.<event_handler>
    self.Destroy()
