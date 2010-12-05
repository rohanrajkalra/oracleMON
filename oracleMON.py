#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import ventPrinc

modules ={u'conectar': [0, '', u'conectar.py'],
 u'conectar2': [0, '', u'conectar2.py'],
 u'ventPrinc': [1, 'Main frame of Application', u'ventPrinc.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = ventPrinc.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
