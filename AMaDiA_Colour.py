# This Python file uses the following encoding: utf-8

# if__name__ == "__main__":
#     pass


# https://doc.qt.io/qt-5/qpalette.html#ColorRole-enum

from PyQt5 import QtCore, QtGui, QtWidgets

def Dark():
    # Inspired by Discord
    tbrush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
    tbrush.setStyle(QtCore.Qt.SolidPattern)

    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush) # Used for tab-text and for the arrows in spinboxes and scrollbars
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush) # Used for Tabs (and their background) and Buttons
    brush = QtGui.QBrush(QtGui.QColor(81, 85, 94))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(67, 71, 78))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(36, 38, 42))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush) # Used for most Text
    brush = QtGui.QBrush(QtGui.QColor(255, 252, 218))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, tbrush) #?
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush) # Used is most places as Text Colour
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush) # Used for Text Field Background
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    # brush = QtGui.QBrush(QtGui.QColor(56, 60, 66))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush) # Used for main background
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush) # Not used (overwritten for every tooltip made in designer?)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush) # Not used (overwritten for every tooltip made in designer?)
    #-----------------------------------------------------------------------------------
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(81, 85, 94))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(67, 71, 78))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(36, 38, 42))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 252, 218))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
    #-----------------------------------------------------------------------------------
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(81, 85, 94))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(67, 71, 78))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(36, 38, 42))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 252, 218))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
    
    #      UI        Special Background Colour  Special Text Colour
    return palette , (54/255, 57/255, 63/255) , (215/255, 213/255, 201/255)

def Bright(): #TODO: Change the Values to a bright theme
    tbrush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
    tbrush.setStyle(QtCore.Qt.SolidPattern)

    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush) # Used for tab-text and for the arrows in spinboxes and scrollbars
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush) # Used for Tabs (and their background) and Buttons
    brush = QtGui.QBrush(QtGui.QColor(81, 85, 94))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(67, 71, 78))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(36, 38, 42))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush) # Used for most Text
    brush = QtGui.QBrush(QtGui.QColor(255, 252, 218))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, tbrush) #?
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush) # Used is most places as Text Colour
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush) # Used for Text Field Background
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    # brush = QtGui.QBrush(QtGui.QColor(56, 60, 66))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush) # Used for main background
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush) #?
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush) # Not used (overwritten for every tooltip made in designer?)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush) # Not used (overwritten for every tooltip made in designer?)
    #-----------------------------------------------------------------------------------
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(81, 85, 94))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(67, 71, 78))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(36, 38, 42))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 252, 218))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(215, 213, 201))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
    #-----------------------------------------------------------------------------------
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(81, 85, 94))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(67, 71, 78))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(36, 38, 42))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 252, 218))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(27, 28, 31))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(54, 57, 63))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
    
    #      UI        Special Background Colour  Special Text Colour
    return palette , (54/255, 57/255, 63/255) , (215/255, 213/255, 201/255)



#----------------- Special -----------------

def Red_ERROR():
    # Inspired by Discord
    brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    text_brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)

    palette = QtGui.QPalette()
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, text_brush) # Used for tab-text and for the arrows in spinboxes and scrollbars
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush) # Used for Tabs (and their background) and Buttons
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, text_brush) # Used for most Text
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, text_brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, text_brush) # Used is most places as Text Colour
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush) # Used for Text Field Background
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush) # Used for main background
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush) #?
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush) # Not used (overwritten for every tooltip made in designer?)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, text_brush) # Not used (overwritten for every tooltip made in designer?)
    #-----------------------------------------------------------------------------------
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, text_brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, text_brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, text_brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, text_brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, text_brush)
    #-----------------------------------------------------------------------------------
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, text_brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, text_brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, text_brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, text_brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, text_brush)
    
    #      UI        Special Background Colour  Special Text Colour
    return palette , (54/255, 57/255, 63/255) , (215/255, 213/255, 201/255)

