import xbmcaddon
import xbmcgui
import xbmc
import time

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Set a string variable to use 
line1 = "Hello World! We can write anything we want here Using Python"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1)

time.sleep(2)

xbmc.executebuiltin('Quit()')
# xbmc.executebuiltin('XBMC.Quit()')
