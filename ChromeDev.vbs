set ws=createobject("wscript.shell")
ws.run "chrome --remote-debugging-port=9222 --user-data-dir=E:\selenum\AutomationProfile",0,true
