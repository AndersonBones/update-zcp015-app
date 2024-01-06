If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If

If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If

If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If

If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If

session.findById("wnd[0]").resizeWorkingPane 179,29,false
session.findById("wnd[0]/tbar[0]/okcd").text = "ZCP015"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/tbar[1]/btn[17]").press
session.findById("wnd[1]/usr/txtV-LOW").text = "BIOMASSAF"
session.findById("wnd[1]/usr/txtENAME-LOW").text = "KFREIRE"
session.findById("wnd[1]/usr/txtENAME-LOW").setFocus
session.findById("wnd[1]/usr/txtENAME-LOW").caretPosition = 7
session.findById("wnd[1]/tbar[0]/btn[8]").press
session.findById("wnd[0]/usr/ctxtS_DT_ROM-HIGH").text = "31.12.2024"
session.findById("wnd[0]/usr/ctxtS_DT_ROM-HIGH").setFocus
session.findById("wnd[0]/usr/ctxtS_DT_ROM-HIGH").caretPosition = 0
session.findById("wnd[0]/tbar[1]/btn[8]").press
session.findById("wnd[0]/usr/shell").pressToolbarContextButton "&MB_EXPORT"
session.findById("wnd[0]/usr/shell").selectContextMenuItem "&XXL"
session.findById("wnd[1]/tbar[0]/btn[0]").press
